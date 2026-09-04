#!/usr/bin/env python3
"""
CIVOPS-Radar: Flask Web Server
Author: CIVOPS-Radar Contributors
License: MIT
"""

import os
import json
import sqlite3
import math
from datetime import datetime
from flask import Flask, render_template, jsonify, request, send_file
from flask_cors import CORS
import io
import csv
import sys
import queue

# Add server dir to path so camera_oui imports correctly
sys.path.insert(0, os.path.dirname(__file__))
from camera_oui import lookup_camera, get_camera_count, CAMERA_OUI_DB


# Configuration
RADAR_DIR = os.environ.get("RADAR_DIR", os.path.expanduser("~/radar"))
DB_PATH = os.path.join(RADAR_DIR, "data", "scans.db")
EXPORT_DIR = os.path.join(RADAR_DIR, "exports")

app = Flask(__name__)
CORS(app)

scan_queue = queue.Queue()

# ═══════════════════════════════════════════════════════════════════
#  CAMERA OUI DATABASE
#  OUI = first 3 bytes of MAC address (identifies manufacturer)
#  Source: IEEE OUI registry + manual research
# ═══════════════════════════════════════════════════════════════════
CAMERA_OUI_DB = {
    # ── Hikvision (largest IP camera manufacturer) ───────────────
    "28:57:be": {"brand": "Hikvision", "type": "IP Camera"},
    "c0:56:e3": {"brand": "Hikvision", "type": "IP Camera"},
    "bc:ad:28": {"brand": "Hikvision", "type": "IP Camera"},
    "44:19:b6": {"brand": "Hikvision", "type": "IP Camera"},
    "88:c3:97": {"brand": "Hikvision", "type": "IP Camera"},
    "34:ea:34": {"brand": "Hikvision", "type": "IP Camera"},
    "4c:c7:d3": {"brand": "Hikvision", "type": "IP Camera"},
    "ec:a8:6b": {"brand": "Hikvision", "type": "IP Camera"},
    "0c:97:1e": {"brand": "Hikvision", "type": "IP Camera"},
    "f4:a4:75": {"brand": "Hikvision", "type": "IP Camera"},
    "d4:e8:53": {"brand": "Hikvision", "type": "IP Camera"},
    "a4:14:37": {"brand": "Hikvision", "type": "IP Camera"},
    "54:c4:15": {"brand": "Hikvision", "type": "IP Camera"},
    "10:12:fb": {"brand": "Hikvision", "type": "IP Camera"},
    "e4:24:6c": {"brand": "Hikvision", "type": "IP Camera"},
    "68:ef:bd": {"brand": "Hikvision", "type": "IP Camera"},
    "08:a1:89": {"brand": "Hikvision", "type": "IP Camera"},
    "b4:a3:82": {"brand": "Hikvision", "type": "IP Camera"},
    "1c:54:6a": {"brand": "Hikvision", "type": "IP Camera"},

    # ── Dahua Technology ─────────────────────────────────────────
    "90:02:a9": {"brand": "Dahua", "type": "IP Camera"},
    "3c:ef:8c": {"brand": "Dahua", "type": "IP Camera"},
    "e0:50:8b": {"brand": "Dahua", "type": "IP Camera"},
    "4c:11:bf": {"brand": "Dahua", "type": "IP Camera"},
    "bc:32:b2": {"brand": "Dahua", "type": "IP Camera"},
    "80:26:89": {"brand": "Dahua", "type": "IP Camera"},
    "a0:f3:c1": {"brand": "Dahua", "type": "IP Camera"},
    "f4:2f:5b": {"brand": "Dahua", "type": "IP Camera"},

    # ── Axis Communications ──────────────────────────────────────
    "00:40:8c": {"brand": "Axis", "type": "IP Camera"},
    "ac:cc:8e": {"brand": "Axis", "type": "IP Camera"},
    "d4:e0:8e": {"brand": "Axis", "type": "IP Camera"},
    "b8:a4:4f": {"brand": "Axis", "type": "IP Camera"},
    "00:4a:23": {"brand": "Axis", "type": "IP Camera"},

    # ── Ring (Amazon) ─────────────────────────────────────────────
    "d0:23:db": {"brand": "Ring", "type": "Doorbell/Camera"},
    "14:7d:da": {"brand": "Ring", "type": "Doorbell/Camera"},
    "fc:a6:67": {"brand": "Ring", "type": "Doorbell/Camera"},
    "b0:9f:ba": {"brand": "Ring", "type": "Doorbell/Camera"},
    "2c:f4:32": {"brand": "Ring", "type": "Doorbell/Camera"},
    "78:8c:b5": {"brand": "Ring", "type": "Doorbell/Camera"},

    # ── Nest / Google ─────────────────────────────────────────────
    "18:b4:30": {"brand": "Nest", "type": "Smart Camera"},
    "64:16:66": {"brand": "Nest", "type": "Smart Camera"},
    "a4:77:33": {"brand": "Nest", "type": "Smart Camera"},
    "d8:a3:5c": {"brand": "Nest/Google", "type": "Smart Camera"},
    "04:f8:f8": {"brand": "Nest", "type": "Smart Camera"},
    "84:5a:3e": {"brand": "Nest/Google", "type": "Smart Camera"},

    # ── Arlo (Netgear) ────────────────────────────────────────────
    "48:1d:70": {"brand": "Arlo", "type": "Wireless Camera"},
    "6c:f3:73": {"brand": "Arlo", "type": "Wireless Camera"},
    "44:a5:6e": {"brand": "Arlo", "type": "Wireless Camera"},
    "04:18:d6": {"brand": "Arlo", "type": "Wireless Camera"},

    # ── Wyze Labs ─────────────────────────────────────────────────
    "2c:aa:8e": {"brand": "Wyze", "type": "Smart Camera"},
    "7c:78:b2": {"brand": "Wyze", "type": "Smart Camera"},
    "d0:52:a8": {"brand": "Wyze", "type": "Smart Camera"},
    "a8:5b:78": {"brand": "Wyze", "type": "Smart Camera"},

    # ── Reolink ───────────────────────────────────────────────────
    "ec:71:db": {"brand": "Reolink", "type": "IP Camera"},
    "dc:44:27": {"brand": "Reolink", "type": "IP Camera"},
    "14:0a:c5": {"brand": "Reolink", "type": "IP Camera"},

    # ── Amcrest ───────────────────────────────────────────────────
    "9c:8e:cd": {"brand": "Amcrest", "type": "IP Camera"},
    "00:1e:c0": {"brand": "Amcrest", "type": "IP Camera"},

    # ── Foscam ────────────────────────────────────────────────────
    "00:0c:e6": {"brand": "Foscam", "type": "IP Camera"},
    "c4:2f:56": {"brand": "Foscam", "type": "IP Camera"},
    "e0:62:90": {"brand": "Foscam", "type": "IP Camera"},

    # ── Eufy (Anker) ──────────────────────────────────────────────
    "48:86:e8": {"brand": "Eufy", "type": "Smart Camera"},
    "d4:5b:89": {"brand": "Eufy", "type": "Smart Camera"},
    "c0:49:ef": {"brand": "Eufy", "type": "Smart Camera"},
    "f4:4d:30": {"brand": "Eufy", "type": "Smart Camera"},

    # ── TP-Link Tapo ──────────────────────────────────────────────
    "10:27:f5": {"brand": "TP-Link Tapo", "type": "Smart Camera"},
    "14:cc:20": {"brand": "TP-Link Tapo", "type": "Smart Camera"},
    "50:c7:bf": {"brand": "TP-Link Tapo", "type": "Smart Camera"},
    "54:af:97": {"brand": "TP-Link Tapo", "type": "Smart Camera"},
    "b0:be:76": {"brand": "TP-Link Tapo", "type": "Smart Camera"},
    "90:9a:4a": {"brand": "TP-Link Tapo", "type": "Smart Camera"},
    "1c:61:b4": {"brand": "TP-Link Tapo", "type": "Smart Camera"},
    "60:32:b1": {"brand": "TP-Link Tapo", "type": "Smart Camera"},

    # ── Ezviz (Hikvision sub-brand) ───────────────────────────────
    "40:31:3c": {"brand": "Ezviz", "type": "Smart Camera"},
    "bc:dd:c2": {"brand": "Ezviz", "type": "Smart Camera"},
    "c4:02:05": {"brand": "Ezviz", "type": "Smart Camera"},

    # ── Yi Technology ─────────────────────────────────────────────
    "7c:49:eb": {"brand": "Yi", "type": "Smart Camera"},
    "78:9c:85": {"brand": "Yi", "type": "Smart Camera"},
    "34:ce:00": {"brand": "Yi", "type": "Smart Camera"},

    # ── Swann ─────────────────────────────────────────────────────
    "00:1e:46": {"brand": "Swann", "type": "IP Camera"},

    # ── Bosch ─────────────────────────────────────────────────────
    "00:07:5f": {"brand": "Bosch", "type": "IP Camera"},
    "00:0e:5c": {"brand": "Bosch", "type": "IP Camera"},

    # ── Hanwha (Samsung Techwin) ──────────────────────────────────
    "00:09:18": {"brand": "Hanwha/Samsung", "type": "IP Camera"},
    "00:09:45": {"brand": "Hanwha/Samsung", "type": "IP Camera"},
    "30:14:4a": {"brand": "Hanwha/Samsung", "type": "IP Camera"},
    "7c:e9:d3": {"brand": "Hanwha/Samsung", "type": "IP Camera"},

    # ── Vivotek ───────────────────────────────────────────────────
    "00:02:d1": {"brand": "Vivotek", "type": "IP Camera"},
    "00:66:19": {"brand": "Vivotek", "type": "IP Camera"},
    "00:69:11": {"brand": "Vivotek", "type": "IP Camera"},

    # ── Uniview (UNV) ─────────────────────────────────────────────
    "48:ea:63": {"brand": "Uniview", "type": "IP Camera"},
    "c0:f4:e6": {"brand": "Uniview", "type": "IP Camera"},

    # ── Pelco ─────────────────────────────────────────────────────
    "00:07:6d": {"brand": "Pelco", "type": "IP Camera"},

    # ── Avigilon ─────────────────────────────────────────────────
    "00:18:85": {"brand": "Avigilon", "type": "IP Camera"},
    "e0:1c:41": {"brand": "Avigilon", "type": "IP Camera"},

    # ── Mobotix ───────────────────────────────────────────────────
    "00:00:12": {"brand": "Mobotix", "type": "IP Camera"},

    # ── FLIR Systems ──────────────────────────────────────────────
    "00:40:7f": {"brand": "FLIR", "type": "Thermal Camera"},
    "d0:4f:7e": {"brand": "FLIR", "type": "Thermal Camera"},

    # ── Zmodo ─────────────────────────────────────────────────────
    "ac:d0:74": {"brand": "Zmodo", "type": "IP Camera"},

    # ── Lorex (Dahua sub-brand) ───────────────────────────────────
    "00:d0:f1": {"brand": "Lorex", "type": "IP Camera"},
    "00:1e:11": {"brand": "Lorex", "type": "IP Camera"},

    # ── Annke ─────────────────────────────────────────────────────
    "c8:02:10": {"brand": "Annke", "type": "IP Camera"},

    # ── Tenvis ────────────────────────────────────────────────────
    "d8:96:85": {"brand": "Tenvis", "type": "IP Camera"},

    # ── Wansview ──────────────────────────────────────────────────
    "dc:0b:34": {"brand": "Wansview", "type": "IP Camera"},

    # ── Blink (Amazon) ────────────────────────────────────────────
    "44:61:32": {"brand": "Blink", "type": "Wireless Camera"},
    "74:75:48": {"brand": "Blink", "type": "Wireless Camera"},

    # ── Canary ────────────────────────────────────────────────────
    "e4:f0:42": {"brand": "Canary", "type": "Smart Camera"},

    # ── Logi Circle (Logitech) ────────────────────────────────────
    "00:04:6b": {"brand": "Logitech", "type": "Webcam/Camera"},

    # ── Owlet ─────────────────────────────────────────────────────
    "44:a8:42": {"brand": "Owlet", "type": "Baby Camera"},

    # ── Infant Optics ─────────────────────────────────────────────
    "f8:f0:05": {"brand": "Infant Optics", "type": "Baby Camera"},

    # ── Nooie ─────────────────────────────────────────────────────
    "00:15:61": {"brand": "Nooie", "type": "Smart Camera"},

    # ── iRobot (has cameras) ──────────────────────────────────────
    "50:14:79": {"brand": "iRobot", "type": "Robot Camera"},
    "80:20:da": {"brand": "iRobot", "type": "Robot Camera"},

    # ── Aqara ─────────────────────────────────────────────────────
    "54:ef:44": {"brand": "Aqara", "type": "Smart Camera"},

    # ── Imou (Dahua consumer brand) ───────────────────────────────
    "44:80:eb": {"brand": "Imou", "type": "Smart Camera"},
    "bc:32:b2": {"brand": "Imou/Dahua", "type": "Smart Camera"},

    # ── Sricam ────────────────────────────────────────────────────
    "00:af:1f": {"brand": "Sricam", "type": "IP Camera"},

    # ── Vstarcam ──────────────────────────────────────────────────
    "c4:13:e2": {"brand": "Vstarcam", "type": "IP Camera"},

    # ── Guardzilla ────────────────────────────────────────────────
    "b4:43:0d": {"brand": "Guardzilla", "type": "Smart Camera"},

    # ── D-Link cameras ────────────────────────────────────────────
    "1c:7e:e5": {"brand": "D-Link", "type": "IP Camera"},
    "34:08:04": {"brand": "D-Link", "type": "IP Camera"},
    "f0:7d:68": {"brand": "D-Link", "type": "IP Camera"},
    "90:f6:52": {"brand": "D-Link", "type": "IP Camera"},
    "00:05:5d": {"brand": "D-Link", "type": "IP Camera"},

    # ── Netgear cameras ───────────────────────────────────────────
    "a0:63:91": {"brand": "Netgear", "type": "IP Camera"},
    "b0:39:56": {"brand": "Netgear", "type": "IP Camera"},

    # ── Ubiquiti UniFi cameras ────────────────────────────────────
    "00:27:22": {"brand": "Ubiquiti", "type": "IP Camera"},
    "04:18:d6": {"brand": "Ubiquiti", "type": "IP Camera"},
    "24:a4:3c": {"brand": "Ubiquiti", "type": "IP Camera"},
    "78:8a:20": {"brand": "Ubiquiti", "type": "IP Camera"},
    "f4:92:bf": {"brand": "Ubiquiti UniFi", "type": "IP Camera"},

    # ── Amcrest/Zosi ──────────────────────────────────────────────
    "00:18:ae": {"brand": "Zosi", "type": "IP Camera"},

    # ── Tiandy ────────────────────────────────────────────────────
    "e4:ab:89": {"brand": "Tiandy", "type": "IP Camera"},

    # ── Milesight ─────────────────────────────────────────────────
    "e8:eb:1b": {"brand": "Milesight", "type": "IP Camera"},

    # ── LTS Security ─────────────────────────────────────────────
    "9c:a3:a9": {"brand": "LTS Security", "type": "IP Camera"},

    # ── TVT Digital ───────────────────────────────────────────────
    "00:1d:c1": {"brand": "TVT Digital", "type": "IP Camera"},

    # ── CP Plus ───────────────────────────────────────────────────
    "b4:ee:b4": {"brand": "CP Plus", "type": "IP Camera"},
    "d4:df:9a": {"brand": "CP Plus", "type": "IP Camera"},

    # ── Honeywell cameras ─────────────────────────────────────────
    "00:04:2a": {"brand": "Honeywell", "type": "IP Camera"},
    "00:30:6e": {"brand": "Honeywell", "type": "IP Camera"},

    # ── Hanwha Vision ─────────────────────────────────────────────
    "84:eb:18": {"brand": "Hanwha Vision", "type": "IP Camera"},

    # ── GeoVision ─────────────────────────────────────────────────
    "00:13:e2": {"brand": "GeoVision", "type": "IP Camera"},

    # ── March Networks ────────────────────────────────────────────
    "00:0f:bc": {"brand": "March Networks", "type": "IP Camera"},

    # ── IndigoVision ─────────────────────────────────────────────
    "00:16:d2": {"brand": "IndigoVision", "type": "IP Camera"},

    # ── Illustra (Tyco) ───────────────────────────────────────────
    "00:09:e7": {"brand": "Illustra/Tyco", "type": "IP Camera"},

    # ── 360 Smart Camera (Qihoo) ──────────────────────────────────
    "90:c7:d8": {"brand": "360 Smart", "type": "Smart Camera"},
    "4c:1a:3d": {"brand": "360 Smart", "type": "Smart Camera"},

    # ── Xiaomi / Mi Home cameras ──────────────────────────────────
    "78:11:dc": {"brand": "Xiaomi Mi", "type": "Smart Camera"},
    "28:6c:07": {"brand": "Xiaomi Mi", "type": "Smart Camera"},
    "34:80:b3": {"brand": "Xiaomi Mi", "type": "Smart Camera"},
    "58:44:98": {"brand": "Xiaomi Mi", "type": "Smart Camera"},
    "64:09:80": {"brand": "Xiaomi Mi", "type": "Smart Camera"},
    "78:02:f8": {"brand": "Xiaomi Mi", "type": "Smart Camera"},
    "f8:a4:5f": {"brand": "Xiaomi Mi", "type": "Smart Camera"},
    "a4:c1:38": {"brand": "Xiaomi Mi", "type": "Smart Camera"},

    # ── Tuya-based cameras (massive white-label ecosystem) ────────
    "00:1e:1b": {"brand": "Tuya OEM", "type": "Smart Camera"},
    "20:f4:1b": {"brand": "Tuya OEM", "type": "Smart Camera"},
    "b0:f8:93": {"brand": "Tuya OEM", "type": "Smart Camera"},
    "d8:f1:5b": {"brand": "Tuya OEM", "type": "Smart Camera"},
    "e8:db:84": {"brand": "Tuya OEM", "type": "Smart Camera"},

    # ── Genie / Genie Access ──────────────────────────────────────
    "00:22:b0": {"brand": "Genie", "type": "IP Camera"},

    # ── LG Innotek ────────────────────────────────────────────────
    "00:e0:91": {"brand": "LG Innotek", "type": "IP Camera"},

    # ── Panasonic IP cameras ───────────────────────────────────────
    "00:80:45": {"brand": "Panasonic", "type": "IP Camera"},
    "00:0d:fd": {"brand": "Panasonic", "type": "IP Camera"},
    "08:00:6b": {"brand": "Panasonic", "type": "IP Camera"},
    "00:a0:de": {"brand": "Panasonic", "type": "IP Camera"},

    # ── Sony cameras ──────────────────────────────────────────────
    "00:01:4a": {"brand": "Sony", "type": "IP Camera"},
    "00:13:a9": {"brand": "Sony", "type": "IP Camera"},
    "00:d0:d7": {"brand": "Sony", "type": "IP Camera"},
    "ac:9b:0a": {"brand": "Sony", "type": "IP Camera"},

    # ── Canon network cameras ─────────────────────────────────────
    "00:02:a0": {"brand": "Canon", "type": "Network Camera"},
    "00:21:b7": {"brand": "Canon", "type": "Network Camera"},
    "00:c0:ee": {"brand": "Canon", "type": "Network Camera"},

    # ── Hikvision OEM brands ──────────────────────────────────────
    "70:5d:cc": {"brand": "Hikvision OEM", "type": "IP Camera"},
    "c8:02:8f": {"brand": "Hikvision OEM", "type": "IP Camera"},
}


def lookup_camera(bssid: str):
    """Check if a BSSID belongs to a known camera manufacturer."""
    if not bssid or len(bssid) < 8:
        return None
    oui = bssid[:8].lower()
    return CAMERA_OUI_DB.get(oui)


class RadarData:
    def __init__(self, db_path):
        self.db_path = db_path
        self.ensure_database()

    def ensure_database(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                bssid TEXT NOT NULL,
                ssid TEXT,
                capabilities TEXT,
                frequency INTEGER,
                level INTEGER,
                distance REAL,
                risk_score INTEGER DEFAULT 0,
                is_hidden BOOLEAN DEFAULT 0,
                is_open BOOLEAN DEFAULT 0,
                vendor TEXT,
                first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                scan_count INTEGER DEFAULT 1
            )
        ''')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_bssid ON scans(bssid)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_timestamp ON scans(timestamp)')
        conn.commit()
        conn.close()

    def get_latest_scans(self, limit=100):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        query = '''
            SELECT bssid, ssid, capabilities, frequency, level, distance,
                   risk_score, is_hidden, is_open, vendor, first_seen, last_seen,
                   scan_count, timestamp
            FROM scans s1
            WHERE timestamp = (SELECT MAX(timestamp) FROM scans s2 WHERE s2.bssid = s1.bssid)
            ORDER BY timestamp DESC LIMIT ?
        '''
        cursor.execute(query, (limit,))
        columns = [d[0] for d in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return results

    def get_scan_statistics(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        stats = {}
        cursor.execute("SELECT COUNT(DISTINCT bssid) FROM scans")
        stats['total_networks'] = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM scans WHERE timestamp > datetime('now', '-5 minutes')")
        stats['active_networks'] = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM scans WHERE risk_score > 50 AND timestamp > datetime('now', '-5 minutes')")
        stats['high_risk_networks'] = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM scans WHERE is_open = 1 AND timestamp > datetime('now', '-5 minutes')")
        stats['open_networks'] = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM scans WHERE is_hidden = 1 AND timestamp > datetime('now', '-5 minutes')")
        stats['hidden_networks'] = cursor.fetchone()[0]
        conn.close()
        return stats

    def calculate_radar_position(self, bssid, level, distance):
        hash_val = hash(bssid) % 360
        angle = math.radians(hash_val)
        max_distance = 200
        normalized_distance = min(distance / max_distance, 1.0) if distance else 0.5
        radius = (1 - normalized_distance) * 0.8
        return {
            'x': radius * math.cos(angle),
            'y': radius * math.sin(angle),
            'angle': hash_val,
            'radius': radius
        }

    def export_data(self, format_type='json'):
        scans = self.get_latest_scans(limit=1000)
        if format_type == 'json':
            return json.dumps(scans, indent=2, default=str)
        elif format_type == 'csv':
            output = io.StringIO()
            if scans:
                writer = csv.DictWriter(output, fieldnames=scans[0].keys())
                writer.writeheader()
                writer.writerows(scans)
            return output.getvalue()
        else:
            raise ValueError(f"Unsupported format: {format_type}")


radar_data = RadarData(DB_PATH)


@app.route('/')
def index():
    return render_template('radar.html')


@app.route('/api/signals')
def get_signals():
    try:
        scans = radar_data.get_latest_scans(limit=100)
        radar_signals = []
        for scan in scans:
            position = radar_data.calculate_radar_position(
                scan['bssid'], scan['level'], scan['distance'])
            cam = lookup_camera(scan['bssid'])
            signal = {
                'bssid': scan['bssid'],
                'ssid': scan['ssid'] or 'Hidden',
                'level': scan['level'],
                'distance': scan['distance'],
                'risk_score': scan['risk_score'],
                'is_hidden': scan['is_hidden'],
                'is_open': scan['is_open'],
                'capabilities': scan['capabilities'],
                'frequency': scan['frequency'],
                'vendor': scan['vendor'],
                'last_seen': scan['last_seen'],
                'scan_count': scan['scan_count'],
                'position': position,
                'is_camera': cam is not None,
                'camera_brand': cam['brand'] if cam else None,
                'camera_type': cam['type'] if cam else None,
            }
            radar_signals.append(signal)
        return jsonify({'signals': radar_signals, 'timestamp': datetime.now().isoformat()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/cameras')
def get_cameras():
    """Return only networks identified as cameras."""
    try:
        scans = radar_data.get_latest_scans(limit=200)
        cameras = []
        for scan in scans:
            cam = lookup_camera(scan['bssid'])
            if cam:
                cameras.append({
                    'bssid': scan['bssid'],
                    'ssid': scan['ssid'] or 'Hidden',
                    'brand': cam['brand'],
                    'type': cam['type'],
                    'level': scan['level'],
                    'distance': scan['distance'],
                    'risk_score': scan['risk_score'],
                    'capabilities': scan['capabilities'],
                    'frequency': scan['frequency'],
                    'last_seen': scan['last_seen'],
                    'is_open': scan['is_open'],
                })
        cameras.sort(key=lambda x: x['level'], reverse=True)
        return jsonify({'cameras': cameras, 'count': len(cameras)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/statistics')
def get_statistics():
    try:
        stats = radar_data.get_scan_statistics()
        # Add camera count
        scans = radar_data.get_latest_scans(limit=200)
        stats['camera_count'] = sum(1 for s in scans if lookup_camera(s['bssid']))
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/export/<format_type>')
def export_data(format_type):
    try:
        if format_type not in ['json', 'csv']:
            return jsonify({'error': 'Unsupported format'}), 400
        data = radar_data.export_data(format_type)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"radar_export_{timestamp}.{format_type}"
        filepath = os.path.join(EXPORT_DIR, filename)
        os.makedirs(EXPORT_DIR, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(data)
        return send_file(filepath, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/network/<bssid>')
def get_network_details(bssid):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM scans WHERE bssid = ? ORDER BY timestamp DESC LIMIT 1', (bssid,))
        columns = [d[0] for d in cursor.description]
        result = cursor.fetchone()
        conn.close()
        if result:
            network = dict(zip(columns, result))
            cam = lookup_camera(bssid)
            network['is_camera'] = cam is not None
            network['camera_brand'] = cam['brand'] if cam else None
            network['camera_type'] = cam['type'] if cam else None
            return jsonify(network)
        return jsonify({'error': 'Not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/scan/start')
def start_scan():
    return jsonify({'status': 'scan_started'})


@app.route('/api/scan/stop')
def stop_scan():
    return jsonify({'status': 'scan_stopped'})


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


def run_server(host='0.0.0.0', port=5000, debug=False):
    print(f"Starting CIVOPS-Radar web server...")
    print(f"Web interface: http://{host}:{port}")
    app.run(host=host, port=port, debug=debug, threaded=True)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='CIVOPS-Radar Web Server')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=5000)
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    run_server(host=args.host, port=args.port, debug=args.debug)

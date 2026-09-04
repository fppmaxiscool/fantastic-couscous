"""
CIVOPS-Radar: Comprehensive Camera OUI Database
Maps MAC address prefixes (OUI) to camera manufacturers.
OUI = first 3 bytes of a device's MAC/BSSID address.
Source: IEEE OUI registry + security research databases.
"""

# Format: "xx:xx:xx": {"brand": "...", "type": "...", "country": "..."}
CAMERA_OUI_DB = {

    # ═══════════════════════════════════════════════════════════
    #  HIKVISION — World's largest IP camera manufacturer (China)
    # ═══════════════════════════════════════════════════════════
    "28:57:be": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "c0:56:e3": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "bc:ad:28": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "44:19:b6": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "88:c3:97": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "34:ea:34": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "4c:c7:d3": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "ec:a8:6b": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "0c:97:1e": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "f4:a4:75": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "d4:e8:53": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "a4:14:37": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "54:c4:15": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "10:12:fb": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "e4:24:6c": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "68:ef:bd": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "08:a1:89": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "b4:a3:82": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "1c:54:6a": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "70:5d:cc": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "c8:02:8f": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "f8:9a:78": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "3c:2e:ff": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "ac:1d:df": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "a4:b1:e9": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "dc:2c:6e": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "08:e9:f6": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "28:26:97": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "2c:d1:67": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "48:ea:63": {"brand": "Hikvision", "type": "NVR/DVR", "country": "CN"},
    "a0:ac:1a": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "5c:4a:1f": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "cc:d3:9d": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "d0:c5:f3": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  DAHUA TECHNOLOGY (China)
    # ═══════════════════════════════════════════════════════════
    "90:02:a9": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "3c:ef:8c": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "e0:50:8b": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "4c:11:bf": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "bc:32:b2": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "80:26:89": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "a0:f3:c1": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "f4:2f:5b": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "40:7c:7d": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "b4:c4:fc": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "98:02:84": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "d4:12:43": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "40:64:ca": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "30:9c:23": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "c8:43:57": {"brand": "Dahua", "type": "NVR", "country": "CN"},
    "28:24:ff": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "e0:d5:55": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "14:75:90": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  AXIS COMMUNICATIONS (Sweden)
    # ═══════════════════════════════════════════════════════════
    "00:40:8c": {"brand": "Axis", "type": "Network Camera", "country": "SE"},
    "ac:cc:8e": {"brand": "Axis", "type": "Network Camera", "country": "SE"},
    "d4:e0:8e": {"brand": "Axis", "type": "Network Camera", "country": "SE"},
    "b8:a4:4f": {"brand": "Axis", "type": "Network Camera", "country": "SE"},
    "00:4a:23": {"brand": "Axis", "type": "Network Camera", "country": "SE"},
    "ac:8f:f9": {"brand": "Axis", "type": "Network Camera", "country": "SE"},
    "00:b8:2c": {"brand": "Axis", "type": "Network Camera", "country": "SE"},
    "00:0b:d0": {"brand": "Axis", "type": "Network Camera", "country": "SE"},

    # ═══════════════════════════════════════════════════════════
    #  RING (Amazon) — USA
    # ═══════════════════════════════════════════════════════════
    "d0:23:db": {"brand": "Ring", "type": "Video Doorbell", "country": "US"},
    "14:7d:da": {"brand": "Ring", "type": "Video Doorbell", "country": "US"},
    "fc:a6:67": {"brand": "Ring", "type": "Floodlight Cam", "country": "US"},
    "b0:9f:ba": {"brand": "Ring", "type": "Spotlight Cam", "country": "US"},
    "2c:f4:32": {"brand": "Ring", "type": "Indoor Cam", "country": "US"},
    "78:8c:b5": {"brand": "Ring", "type": "Video Doorbell", "country": "US"},
    "20:eb:4e": {"brand": "Ring", "type": "Outdoor Cam", "country": "US"},
    "34:ab:37": {"brand": "Ring", "type": "Video Doorbell Pro", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  NEST / GOOGLE (USA)
    # ═══════════════════════════════════════════════════════════
    "18:b4:30": {"brand": "Google Nest", "type": "Indoor Cam", "country": "US"},
    "64:16:66": {"brand": "Google Nest", "type": "Outdoor Cam", "country": "US"},
    "a4:77:33": {"brand": "Google Nest", "type": "Doorbell", "country": "US"},
    "d8:a3:5c": {"brand": "Google Nest", "type": "Smart Camera", "country": "US"},
    "04:f8:f8": {"brand": "Google Nest", "type": "Cam IQ", "country": "US"},
    "84:5a:3e": {"brand": "Google Nest", "type": "Cam IQ Outdoor", "country": "US"},
    "28:6c:07": {"brand": "Google", "type": "Nest Hub Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ARLO (Netgear) — USA
    # ═══════════════════════════════════════════════════════════
    "48:1d:70": {"brand": "Arlo", "type": "Wire-Free Camera", "country": "US"},
    "6c:f3:73": {"brand": "Arlo", "type": "Pro 3/4", "country": "US"},
    "44:a5:6e": {"brand": "Arlo", "type": "Ultra 2", "country": "US"},
    "04:18:d6": {"brand": "Arlo", "type": "Essential Cam", "country": "US"},
    "c8:93:46": {"brand": "Arlo", "type": "Pro 2", "country": "US"},
    "00:b0:c8": {"brand": "Arlo", "type": "Doorbell", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  WYZE LABS — USA
    # ═══════════════════════════════════════════════════════════
    "2c:aa:8e": {"brand": "Wyze Cam", "type": "Indoor Cam v3", "country": "US"},
    "7c:78:b2": {"brand": "Wyze Cam", "type": "Outdoor Cam", "country": "US"},
    "d0:52:a8": {"brand": "Wyze Cam", "type": "Pan Cam", "country": "US"},
    "a8:5b:78": {"brand": "Wyze Cam", "type": "Cam v2", "country": "US"},
    "c4:d7:97": {"brand": "Wyze Cam", "type": "Floodlight", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  REOLINK — China/USA
    # ═══════════════════════════════════════════════════════════
    "ec:71:db": {"brand": "Reolink", "type": "IP Camera", "country": "CN"},
    "dc:44:27": {"brand": "Reolink", "type": "IP Camera", "country": "CN"},
    "14:0a:c5": {"brand": "Reolink", "type": "IP Camera", "country": "CN"},
    "48:70:2d": {"brand": "Reolink", "type": "IP Camera", "country": "CN"},
    "b0:c5:54": {"brand": "Reolink", "type": "IP Camera", "country": "CN"},
    "e4:3a:6e": {"brand": "Reolink", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  AMCREST — USA
    # ═══════════════════════════════════════════════════════════
    "9c:8e:cd": {"brand": "Amcrest", "type": "IP Camera", "country": "US"},
    "00:1e:c0": {"brand": "Amcrest", "type": "IP Camera", "country": "US"},
    "00:18:ae": {"brand": "Amcrest", "type": "IP Camera", "country": "US"},
    "90:15:65": {"brand": "Amcrest", "type": "Doorbell Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  FOSCAM — China
    # ═══════════════════════════════════════════════════════════
    "00:0c:e6": {"brand": "Foscam", "type": "IP Camera", "country": "CN"},
    "c4:2f:56": {"brand": "Foscam", "type": "IP Camera", "country": "CN"},
    "e0:62:90": {"brand": "Foscam", "type": "IP Camera", "country": "CN"},
    "3c:49:37": {"brand": "Foscam", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  EUFY (Anker Innovations) — China/USA
    # ═══════════════════════════════════════════════════════════
    "48:86:e8": {"brand": "Eufy", "type": "Indoor Cam 2K", "country": "CN"},
    "d4:5b:89": {"brand": "Eufy", "type": "HomeBase 2", "country": "CN"},
    "c0:49:ef": {"brand": "Eufy", "type": "Video Doorbell", "country": "CN"},
    "f4:4d:30": {"brand": "Eufy", "type": "Outdoor Cam", "country": "CN"},
    "00:37:ab": {"brand": "Eufy", "type": "SoloCam", "country": "CN"},
    "44:74:5b": {"brand": "Eufy", "type": "Floodlight Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  TP-LINK TAPO — China
    # ═══════════════════════════════════════════════════════════
    "10:27:f5": {"brand": "TP-Link Tapo", "type": "C200 Pan/Tilt", "country": "CN"},
    "14:cc:20": {"brand": "TP-Link Tapo", "type": "C310 Outdoor", "country": "CN"},
    "50:c7:bf": {"brand": "TP-Link Tapo", "type": "C100 Indoor", "country": "CN"},
    "54:af:97": {"brand": "TP-Link Tapo", "type": "C320WS", "country": "CN"},
    "b0:be:76": {"brand": "TP-Link Tapo", "type": "C500 Outdoor", "country": "CN"},
    "90:9a:4a": {"brand": "TP-Link Tapo", "type": "C420S2", "country": "CN"},
    "1c:61:b4": {"brand": "TP-Link Tapo", "type": "C225 Pan/Tilt", "country": "CN"},
    "60:32:b1": {"brand": "TP-Link Tapo", "type": "C110 Indoor", "country": "CN"},
    "ac:15:a2": {"brand": "TP-Link", "type": "Cloud Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  EZVIZ (Hikvision consumer brand) — China
    # ═══════════════════════════════════════════════════════════
    "40:31:3c": {"brand": "Ezviz", "type": "Smart Camera", "country": "CN"},
    "bc:dd:c2": {"brand": "Ezviz", "type": "Outdoor Camera", "country": "CN"},
    "c4:02:05": {"brand": "Ezviz", "type": "Indoor Camera", "country": "CN"},
    "8c:d5:a7": {"brand": "Ezviz", "type": "Doorbell Camera", "country": "CN"},
    "54:c4:e9": {"brand": "Ezviz", "type": "PTZ Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  XIAOMI / MI HOME — China
    # ═══════════════════════════════════════════════════════════
    "78:11:dc": {"brand": "Xiaomi Mi Cam", "type": "Smart Camera 360", "country": "CN"},
    "34:80:b3": {"brand": "Xiaomi Mi Cam", "type": "Home Security Cam", "country": "CN"},
    "58:44:98": {"brand": "Xiaomi Mi Cam", "type": "Outdoor Camera", "country": "CN"},
    "64:09:80": {"brand": "Xiaomi Mi Cam", "type": "Baby Monitor", "country": "CN"},
    "78:02:f8": {"brand": "Xiaomi Mi Cam", "type": "Smart Camera 2K", "country": "CN"},
    "f8:a4:5f": {"brand": "Xiaomi Mi Cam", "type": "Doorbell Camera", "country": "CN"},
    "a4:c1:38": {"brand": "Xiaomi Mi Cam", "type": "Smart Camera", "country": "CN"},
    "14:f6:5a": {"brand": "Xiaomi Mi Cam", "type": "Indoor Camera", "country": "CN"},
    "8c:be:be": {"brand": "Xiaomi", "type": "Smart Camera Pro", "country": "CN"},
    "34:ce:00": {"brand": "Xiaomi Mi Cam", "type": "Outdoor Camera", "country": "CN"},
    "50:8f:4c": {"brand": "Xiaomi Mi Cam", "type": "Smart Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  YI TECHNOLOGY — China/USA
    # ═══════════════════════════════════════════════════════════
    "7c:49:eb": {"brand": "Yi Home Camera", "type": "Indoor Cam", "country": "CN"},
    "78:9c:85": {"brand": "Yi Home Camera", "type": "Outdoor Camera", "country": "CN"},
    "98:5a:eb": {"brand": "Yi Camera", "type": "Dome Camera", "country": "CN"},
    "68:a3:c4": {"brand": "Yi Camera", "type": "1080p Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  BLINK (Amazon) — USA
    # ═══════════════════════════════════════════════════════════
    "44:61:32": {"brand": "Blink", "type": "Outdoor Camera", "country": "US"},
    "74:75:48": {"brand": "Blink", "type": "Indoor Camera", "country": "US"},
    "1c:c5:d6": {"brand": "Blink", "type": "Video Doorbell", "country": "US"},
    "f0:45:da": {"brand": "Blink", "type": "Mini Indoor Cam", "country": "US"},
    "3c:8d:20": {"brand": "Blink", "type": "Outdoor 4 Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  SWANN COMMUNICATIONS — Australia/USA
    # ═══════════════════════════════════════════════════════════
    "00:1e:46": {"brand": "Swann", "type": "IP Camera", "country": "AU"},
    "d4:6e:0e": {"brand": "Swann", "type": "Outdoor Camera", "country": "AU"},
    "70:4f:57": {"brand": "Swann", "type": "Security Camera", "country": "AU"},

    # ═══════════════════════════════════════════════════════════
    #  LOREX (Dahua sub-brand) — Canada/USA
    # ═══════════════════════════════════════════════════════════
    "00:d0:f1": {"brand": "Lorex", "type": "IP Camera", "country": "CA"},
    "00:1e:11": {"brand": "Lorex", "type": "IP Camera", "country": "CA"},
    "98:9b:cb": {"brand": "Lorex", "type": "4K IP Camera", "country": "CA"},
    "2c:8d:b1": {"brand": "Lorex", "type": "Outdoor Camera", "country": "CA"},

    # ═══════════════════════════════════════════════════════════
    #  HANWHA / SAMSUNG TECHWIN (Korea)
    # ═══════════════════════════════════════════════════════════
    "00:09:18": {"brand": "Hanwha Wisenet", "type": "IP Camera", "country": "KR"},
    "00:09:45": {"brand": "Hanwha Wisenet", "type": "IP Camera", "country": "KR"},
    "30:14:4a": {"brand": "Hanwha Wisenet", "type": "PTZ Camera", "country": "KR"},
    "7c:e9:d3": {"brand": "Hanwha Wisenet", "type": "Fisheye Cam", "country": "KR"},
    "84:eb:18": {"brand": "Hanwha Vision", "type": "AI Camera", "country": "KR"},
    "00:0d:f1": {"brand": "Hanwha Techwin", "type": "IP Camera", "country": "KR"},
    "2c:a1:7c": {"brand": "Hanwha", "type": "AI Box Camera", "country": "KR"},

    # ═══════════════════════════════════════════════════════════
    #  VIVOTEK — Taiwan
    # ═══════════════════════════════════════════════════════════
    "00:02:d1": {"brand": "Vivotek", "type": "IP Camera", "country": "TW"},
    "00:66:19": {"brand": "Vivotek", "type": "IP Camera", "country": "TW"},
    "00:69:11": {"brand": "Vivotek", "type": "IP Camera", "country": "TW"},
    "08:82:d4": {"brand": "Vivotek", "type": "Fisheye Camera", "country": "TW"},
    "d0:65:ca": {"brand": "Vivotek", "type": "Speed Dome", "country": "TW"},
    "f8:d5:11": {"brand": "Vivotek", "type": "Outdoor Camera", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  PELCO (USA) — Schneider Electric subsidiary
    # ═══════════════════════════════════════════════════════════
    "00:07:6d": {"brand": "Pelco", "type": "IP Camera", "country": "US"},
    "00:40:1b": {"brand": "Pelco", "type": "IP Camera", "country": "US"},
    "8c:9d:12": {"brand": "Pelco", "type": "Sarix Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  AVIGILON (Motorola Solutions) — Canada
    # ═══════════════════════════════════════════════════════════
    "00:18:85": {"brand": "Avigilon", "type": "H4 Camera", "country": "CA"},
    "e0:1c:41": {"brand": "Avigilon", "type": "H5A Camera", "country": "CA"},
    "ac:a4:1b": {"brand": "Avigilon", "type": "Fisheye Camera", "country": "CA"},
    "ec:a9:40": {"brand": "Avigilon", "type": "Thermal Camera", "country": "CA"},

    # ═══════════════════════════════════════════════════════════
    #  MOBOTIX — Germany
    # ═══════════════════════════════════════════════════════════
    "00:00:12": {"brand": "Mobotix", "type": "Hemispheric Cam", "country": "DE"},
    "e4:60:e8": {"brand": "Mobotix", "type": "M73 Camera", "country": "DE"},
    "d0:8e:79": {"brand": "Mobotix", "type": "Q71 Camera", "country": "DE"},

    # ═══════════════════════════════════════════════════════════
    #  FLIR SYSTEMS — USA
    # ═══════════════════════════════════════════════════════════
    "00:40:7f": {"brand": "FLIR", "type": "Thermal Camera", "country": "US"},
    "d0:4f:7e": {"brand": "FLIR", "type": "IP Camera", "country": "US"},
    "c4:f0:81": {"brand": "FLIR", "type": "Security Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  BOSCH SECURITY — Germany
    # ═══════════════════════════════════════════════════════════
    "00:07:5f": {"brand": "Bosch Security", "type": "Flexidome Cam", "country": "DE"},
    "00:0e:5c": {"brand": "Bosch Security", "type": "Autodome PTZ", "country": "DE"},
    "44:4e:6d": {"brand": "Bosch Security", "type": "IP Camera 5000", "country": "DE"},
    "00:26:7e": {"brand": "Bosch Security", "type": "Dinion Camera", "country": "DE"},

    # ═══════════════════════════════════════════════════════════
    #  D-LINK CAMERAS — Taiwan
    # ═══════════════════════════════════════════════════════════
    "1c:7e:e5": {"brand": "D-Link", "type": "DCS Camera", "country": "TW"},
    "34:08:04": {"brand": "D-Link", "type": "DCS-8302LH", "country": "TW"},
    "f0:7d:68": {"brand": "D-Link", "type": "DCS-8525LH", "country": "TW"},
    "90:f6:52": {"brand": "D-Link", "type": "DCS-2530L", "country": "TW"},
    "00:05:5d": {"brand": "D-Link", "type": "IP Camera", "country": "TW"},
    "c4:a8:1d": {"brand": "D-Link", "type": "DCS Outdoor Cam", "country": "TW"},
    "28:10:7b": {"brand": "D-Link", "type": "DCS-8300LH", "country": "TW"},
    "14:d6:4d": {"brand": "D-Link", "type": "DCS Pan/Tilt", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  UBIQUITI UNIFI PROTECT — USA
    # ═══════════════════════════════════════════════════════════
    "00:27:22": {"brand": "Ubiquiti UniFi", "type": "G4 Dome", "country": "US"},
    "04:18:d6": {"brand": "Ubiquiti UniFi", "type": "G4 Pro", "country": "US"},
    "24:a4:3c": {"brand": "Ubiquiti UniFi", "type": "G4 Bullet", "country": "US"},
    "78:8a:20": {"brand": "Ubiquiti UniFi", "type": "G3 Flex", "country": "US"},
    "f4:92:bf": {"brand": "Ubiquiti UniFi", "type": "G5 Camera", "country": "US"},
    "18:e8:29": {"brand": "Ubiquiti UniFi", "type": "G4 Doorbell", "country": "US"},
    "24:5a:4c": {"brand": "Ubiquiti UniFi", "type": "AI Pro Camera", "country": "US"},
    "70:a7:41": {"brand": "Ubiquiti UniFi", "type": "G4 PTZ", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  UNIVIEW (UNV) — China
    # ═══════════════════════════════════════════════════════════
    "c0:f4:e6": {"brand": "Uniview", "type": "IP Camera", "country": "CN"},
    "e8:48:b8": {"brand": "Uniview", "type": "IP Camera", "country": "CN"},
    "7c:27:e8": {"brand": "Uniview", "type": "PTZ Camera", "country": "CN"},
    "60:cf:84": {"brand": "Uniview", "type": "Outdoor Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  TIANDY — China
    # ═══════════════════════════════════════════════════════════
    "e4:ab:89": {"brand": "Tiandy", "type": "IP Camera", "country": "CN"},
    "f4:4c:7f": {"brand": "Tiandy", "type": "AI Camera", "country": "CN"},
    "04:ab:18": {"brand": "Tiandy", "type": "PTZ Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  IMOU (Dahua consumer brand) — China
    # ═══════════════════════════════════════════════════════════
    "44:80:eb": {"brand": "Imou", "type": "Cue 2 Camera", "country": "CN"},
    "38:a2:8c": {"brand": "Imou", "type": "Cell Pro Cam", "country": "CN"},
    "c8:73:75": {"brand": "Imou", "type": "Outdoor Cam", "country": "CN"},
    "58:d9:d5": {"brand": "Imou", "type": "Ranger Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ANNKE — China
    # ═══════════════════════════════════════════════════════════
    "c8:02:10": {"brand": "Annke", "type": "IP Camera", "country": "CN"},
    "00:1c:c0": {"brand": "Annke", "type": "Security Camera", "country": "CN"},
    "58:ef:68": {"brand": "Annke", "type": "4K Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ZMODO — USA
    # ═══════════════════════════════════════════════════════════
    "ac:d0:74": {"brand": "Zmodo", "type": "IP Camera", "country": "US"},
    "00:e0:f9": {"brand": "Zmodo", "type": "Wi-Fi Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  PANASONIC IP CAMERAS — Japan
    # ═══════════════════════════════════════════════════════════
    "00:80:45": {"brand": "Panasonic", "type": "WV IP Camera", "country": "JP"},
    "00:0d:fd": {"brand": "Panasonic", "type": "WV Dome Cam", "country": "JP"},
    "08:00:6b": {"brand": "Panasonic", "type": "WV PTZ Cam", "country": "JP"},
    "00:a0:de": {"brand": "Panasonic", "type": "WV Outdoor Cam", "country": "JP"},
    "40:ae:30": {"brand": "Panasonic", "type": "WV-SPW Camera", "country": "JP"},
    "0c:72:2c": {"brand": "Panasonic", "type": "WV-X Camera", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  SONY SECURITY CAMERAS — Japan
    # ═══════════════════════════════════════════════════════════
    "00:01:4a": {"brand": "Sony", "type": "SNC IP Camera", "country": "JP"},
    "00:13:a9": {"brand": "Sony", "type": "SNC Dome Cam", "country": "JP"},
    "00:d0:d7": {"brand": "Sony", "type": "SNC Outdoor Cam", "country": "JP"},
    "ac:9b:0a": {"brand": "Sony", "type": "SNC Box Cam", "country": "JP"},
    "00:50:f1": {"brand": "Sony", "type": "SNC PTZ Cam", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  CANON NETWORK CAMERAS — Japan
    # ═══════════════════════════════════════════════════════════
    "00:02:a0": {"brand": "Canon", "type": "VB Network Cam", "country": "JP"},
    "00:21:b7": {"brand": "Canon", "type": "VB-M Dome Cam", "country": "JP"},
    "00:c0:ee": {"brand": "Canon", "type": "VB-H Camera", "country": "JP"},
    "40:1c:83": {"brand": "Canon", "type": "VB-R Camera", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  HONEYWELL — USA
    # ═══════════════════════════════════════════════════════════
    "00:04:2a": {"brand": "Honeywell", "type": "equIP Camera", "country": "US"},
    "00:30:6e": {"brand": "Honeywell", "type": "Performance Cam", "country": "US"},
    "70:b3:17": {"brand": "Honeywell", "type": "EquIP IP Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  GEOVISION — Taiwan
    # ═══════════════════════════════════════════════════════════
    "00:13:e2": {"brand": "GeoVision", "type": "GV-IP Camera", "country": "TW"},
    "00:1a:4b": {"brand": "GeoVision", "type": "GV-UBL Camera", "country": "TW"},
    "00:50:56": {"brand": "GeoVision", "type": "GV-Fisheye", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  MARCH NETWORKS — Canada
    # ═══════════════════════════════════════════════════════════
    "00:0f:bc": {"brand": "March Networks", "type": "IP Camera", "country": "CA"},
    "00:1c:e1": {"brand": "March Networks", "type": "MegaPX Camera", "country": "CA"},

    # ═══════════════════════════════════════════════════════════
    #  INDIGOVISION — UK/Scotland
    # ═══════════════════════════════════════════════════════════
    "00:16:d2": {"brand": "IndigoVision", "type": "9000 IP Camera", "country": "GB"},
    "00:1d:25": {"brand": "IndigoVision", "type": "Ultra Cam", "country": "GB"},

    # ═══════════════════════════════════════════════════════════
    #  ILLUSTRA / TYCO (Johnson Controls) — USA
    # ═══════════════════════════════════════════════════════════
    "00:09:e7": {"brand": "Illustra/Tyco", "type": "Flex Cam", "country": "US"},
    "00:00:09": {"brand": "Tyco Security", "type": "VideoEdge Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  MILESIGHT — China
    # ═══════════════════════════════════════════════════════════
    "e8:eb:1b": {"brand": "Milesight", "type": "AI Camera", "country": "CN"},
    "a4:3e:60": {"brand": "Milesight", "type": "Outdoor Camera", "country": "CN"},
    "d8:47:20": {"brand": "Milesight", "type": "Fisheye Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  TVT DIGITAL — China
    # ═══════════════════════════════════════════════════════════
    "00:1d:c1": {"brand": "TVT Digital", "type": "IP Camera", "country": "CN"},
    "50:bd:5f": {"brand": "TVT Digital", "type": "PTZ Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  CP PLUS — India
    # ═══════════════════════════════════════════════════════════
    "b4:ee:b4": {"brand": "CP Plus", "type": "IP Camera", "country": "IN"},
    "d4:df:9a": {"brand": "CP Plus", "type": "Bullet Camera", "country": "IN"},
    "48:4b:aa": {"brand": "CP Plus", "type": "Dome Camera", "country": "IN"},

    # ═══════════════════════════════════════════════════════════
    #  NOOIE — China/USA
    # ═══════════════════════════════════════════════════════════
    "00:15:61": {"brand": "Nooie", "type": "Indoor Cam 360", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  GUARDZILLA — USA
    # ═══════════════════════════════════════════════════════════
    "b4:43:0d": {"brand": "Guardzilla", "type": "360 Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  CANARY — USA
    # ═══════════════════════════════════════════════════════════
    "e4:f0:42": {"brand": "Canary", "type": "Indoor Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  TENVIS — China
    # ═══════════════════════════════════════════════════════════
    "d8:96:85": {"brand": "Tenvis", "type": "IP Camera", "country": "CN"},
    "00:55:7b": {"brand": "Tenvis", "type": "HD IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  WANSVIEW — China
    # ═══════════════════════════════════════════════════════════
    "dc:0b:34": {"brand": "Wansview", "type": "IP Camera", "country": "CN"},
    "c8:f7:42": {"brand": "Wansview", "type": "W9 Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  VSTARCAM — China
    # ═══════════════════════════════════════════════════════════
    "c4:13:e2": {"brand": "Vstarcam", "type": "IP Camera", "country": "CN"},
    "00:c8:8b": {"brand": "Vstarcam", "type": "Outdoor Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  SRICAM — China
    # ═══════════════════════════════════════════════════════════
    "00:af:1f": {"brand": "Sricam", "type": "SP Series Cam", "country": "CN"},
    "5c:f7:19": {"brand": "Sricam", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  360 SMART CAMERA (Qihoo) — China
    # ═══════════════════════════════════════════════════════════
    "90:c7:d8": {"brand": "360 Smart Camera", "type": "AI Pan/Tilt", "country": "CN"},
    "4c:1a:3d": {"brand": "360 Smart Camera", "type": "Indoor Cam", "country": "CN"},
    "a8:7e:ea": {"brand": "360 Smart Camera", "type": "Outdoor Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  AQARA (Lumi United Technology) — China
    # ═══════════════════════════════════════════════════════════
    "54:ef:44": {"brand": "Aqara Camera", "type": "G3 Hub Camera", "country": "CN"},
    "00:15:8d": {"brand": "Aqara Camera", "type": "E1 Camera", "country": "CN"},
    "28:6d:cd": {"brand": "Aqara Camera", "type": "G2H Pro", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  OWLET — USA
    # ═══════════════════════════════════════════════════════════
    "44:a8:42": {"brand": "Owlet", "type": "Cam 2 Baby Monitor", "country": "US"},
    "e8:db:84": {"brand": "Owlet", "type": "Dream Sock Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  INFANT OPTICS — USA
    # ═══════════════════════════════════════════════════════════
    "f8:f0:05": {"brand": "Infant Optics", "type": "DXR-8 Baby Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  TUYA / SMART LIFE (massive white-label ecosystem) — China
    # ═══════════════════════════════════════════════════════════
    "00:1e:1b": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "20:f4:1b": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "b0:f8:93": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "d8:f1:5b": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "e8:db:84": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "50:02:91": {"brand": "Tuya OEM Camera", "type": "Indoor Camera", "country": "CN"},
    "7c:01:0a": {"brand": "Tuya OEM Camera", "type": "Outdoor Camera", "country": "CN"},
    "d8:96:e0": {"brand": "Tuya OEM Camera", "type": "Doorbell Camera", "country": "CN"},
    "68:57:2d": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "a8:03:2a": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "bc:25:e0": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "18:93:d7": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  NETGEAR CAMERAS — USA
    # ═══════════════════════════════════════════════════════════
    "a0:63:91": {"brand": "Netgear", "type": "VMS Camera", "country": "US"},
    "b0:39:56": {"brand": "Netgear", "type": "Arlo Base Station", "country": "US"},
    "20:e5:2a": {"brand": "Netgear", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  LG INNOTEK — South Korea
    # ═══════════════════════════════════════════════════════════
    "00:e0:91": {"brand": "LG Innotek", "type": "IP Camera", "country": "KR"},
    "cc:4b:73": {"brand": "LG Innotek", "type": "Security Camera", "country": "KR"},

    # ═══════════════════════════════════════════════════════════
    #  PELCO / SCHNEIDER — USA
    # ═══════════════════════════════════════════════════════════
    "00:07:6d": {"brand": "Pelco", "type": "Sarix PTZ", "country": "US"},
    "00:e1:8c": {"brand": "Pelco", "type": "Spectra HD PTZ", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ZOSI — China/USA
    # ═══════════════════════════════════════════════════════════
    "00:18:ae": {"brand": "Zosi", "type": "IP Camera", "country": "CN"},
    "70:3a:cb": {"brand": "Zosi", "type": "4K Camera", "country": "CN"},
    "8c:4b:14": {"brand": "Zosi", "type": "Outdoor Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  SPECO TECHNOLOGIES — USA
    # ═══════════════════════════════════════════════════════════
    "00:1b:a4": {"brand": "Speco", "type": "IP Camera", "country": "US"},
    "00:50:1e": {"brand": "Speco", "type": "Intensifier Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ACTi — Taiwan
    # ═══════════════════════════════════════════════════════════
    "00:1a:07": {"brand": "ACTi", "type": "IP Camera", "country": "TW"},
    "00:d0:93": {"brand": "ACTi", "type": "E Series Camera", "country": "TW"},
    "ac:be:5b": {"brand": "ACTi", "type": "B Series Camera", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  ARECONT VISION — USA (now part of Costar)
    # ═══════════════════════════════════════════════════════════
    "00:1d:7b": {"brand": "Arecont Vision", "type": "Megapixel Camera", "country": "US"},
    "00:26:88": {"brand": "Arecont Vision", "type": "SurroundVideo Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  DIGITAL WATCHDOG — USA
    # ═══════════════════════════════════════════════════════════
    "00:26:48": {"brand": "Digital Watchdog", "type": "MEGApix Camera", "country": "US"},
    "a4:ed:43": {"brand": "Digital Watchdog", "type": "Stellar Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ONCAM / ONCAM GRANDEYE — UK
    # ═══════════════════════════════════════════════════════════
    "00:e0:c8": {"brand": "Oncam", "type": "360° Fisheye Cam", "country": "GB"},

    # ═══════════════════════════════════════════════════════════
    #  IDIS — South Korea
    # ═══════════════════════════════════════════════════════════
    "00:0d:6f": {"brand": "IDIS", "type": "IP Camera", "country": "KR"},
    "d8:d4:3c": {"brand": "IDIS", "type": "DirectIP Camera", "country": "KR"},
    "e4:42:a6": {"brand": "IDIS", "type": "Full HD Camera", "country": "KR"},

    # ═══════════════════════════════════════════════════════════
    #  LILIN (Merit LILIN) — Taiwan
    # ═══════════════════════════════════════════════════════════
    "00:0b:2b": {"brand": "Merit LILIN", "type": "IP Camera", "country": "TW"},
    "00:c0:02": {"brand": "Merit LILIN", "type": "AI Camera", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  HUNT ELECTRONICS — Taiwan
    # ═══════════════════════════════════════════════════════════
    "00:0b:6b": {"brand": "Hunt Electronics", "type": "IP Camera", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  VICON INDUSTRIES — USA
    # ═══════════════════════════════════════════════════════════
    "00:15:f9": {"brand": "Vicon", "type": "V-Series Camera", "country": "US"},
    "00:40:aa": {"brand": "Vicon", "type": "IQmini Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  VIDEOTEC — Italy
    # ═══════════════════════════════════════════════════════════
    "00:30:6f": {"brand": "Videotec", "type": "IP Camera", "country": "IT"},

    # ═══════════════════════════════════════════════════════════
    #  IQinVision (now part of Flir) — USA
    # ═══════════════════════════════════════════════════════════
    "00:1c:f0": {"brand": "IQinVision", "type": "IQeye Camera", "country": "US"},
    "00:0c:03": {"brand": "IQinVision", "type": "IQeye Sentinel", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  SIQURA / GUARDIAN — Netherlands
    # ═══════════════════════════════════════════════════════════
    "00:30:c8": {"brand": "Siqura", "type": "IP Camera", "country": "NL"},

    # ═══════════════════════════════════════════════════════════
    #  LOGI / LOGITECH — Switzerland/USA
    # ═══════════════════════════════════════════════════════════
    "00:04:6b": {"brand": "Logitech", "type": "Circle Camera", "country": "CH"},
    "34:02:86": {"brand": "Logitech", "type": "Circle 2 Camera", "country": "CH"},

    # ═══════════════════════════════════════════════════════════
    #  TEND INSIGHTS / LYNX — USA
    # ═══════════════════════════════════════════════════════════
    "e4:95:6e": {"brand": "Tend Insights", "type": "Lynx Indoor Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ARCHERFISH — USA
    # ═══════════════════════════════════════════════════════════
    "00:0f:a3": {"brand": "Archerfish", "type": "Smart Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  LAVIEW — USA
    # ═══════════════════════════════════════════════════════════
    "00:c2:c6": {"brand": "LaView", "type": "Security Camera", "country": "US"},
    "38:2c:4a": {"brand": "LaView", "type": "One Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  VIVINT — USA
    # ═══════════════════════════════════════════════════════════
    "00:16:b6": {"brand": "Vivint", "type": "Smart Cam", "country": "US"},
    "4c:bc:a5": {"brand": "Vivint", "type": "Indoor Camera", "country": "US"},
    "b4:5d:50": {"brand": "Vivint", "type": "Outdoor Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ADT (USA)
    # ═══════════════════════════════════════════════════════════
    "00:21:f2": {"brand": "ADT", "type": "Pulse Camera", "country": "US"},
    "e0:aa:96": {"brand": "ADT", "type": "Security Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  SIMPLISAFE — USA
    # ═══════════════════════════════════════════════════════════
    "00:24:b2": {"brand": "SimpliSafe", "type": "Outdoor Camera", "country": "US"},
    "7c:b2:7d": {"brand": "SimpliSafe", "type": "Indoor Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ABODE SYSTEMS — USA
    # ═══════════════════════════════════════════════════════════
    "70:b3:d5": {"brand": "Abode", "type": "Indoor Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ALFRED (HOME SECURITY) — USA
    # ═══════════════════════════════════════════════════════════
    "38:bc:1a": {"brand": "Alfred Camera", "type": "Home Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  COHU — USA
    # ═══════════════════════════════════════════════════════════
    "00:90:f3": {"brand": "Cohu", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  SCALLOP IMAGING — USA
    # ═══════════════════════════════════════════════════════════
    "00:30:b8": {"brand": "Scallop Imaging", "type": "Wide Angle Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  SURFSIGHT (Lytx) — USA (dashcams)
    # ═══════════════════════════════════════════════════════════
    "00:1c:7c": {"brand": "Lytx Surfsight", "type": "Dash Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  GENIE ACCESS — UK
    # ═══════════════════════════════════════════════════════════
    "00:22:b0": {"brand": "Genie Access", "type": "IP Camera", "country": "GB"},

    # ═══════════════════════════════════════════════════════════
    #  MESSOA — Taiwan
    # ═══════════════════════════════════════════════════════════
    "00:0c:1c": {"brand": "Messoa", "type": "IP Camera", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  TRENDNET — USA
    # ═══════════════════════════════════════════════════════════
    "00:14:d1": {"brand": "TRENDnet", "type": "TV-IP Camera", "country": "US"},
    "c0:a0:bb": {"brand": "TRENDnet", "type": "TV-IP Outdoor", "country": "US"},
    "00:08:c7": {"brand": "TRENDnet", "type": "TV-IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  DLINK (IP cameras have separate OUI blocks)
    # already listed above - additional ones:
    # ═══════════════════════════════════════════════════════════
    "a4:77:33": {"brand": "D-Link", "type": "DCS Smart Cam", "country": "TW"},
    "cc:b2:55": {"brand": "D-Link", "type": "DCS-6100LH", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  SANNCE — China
    # ═══════════════════════════════════════════════════════════
    "00:18:8b": {"brand": "Sannce", "type": "IP Camera", "country": "CN"},
    "d4:a6:51": {"brand": "Sannce", "type": "1080p IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  JENNOV — China
    # ═══════════════════════════════════════════════════════════
    "30:83:98": {"brand": "Jennov", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  GALAYOU — China
    # ═══════════════════════════════════════════════════════════
    "c8:f7:50": {"brand": "Galayou", "type": "Indoor Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  CTRONICS — China
    # ═══════════════════════════════════════════════════════════
    "1c:87:74": {"brand": "Ctronics", "type": "PTZ Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  HISEEU — China
    # ═══════════════════════════════════════════════════════════
    "70:f0:87": {"brand": "Hiseeu", "type": "IP Camera", "country": "CN"},
    "9c:a5:13": {"brand": "Hiseeu", "type": "4K Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  TOUCAN — USA
    # ═══════════════════════════════════════════════════════════
    "40:a3:6b": {"brand": "Toucan", "type": "Outdoor Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  AMCREST / FOSCAM OEM VARIANTS
    # ═══════════════════════════════════════════════════════════
    "98:d8:63": {"brand": "Amcrest OEM", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  VIMTAG — China
    # ═══════════════════════════════════════════════════════════
    "a8:40:41": {"brand": "Vimtag", "type": "Cloud Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  IGLOOHOME — Singapore
    # ═══════════════════════════════════════════════════════════
    "30:ae:a4": {"brand": "Igloohome", "type": "Smart Cam", "country": "SG"},

    # ═══════════════════════════════════════════════════════════
    #  ZKTECO — China (access control + cameras)
    # ═══════════════════════════════════════════════════════════
    "00:17:61": {"brand": "ZKTeco", "type": "IP Camera", "country": "CN"},
    "c0:7e:bf": {"brand": "ZKTeco", "type": "Face Camera", "country": "CN"},
    "a4:c4:94": {"brand": "ZKTeco", "type": "AI Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  KEDACOM — China
    # ═══════════════════════════════════════════════════════════
    "00:0c:8a": {"brand": "Kedacom", "type": "IP Camera", "country": "CN"},
    "30:b5:c2": {"brand": "Kedacom", "type": "PTZ Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  SUNELL — China
    # ═══════════════════════════════════════════════════════════
    "70:62:b8": {"brand": "Sunell", "type": "AI Camera", "country": "CN"},
    "e0:d5:e9": {"brand": "Sunell", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  TAPO (additional TP-Link blocks)
    # ═══════════════════════════════════════════════════════════
    "18:d6:c7": {"brand": "TP-Link Tapo", "type": "C500 Camera", "country": "CN"},
    "98:25:4a": {"brand": "TP-Link Tapo", "type": "C325WB Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ATHENA SECURITY — USA
    # ═══════════════════════════════════════════════════════════
    "2c:26:17": {"brand": "Athena Security", "type": "AI Threat Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  VERKADA — USA
    # ═══════════════════════════════════════════════════════════
    "b4:fb:e4": {"brand": "Verkada", "type": "Dome Camera", "country": "US"},
    "cc:40:d0": {"brand": "Verkada", "type": "Bullet Camera", "country": "US"},
    "00:3e:e1": {"brand": "Verkada", "type": "Mini Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  RHOMBUS SYSTEMS — USA
    # ═══════════════════════════════════════════════════════════
    "90:61:ae": {"brand": "Rhombus", "type": "R100 Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  EAGLE EYE NETWORKS — USA
    # ═══════════════════════════════════════════════════════════
    "68:72:51": {"brand": "Eagle Eye Networks", "type": "CMVR Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  MOTOROLA SOLUTIONS — USA (CCTV)
    # ═══════════════════════════════════════════════════════════
    "58:ac:78": {"brand": "Motorola", "type": "Focus Cam", "country": "US"},
    "00:e0:70": {"brand": "Motorola", "type": "Security Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  LOREX (additional OUIs)
    # ═══════════════════════════════════════════════════════════
    "e8:f4:08": {"brand": "Lorex", "type": "Fusion IP Camera", "country": "CA"},
    "f4:ab:2a": {"brand": "Lorex", "type": "Smart Outdoor Cam", "country": "CA"},

    # ═══════════════════════════════════════════════════════════
    #  SHARX SECURITY — USA
    # ═══════════════════════════════════════════════════════════
    "00:1a:e8": {"brand": "Sharx Security", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  WISENET (Hanwha consumer line) — Korea
    # ═══════════════════════════════════════════════════════════
    "10:9a:dd": {"brand": "Wisenet", "type": "QNV Dome Cam", "country": "KR"},
    "00:08:40": {"brand": "Wisenet", "type": "XNO Bullet Cam", "country": "KR"},

    # ═══════════════════════════════════════════════════════════
    #  IOIMAGE (Texas Instruments based) — Israel
    # ═══════════════════════════════════════════════════════════
    "00:11:ce": {"brand": "IOimage", "type": "IP Camera", "country": "IL"},

    # ═══════════════════════════════════════════════════════════
    #  DLINK CLOUD cameras (additional)
    # ═══════════════════════════════════════════════════════════
    "b0:c5:54": {"brand": "D-Link", "type": "DCS Wireless Cam", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  INTELLIO — Hungary
    # ═══════════════════════════════════════════════════════════
    "00:26:82": {"brand": "Intellio", "type": "AI Camera", "country": "HU"},

    # ═══════════════════════════════════════════════════════════
    #  SMARTEC (Russia/Europe)
    # ═══════════════════════════════════════════════════════════
    "f4:ec:38": {"brand": "Smartec", "type": "IP Camera", "country": "RU"},

    # ═══════════════════════════════════════════════════════════
    #  DALI TECHNOLOGY — China
    # ═══════════════════════════════════════════════════════════
    "f4:f9:51": {"brand": "DALI Technology", "type": "Thermal+Optical Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  INFIRAY / IRay Technology — China (thermal cameras)
    # ═══════════════════════════════════════════════════════════
    "7c:b0:c2": {"brand": "InfiRay", "type": "Thermal Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  PROVISION-ISR — Israel
    # ═══════════════════════════════════════════════════════════
    "00:30:19": {"brand": "Provision-ISR", "type": "IP Camera", "country": "IL"},
    "00:1a:4b": {"brand": "Provision-ISR", "type": "S-Series Camera", "country": "IL"},

    # ═══════════════════════════════════════════════════════════
    #  YOOSEE / GOOWLS — China
    # ═══════════════════════════════════════════════════════════
    "e4:00:7f": {"brand": "Yoosee Camera", "type": "Indoor Cam", "country": "CN"},
    "c4:5b:be": {"brand": "Yoosee Camera", "type": "Outdoor Cam", "country": "CN"},
    "60:77:71": {"brand": "Yoosee Camera", "type": "Pan/Tilt Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ICATCH / SONIX TECHNOLOGY (camera chipmakers)
    # ═══════════════════════════════════════════════════════════
    "00:19:69": {"brand": "iCatch OEM Cam", "type": "IP Camera", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  PELCO Endura (NVR/IP cameras)
    # ═══════════════════════════════════════════════════════════
    "00:e1:8c": {"brand": "Pelco Endura", "type": "IP Dome Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  GRANDSTREAM — USA/China
    # ═══════════════════════════════════════════════════════════
    "00:0b:82": {"brand": "Grandstream", "type": "GXV IP Camera", "country": "US"},
    "c0:74:ad": {"brand": "Grandstream", "type": "GDS Doorbell Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  DAHUA TECHNOLOGY (sub-brands and OEM)
    # ═══════════════════════════════════════════════════════════
    "68:ce:4e": {"brand": "Dahua OEM", "type": "IP Camera", "country": "CN"},
    "40:2c:f4": {"brand": "Dahua OEM", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  AJAX SYSTEMS — Ukraine
    # ═══════════════════════════════════════════════════════════
    "f0:7c:32": {"brand": "Ajax Systems", "type": "Outdoor Cam", "country": "UA"},
    "ac:e8:7b": {"brand": "Ajax Systems", "type": "DomeCam Mini", "country": "UA"},

    # ═══════════════════════════════════════════════════════════
    #  LONGSE — China
    # ═══════════════════════════════════════════════════════════
    "48:da:35": {"brand": "Longse", "type": "IP Camera", "country": "CN"},
    "a4:18:75": {"brand": "Longse", "type": "Starlight Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  JOVISION — China
    # ═══════════════════════════════════════════════════════════
    "98:82:d3": {"brand": "Jovision", "type": "IP Camera", "country": "CN"},
    "c8:18:56": {"brand": "Jovision", "type": "Smart Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  HIBIRD (Hikvision OEM) — China
    # ═══════════════════════════════════════════════════════════
    "e4:b3:18": {"brand": "Hibird", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  SAFIRE (Hikvision European line)
    # ═══════════════════════════════════════════════════════════
    "9c:8e:94": {"brand": "Safire", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  TURBO HD (Hikvision product line)
    # ═══════════════════════════════════════════════════════════
    "c0:56:27": {"brand": "Turbo HD Cam", "type": "Analog+IP Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  IC REALTIME — USA
    # ═══════════════════════════════════════════════════════════
    "00:30:f8": {"brand": "IC Realtime", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  HIMAX / HIK OEM — China
    # ═══════════════════════════════════════════════════════════
    "80:1f:02": {"brand": "Himax Camera", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  LIQTECH (door phones/cameras) — China
    # ═══════════════════════════════════════════════════════════
    "d0:17:c2": {"brand": "Liqtech", "type": "Video Door Phone", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  HIKVISION MINEW (OEM) — China
    # ═══════════════════════════════════════════════════════════
    "ac:cf:23": {"brand": "Hikvision OEM", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  QUBO (Hero Group) — India
    # ═══════════════════════════════════════════════════════════
    "b4:75:0e": {"brand": "Qubo", "type": "Smart Cam 360", "country": "IN"},

    # ═══════════════════════════════════════════════════════════
    #  GODREJ SECURITY — India
    # ═══════════════════════════════════════════════════════════
    "60:45:bd": {"brand": "Godrej Security", "type": "IP Camera", "country": "IN"},

    # ═══════════════════════════════════════════════════════════
    #  I-PRO (formerly Panasonic i-PRO) — Japan
    # ═══════════════════════════════════════════════════════════
    "00:80:f0": {"brand": "i-PRO (Panasonic)", "type": "WV X-Series Cam", "country": "JP"},
    "30:e1:71": {"brand": "i-PRO", "type": "AI Camera", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  DAHUA LECHANGE / IMOU (additional)
    # ═══════════════════════════════════════════════════════════
    "e4:f3:f5": {"brand": "Imou Dahua", "type": "Bullet Lite Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  HIKVISION DEEPINVIEW — China (AI cameras)
    # ═══════════════════════════════════════════════════════════
    "2c:f0:a2": {"brand": "Hikvision DeepinView", "type": "AI Facial Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  DHUA TIOC (Two-in-One Camera) — China
    # ═══════════════════════════════════════════════════════════
    "a0:aa:af": {"brand": "Dahua TIOC", "type": "Full-Color Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  VIGI (TP-Link business line) — China
    # ═══════════════════════════════════════════════════════════
    "38:94:ed": {"brand": "TP-Link VIGI", "type": "C540 Bullet Cam", "country": "CN"},
    "60:e3:27": {"brand": "TP-Link VIGI", "type": "C340 Dome Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  WANSVIEW (additional OUIs)
    # ═══════════════════════════════════════════════════════════
    "b0:72:bf": {"brand": "Wansview", "type": "W6 Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  EDIMAX — Taiwan
    # ═══════════════════════════════════════════════════════════
    "00:19:3b": {"brand": "Edimax", "type": "IC IP Camera", "country": "TW"},
    "00:1f:1f": {"brand": "Edimax", "type": "IC Outdoor Cam", "country": "TW"},
    "74:da:38": {"brand": "Edimax", "type": "IC-7113W Camera", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  SERCOMM — Taiwan (makes cameras for various brands)
    # ═══════════════════════════════════════════════════════════
    "00:0c:e5": {"brand": "Sercomm OEM Cam", "type": "IP Camera", "country": "TW"},
    "8c:89:a5": {"brand": "Sercomm OEM Cam", "type": "Smart Camera", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  AMBARELLA (chip vendor — cameras built on their SoC)
    # ═══════════════════════════════════════════════════════════
    "70:81:05": {"brand": "Ambarella-based Cam", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  INGENIC SEMICONDUCTOR (chip vendor) — China
    # ═══════════════════════════════════════════════════════════
    "78:9a:18": {"brand": "Ingenic-based Cam", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  VARIFOCAL CAMERAS / ALHUA OEM — China
    # ═══════════════════════════════════════════════════════════
    "14:c1:4e": {"brand": "Alhua OEM Cam", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  NIPPON ELECTRIC (NEC) CAMERAS — Japan
    # ═══════════════════════════════════════════════════════════
    "00:14:22": {"brand": "NEC IP Camera", "type": "SV Series Cam", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  BASLER — Germany (machine vision / security)
    # ═══════════════════════════════════════════════════════════
    "00:30:53": {"brand": "Basler", "type": "IP Camera", "country": "DE"},

    # ═══════════════════════════════════════════════════════════
    #  IHAWK — USA
    # ═══════════════════════════════════════════════════════════
    "00:18:71": {"brand": "iHawk", "type": "Overhead Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  HIC — China (rebranded/OEM)
    # ═══════════════════════════════════════════════════════════
    "00:1e:4f": {"brand": "HIC Camera", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  SECO-LARM — USA
    # ═══════════════════════════════════════════════════════════
    "00:0f:e9": {"brand": "Seco-Larm", "type": "Enforcer IP Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ERNITEC — Finland
    # ═══════════════════════════════════════════════════════════
    "00:0e:40": {"brand": "Ernitec", "type": "IP Camera", "country": "FI"},

    # ═══════════════════════════════════════════════════════════
    #  HUNT/DVTel — USA
    # ═══════════════════════════════════════════════════════════
    "00:90:e8": {"brand": "DVTel", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  COSTAR VIDEO SYSTEMS — USA
    # ═══════════════════════════════════════════════════════════
    "00:0f:06": {"brand": "Costar Video", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ADDITIONAL TUYA/SMART LIFE OEM CAMERAS — China
    # ═══════════════════════════════════════════════════════════
    "7c:87:ce": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "e4:53:c3": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "6c:b2:ae": {"brand": "Tuya OEM Camera", "type": "Indoor Camera", "country": "CN"},
    "f8:34:41": {"brand": "Tuya OEM Camera", "type": "Outdoor Camera", "country": "CN"},
    "cc:50:e3": {"brand": "Tuya OEM Camera", "type": "Pan/Tilt Camera", "country": "CN"},
    "28:6d:97": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "18:b9:05": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},
    "24:0a:c4": {"brand": "Tuya OEM Camera", "type": "Outdoor Camera", "country": "CN"},
    "40:a3:cc": {"brand": "Tuya OEM Camera", "type": "Smart Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ADDITIONAL HIKVISION OEM/VARIANTS — China
    # ═══════════════════════════════════════════════════════════
    "00:40:48": {"brand": "Hikvision OEM", "type": "IP Camera", "country": "CN"},
    "3c:13:c2": {"brand": "Hikvision OEM", "type": "IP Camera", "country": "CN"},
    "44:51:0e": {"brand": "Hikvision OEM", "type": "IP Camera", "country": "CN"},
    "7c:1e:b3": {"brand": "Hikvision OEM", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ISENTRY — Australia
    # ═══════════════════════════════════════════════════════════
    "a0:a3:b3": {"brand": "iSentry", "type": "IP Camera", "country": "AU"},

    # ═══════════════════════════════════════════════════════════
    #  ICONNECT / IQCAMERAS — various
    # ═══════════════════════════════════════════════════════════
    "00:22:a7": {"brand": "iConnect Camera", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  SV3C — China
    # ═══════════════════════════════════════════════════════════
    "48:27:e2": {"brand": "SV3C", "type": "PoE IP Camera", "country": "CN"},
    "f0:de:f1": {"brand": "SV3C", "type": "1080p Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ULTRA SECURE — UK
    # ═══════════════════════════════════════════════════════════
    "00:30:c4": {"brand": "Ultra Secure", "type": "IP Camera", "country": "GB"},

    # ═══════════════════════════════════════════════════════════
    #  IEGEEK — China
    # ═══════════════════════════════════════════════════════════
    "78:72:57": {"brand": "ieGeek", "type": "Solar IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  TECKIN — China
    # ═══════════════════════════════════════════════════════════
    "30:ae:7b": {"brand": "Teckin", "type": "Smart Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  TAOKKIM — China
    # ═══════════════════════════════════════════════════════════
    "5c:02:14": {"brand": "Taokkim", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  HIKVISION ADDITIONAL SUB-OUIs
    # ═══════════════════════════════════════════════════════════
    "58:a0:23": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "24:28:fd": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "f0:6c:f7": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "10:c3:7b": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "d0:1c:12": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},
    "18:68:cb": {"brand": "Hikvision", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  DAHUA ADDITIONAL SUB-OUIs
    # ═══════════════════════════════════════════════════════════
    "5c:35:3b": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "28:57:be": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "f8:a2:d6": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "b4:04:39": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},
    "74:75:48": {"brand": "Dahua", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ZMODO ADDITIONAL
    # ═══════════════════════════════════════════════════════════
    "d0:94:66": {"brand": "Zmodo/Meshare", "type": "Smart Camera", "country": "US"},
    "c4:45:67": {"brand": "Zmodo", "type": "Outdoor Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  DIGITUS — Germany
    # ═══════════════════════════════════════════════════════════
    "00:0c:43": {"brand": "Digitus", "type": "DN IP Camera", "country": "DE"},

    # ═══════════════════════════════════════════════════════════
    #  LEVEL ONE — Taiwan
    # ═══════════════════════════════════════════════════════════
    "00:d0:59": {"brand": "LevelOne", "type": "FCS IP Camera", "country": "TW"},
    "00:11:6b": {"brand": "LevelOne", "type": "FCS Dome Cam", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  INSTAR — Germany
    # ═══════════════════════════════════════════════════════════
    "48:51:63": {"brand": "Instar", "type": "IN IP Camera", "country": "DE"},
    "b8:27:eb": {"brand": "Instar", "type": "Outdoor Camera", "country": "DE"},

    # ═══════════════════════════════════════════════════════════
    #  INDEXA — Germany
    # ═══════════════════════════════════════════════════════════
    "c4:6e:1f": {"brand": "Indexa", "type": "Smart Camera", "country": "DE"},

    # ═══════════════════════════════════════════════════════════
    #  DERICAM — China
    # ═══════════════════════════════════════════════════════════
    "ac:ab:a1": {"brand": "Dericam", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ESCAM — China
    # ═══════════════════════════════════════════════════════════
    "3c:e8:24": {"brand": "Escam", "type": "QD IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  REOLINK (additional OUIs)
    # ═══════════════════════════════════════════════════════════
    "8c:9c:02": {"brand": "Reolink", "type": "RLC IP Camera", "country": "CN"},
    "54:eb:71": {"brand": "Reolink", "type": "RLC-820A", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  HIKVISION THERMOGRAPHIC CAMERAS
    # ═══════════════════════════════════════════════════════════
    "34:40:b6": {"brand": "Hikvision Thermal", "type": "Thermographic Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  MOBOTIX (additional)
    # ═══════════════════════════════════════════════════════════
    "00:50:c2": {"brand": "Mobotix", "type": "S73 Camera", "country": "DE"},

    # ═══════════════════════════════════════════════════════════
    #  DEDICATED MICROS / INFINOVA — UK/USA
    # ═══════════════════════════════════════════════════════════
    "00:1d:72": {"brand": "Infinova", "type": "V Series Cam", "country": "US"},
    "00:60:e0": {"brand": "Dedicated Micros", "type": "IP Camera", "country": "GB"},

    # ═══════════════════════════════════════════════════════════
    #  W-BOX (Orion Technologies / OEM)
    # ═══════════════════════════════════════════════════════════
    "00:8c:fa": {"brand": "W-Box", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  LUMA SURVEILLANCE — USA
    # ═══════════════════════════════════════════════════════════
    "4c:bc:98": {"brand": "Luma Surveillance", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  REVO AMERICA — USA
    # ═══════════════════════════════════════════════════════════
    "00:9a:cd": {"brand": "Revo America", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  OPTIVIEW (USA)
    # ═══════════════════════════════════════════════════════════
    "00:1b:e5": {"brand": "Optiview", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  CAMIUS — USA/China
    # ═══════════════════════════════════════════════════════════
    "c8:d1:b6": {"brand": "Camius", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  Q-SEE (QUOVADIS) — USA
    # ═══════════════════════════════════════════════════════════
    "00:23:24": {"brand": "Q-See", "type": "IP Camera", "country": "US"},
    "e0:40:07": {"brand": "Q-See", "type": "QCN Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  BTICINO (Legrand) — Italy
    # ═══════════════════════════════════════════════════════════
    "00:13:71": {"brand": "BTicino", "type": "Videodoor Cam", "country": "IT"},

    # ═══════════════════════════════════════════════════════════
    #  COME TECH — China
    # ═══════════════════════════════════════════════════════════
    "a4:70:d6": {"brand": "Cometech", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  SIQURA (IndigoVision rebrand) — Netherlands
    # ═══════════════════════════════════════════════════════════
    "14:e4:a3": {"brand": "Siqura", "type": "HD Camera", "country": "NL"},

    # ═══════════════════════════════════════════════════════════
    #  GUARDIAN MICROELECTRONICS — India
    # ═══════════════════════════════════════════════════════════
    "48:8a:d2": {"brand": "Guardian", "type": "IP Camera", "country": "IN"},

    # ═══════════════════════════════════════════════════════════
    #  CONCORD — various
    # ═══════════════════════════════════════════════════════════
    "60:d0:2c": {"brand": "Concord", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  MAPESEN — China
    # ═══════════════════════════════════════════════════════════
    "38:02:3c": {"brand": "Mapesen", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  EMINENT — Netherlands
    # ═══════════════════════════════════════════════════════════
    "00:25:4b": {"brand": "Eminent", "type": "EM IP Camera", "country": "NL"},

    # ═══════════════════════════════════════════════════════════
    #  ORNO — Poland
    # ═══════════════════════════════════════════════════════════
    "14:29:d7": {"brand": "Orno", "type": "IP Camera", "country": "PL"},

    # ═══════════════════════════════════════════════════════════
    #  XIAOVV — China
    # ═══════════════════════════════════════════════════════════
    "00:f6:63": {"brand": "Xiaovv", "type": "1080p IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  TP-LINK ADDITIONAL IP CAMERAS
    # ═══════════════════════════════════════════════════════════
    "e8:de:27": {"brand": "TP-Link Camera", "type": "Wireless Cam", "country": "CN"},
    "94:d9:b3": {"brand": "TP-Link Camera", "type": "Outdoor Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ABUS — Germany
    # ═══════════════════════════════════════════════════════════
    "00:90:a9": {"brand": "ABUS", "type": "IP Camera", "country": "DE"},
    "3c:95:09": {"brand": "ABUS", "type": "TVIP Camera", "country": "DE"},

    # ═══════════════════════════════════════════════════════════
    #  OPTEX — Japan
    # ═══════════════════════════════════════════════════════════
    "00:0b:3a": {"brand": "Optex", "type": "IP Camera", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  SANYO SECURITY — Japan
    # ═══════════════════════════════════════════════════════════
    "00:01:e3": {"brand": "Sanyo", "type": "VCC IP Camera", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  FUJITSU GENERAL — Japan
    # ═══════════════════════════════════════════════════════════
    "00:17:42": {"brand": "Fujitsu", "type": "IP Camera", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  TOSHIBA NETWORK CAMERAS — Japan
    # ═══════════════════════════════════════════════════════════
    "00:07:0d": {"brand": "Toshiba", "type": "IK-WP IP Cam", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  HITACHI KOKUSAI ELECTRIC — Japan
    # ═══════════════════════════════════════════════════════════
    "00:0e:1a": {"brand": "Hitachi Kokusai", "type": "IP Camera", "country": "JP"},

    # ═══════════════════════════════════════════════════════════
    #  COMPRO TECHNOLOGY — Taiwan
    # ═══════════════════════════════════════════════════════════
    "00:e0:11": {"brand": "Compro", "type": "TN IP Camera", "country": "TW"},

    # ═══════════════════════════════════════════════════════════
    #  MICRODIGITAL — South Korea
    # ═══════════════════════════════════════════════════════════
    "00:0a:92": {"brand": "Microdigital", "type": "MDC IP Camera", "country": "KR"},

    # ═══════════════════════════════════════════════════════════
    #  VDEO SECURITY — USA
    # ═══════════════════════════════════════════════════════════
    "d4:68:4d": {"brand": "Vdeo Security", "type": "IP Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  EBITCAM — China
    # ═══════════════════════════════════════════════════════════
    "d8:1c:a5": {"brand": "Ebitcam", "type": "E3 IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  PANACAST (Jabra) — Denmark
    # ═══════════════════════════════════════════════════════════
    "50:c2:e8": {"brand": "Jabra PanaCast", "type": "Video Conferencing", "country": "DK"},

    # ═══════════════════════════════════════════════════════════
    #  TELTONIKA — Lithuania
    # ═══════════════════════════════════════════════════════════
    "00:1e:42": {"brand": "Teltonika", "type": "IP Camera", "country": "LT"},

    # ═══════════════════════════════════════════════════════════
    #  NETIO — Czech Republic
    # ═══════════════════════════════════════════════════════════
    "00:22:66": {"brand": "Netio", "type": "IP Camera", "country": "CZ"},

    # ═══════════════════════════════════════════════════════════
    #  HANWHA AEROSPACE (different from Hanwha Vision)
    # ═══════════════════════════════════════════════════════════
    "18:26:49": {"brand": "Hanwha Aerospace", "type": "AI Security Cam", "country": "KR"},

    # ═══════════════════════════════════════════════════════════
    #  WISENET ADDITIONAL
    # ═══════════════════════════════════════════════════════════
    "64:a8:3c": {"brand": "Wisenet AI Camera", "type": "P-Series Cam", "country": "KR"},

    # ═══════════════════════════════════════════════════════════
    #  SHEN ZHEN RICH VIDEO — China
    # ═══════════════════════════════════════════════════════════
    "a4:58:0f": {"brand": "Rich Video Cam", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  RICHER-R / GENERIC BUDGET — China
    # ═══════════════════════════════════════════════════════════
    "20:0d:b0": {"brand": "Budget IP Camera", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  CAM CLOUD PLATFORMS (OEM)
    # ═══════════════════════════════════════════════════════════
    "d0:39:72": {"brand": "Cloud Camera OEM", "type": "Smart Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  ADDITIONAL RING / BLINK OUIs (Amazon)
    # ═══════════════════════════════════════════════════════════
    "f4:f5:d8": {"brand": "Amazon Ring", "type": "Ring Pro 2", "country": "US"},
    "40:b4:cd": {"brand": "Amazon Blink", "type": "Blink Outdoor Cam", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  ADC (Alarm.com) — USA
    # ═══════════════════════════════════════════════════════════
    "70:d8:23": {"brand": "Alarm.com", "type": "ADC Camera", "country": "US"},
    "00:1d:d9": {"brand": "Alarm.com", "type": "Smart Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  DEEP SENTINEL — USA
    # ═══════════════════════════════════════════════════════════
    "d4:8a:fc": {"brand": "Deep Sentinel", "type": "AI Guard Camera", "country": "US"},

    # ═══════════════════════════════════════════════════════════
    #  SOLIOM — China/USA
    # ═══════════════════════════════════════════════════════════
    "a4:c3:f0": {"brand": "Soliom", "type": "Solar Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  WUUK — China/USA
    # ═══════════════════════════════════════════════════════════
    "f8:b5:68": {"brand": "WUUK", "type": "Smart Cam", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  AKASO — China
    # ═══════════════════════════════════════════════════════════
    "8c:f7:c7": {"brand": "Akaso", "type": "IP Camera", "country": "CN"},

    # ═══════════════════════════════════════════════════════════
    #  HERSMAY — China
    # ═══════════════════════════════════════════════════════════
    "50:ec:50": {"brand": "Hersmay", "type": "IP Camera", "country": "CN"},
}


def lookup_camera(bssid: str):
    """
    Check if a BSSID belongs to a known camera manufacturer.
    Returns dict with brand, type, country or None if not a camera.
    """
    if not bssid or len(bssid) < 8:
        return None
    oui = bssid[:8].lower()
    return CAMERA_OUI_DB.get(oui)


def get_camera_count():
    return len(CAMERA_OUI_DB)

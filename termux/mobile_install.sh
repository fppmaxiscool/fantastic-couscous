#!/bin/bash
# CIVOPS-Radar: Mobile Installation Script
# Author: CIVOPS-Radar Contributors
# License: MIT
#
# This script installs CIVOPS-Radar on Android devices via Termux

# NOTE: Do NOT use set -euo pipefail here — optional steps would kill the whole install

# Configuration
RADAR_DIR="$HOME/radar"
GITHUB_REPO="https://github.com/fppmaxiscool/fantastic-couscous.git"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

log()     { echo -e "[$(date '+%H:%M:%S')] $1"; }
success() { log "${GREEN}✓ $1${NC}"; }
warning() { log "${YELLOW}⚠ $1${NC}"; }
info()    { log "${BLUE}ℹ $1${NC}"; }
error()   { log "${RED}✗ $1${NC}"; }
progress(){ log "${PURPLE}$1${NC}"; }

# ─── Step 1: Update packages ────────────────────────────────────────────────
progress "[10%] Updating Termux package list..."
pkg update -y 2>/dev/null || warning "pkg update had warnings (continuing)"
success "Package list updated"

# ─── Step 2: Install system packages ────────────────────────────────────────
progress "[20%] Installing required system packages..."

PACKAGES="python python-pip sqlite git curl wget"
for pkg_name in $PACKAGES; do
    info "Installing $pkg_name..."
    pkg install -y "$pkg_name" 2>/dev/null || warning "Could not install $pkg_name (continuing)"
done

# termux-api is optional (required for Wi-Fi scanning but not for web interface)
info "Installing termux-api (optional, needed for Wi-Fi scanning)..."
pkg install -y termux-api 2>/dev/null || warning "termux-api not installed — Wi-Fi scanning won't work but web UI will"

success "System packages done"

# ─── Step 3: Clone repository ───────────────────────────────────────────────
progress "[40%] Downloading CIVOPS-Radar code from GitHub..."

if [ -d "$RADAR_DIR" ]; then
    info "Found existing installation at $RADAR_DIR — updating..."
    cd "$RADAR_DIR" && git pull origin main 2>/dev/null || {
        warning "Git pull failed — doing fresh install"
        cd "$HOME"
        rm -rf "$RADAR_DIR"
        git clone "$GITHUB_REPO" "$RADAR_DIR" || { error "Failed to clone repository. Check internet connection."; exit 1; }
    }
else
    git clone "$GITHUB_REPO" "$RADAR_DIR" || { error "Failed to clone repository. Check internet connection."; exit 1; }
fi

success "Code downloaded"

# ─── Step 4: Install Python packages ────────────────────────────────────────
progress "[60%] Installing Python packages..."

cd "$RADAR_DIR"
export PIP_BREAK_SYSTEM_PACKAGES=1

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt 2>/dev/null || {
        warning "requirements.txt install failed — trying individual packages"
        pip install flask flask-cors requests beautifulsoup4 2>/dev/null || \
            warning "Some Python packages failed to install"
    }
else
    pip install flask flask-cors requests beautifulsoup4 2>/dev/null || \
        warning "Some Python packages failed to install"
fi

success "Python packages done"

# ─── Step 5: Set up directories and database ────────────────────────────────
progress "[75%] Setting up directories and database..."

cd "$RADAR_DIR"
mkdir -p data/exports data/samples server/templates server/static

# Initialize database directly with sqlite3 (no dependency on radar_prototype.sh)
sqlite3 data/scans.db "
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
);
CREATE INDEX IF NOT EXISTS idx_bssid ON scans(bssid);
CREATE INDEX IF NOT EXISTS idx_timestamp ON scans(timestamp);
" 2>/dev/null && success "Database ready" || warning "Database setup had issues (will be created on first run)"

success "Directories ready"

# ─── Step 6: Create startup scripts ─────────────────────────────────────────
progress "[90%] Creating startup shortcuts..."

cd "$RADAR_DIR"

cat > start_mobile.sh << 'STARTEOF'
#!/bin/bash
# CIVOPS-Radar — Full Launcher
cd "$HOME/radar"

echo ""
echo "  ██████╗██╗██╗   ██╗ ██████╗ ██████╗ ███████╗"
echo "  ██╔════╝██║██║   ██║██╔═══██╗██╔══██╗██╔════╝"
echo "  ██║     ██║██║   ██║██║   ██║██████╔╝███████╗"
echo "  ██║     ██║╚██╗ ██╔╝██║   ██║██╔═══╝ ╚════██║"
echo "  ╚██████╗██║ ╚████╔╝ ╚██████╔╝██║     ███████║"
echo "   ╚═════╝╚═╝  ╚═══╝   ╚═════╝ ╚═╝     ╚══════╝"
echo "         R A D A R  //  SIGINT  SYSTEM"
echo ""

# 1. Pull latest code
echo "[1/4] Pulling latest code..."
git pull origin main --quiet 2>/dev/null && echo "      ✓ Up to date" || echo "      ⚠ Could not update (offline?)"

# 2. Install/verify Python deps
echo "[2/4] Checking Python dependencies..."
export PIP_BREAK_SYSTEM_PACKAGES=1
pip install flask flask-cors requests beautifulsoup4 -q 2>/dev/null && echo "      ✓ Dependencies OK" || echo "      ⚠ Some deps missing"

# 3. Start scanner (only if termux-api works)
echo "[3/4] Starting Wi-Fi scanner..."
if command -v termux-wifi-scaninfo &>/dev/null; then
    # Test if it actually responds
    timeout 4 termux-wifi-scaninfo &>/dev/null
    if [ $? -eq 0 ]; then
        bash termux/radar_prototype.sh scan &>/dev/null &
        echo "      ✓ Real scanner ACTIVE — scanning nearby networks"
    else
        echo "      ⚠ termux-api installed but not responding"
        echo "        → Grant Location permission in Android Settings > Apps > Termux"
        echo "        → Showing DEMO data in radar"
    fi
else
    echo "      ⚠ Termux:API not found → Install from F-Droid for real networks"
    echo "        → Showing DEMO data in radar"
fi

# 4. Start web server
echo "[4/4] Starting web server..."
sleep 1
python server/app.py --host 0.0.0.0 --port 5000 &>/dev/null &
sleep 1
echo "      ✓ Server started"

echo ""
echo "  ┌─────────────────────────────────────────┐"
echo "  │  Open your browser and go to:           │"
echo "  │                                         │"
echo "  │     http://localhost:5000               │"
echo "  │                                         │"
echo "  │  Press Ctrl+C to stop everything        │"
echo "  └─────────────────────────────────────────┘"
echo ""

trap 'echo ""; echo "Stopping CIVOPS-Radar..."; kill $(jobs -p) 2>/dev/null; exit 0' INT
wait
STARTEOF
chmod +x start_mobile.sh

cat > quick_start.sh << 'QSEOF'
#!/bin/bash
cd "$HOME/radar"
echo "🚀 CIVOPS-Radar Quick Start"
echo "Open browser to: http://localhost:5000"
echo "Press Ctrl+C to stop"
export PIP_BREAK_SYSTEM_PACKAGES=1
python server/app.py --host 0.0.0.0 --port 5000
QSEOF
chmod +x quick_start.sh

cat > update_radar.sh << 'UPDATEEOF'
#!/bin/bash
cd "$HOME/radar"
echo "🔄 Updating CIVOPS-Radar..."
git pull origin main
export PIP_BREAK_SYSTEM_PACKAGES=1
pip install -r requirements.txt 2>/dev/null
echo "✅ Done! Run ./start_mobile.sh to restart."
UPDATEEOF
chmod +x update_radar.sh

success "Startup scripts created"

# ─── Request storage permissions (non-blocking) ─────────────────────────────
progress "[95%] Requesting storage permissions (a dialog may appear)..."
termux-setup-storage 2>/dev/null &
sleep 1

# ─── Done ───────────────────────────────────────────────────────────────────
progress "[100%] ✅ Installation complete!"

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   CIVOPS-Radar installed successfully!   ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════╝${NC}"
echo ""
echo -e "  📁 Location:  $RADAR_DIR"
echo -e "  🌐 URL:        http://localhost:5000"
echo ""
echo -e "  ${YELLOW}To start the radar:${NC}"
echo -e "    cd ~/radar"
echo -e "    ./start_mobile.sh"
echo ""
echo -e "  ${YELLOW}Or just the web UI (no scanner):${NC}"
echo -e "    cd ~/radar"
echo -e "    ./quick_start.sh"
echo ""

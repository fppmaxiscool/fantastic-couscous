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

# Fix permissions
chmod +x termux/*.sh 2>/dev/null

# 1. Pull latest code
echo "[1/4] Pulling latest code..."
git pull origin main --quiet 2>/dev/null && echo "      OK" || echo "      Could not update (offline?)"

# 2. Install/verify Python deps
echo "[2/4] Checking Python dependencies..."
export PIP_BREAK_SYSTEM_PACKAGES=1
pip install flask flask-cors requests beautifulsoup4 -q 2>/dev/null && echo "      OK" || echo "      Some deps missing"

# 3. Start scanner (only if termux-api works)
echo "[3/4] Starting Wi-Fi scanner..."
if command -v termux-wifi-scaninfo &>/dev/null; then
    timeout 4 termux-wifi-scaninfo &>/dev/null
    if [ $? -eq 0 ]; then
        bash termux/radar_prototype.sh scan &>/dev/null &
        echo "      REAL scanner ACTIVE"
    else
        echo "      termux-api not responding"
        echo "      -> Grant Location permission: Android Settings > Apps > Termux > Permissions"
    fi
else
    echo "      Termux:API not installed"
    echo "      -> Install from F-Droid: https://f-droid.org/packages/com.termux.api/"
fi

# 4. Start web server
echo "[4/4] Starting web server..."
sleep 1
python server/app.py --host 0.0.0.0 --port 5000 &>/dev/null &
sleep 1
echo "      OK"

echo ""
echo "  ┌─────────────────────────────────────────┐"
echo "  │  Open browser to: http://localhost:5000  │"
echo "  │  Press Ctrl+C to stop                   │"
echo "  └─────────────────────────────────────────┘"
echo ""

trap 'echo "Stopping..."; kill $(jobs -p) 2>/dev/null; exit 0' INT
wait

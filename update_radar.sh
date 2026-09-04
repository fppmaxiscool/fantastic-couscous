#!/bin/bash
# CIVOPS-Radar — Update Script
cd "$HOME/radar"
echo "Updating CIVOPS-Radar..."
git pull origin main
chmod +x termux/*.sh start_mobile.sh update_radar.sh 2>/dev/null
export PIP_BREAK_SYSTEM_PACKAGES=1
pip install -r requirements.txt -q 2>/dev/null
echo "Done! Run ./start_mobile.sh to start."

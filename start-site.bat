@echo off
title RSI Panel - Local Server
cd /d "%USERPROFILE%\Desktop\RSI"
echo RSI Panel acilir: http://127.0.0.1:8000
echo Baglamaq ucun bu pencereni bagla.
python -m http.server 8000
pause

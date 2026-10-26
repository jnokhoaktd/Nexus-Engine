@echo off
cd /d D:\nghien-cuu-ck
set HF_HUB_CACHE=D:\hf-cache
start "" /min cmd /c "timeout /t 6 >nul & start http://127.0.0.1:8000"
.\.venv\Scripts\python.exe .\laya-main\examples\server.py --no-preload --device cpu
pause

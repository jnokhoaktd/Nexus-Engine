@echo off
start /b "" "D:\nghien-cuu-ck\.venv\Scripts\python.exe" "D:\nghien-cuu-ck\nexus-main\examples\server.py"
timeout /t 5 /nobreak >nul
start http://127.0.0.1:8000/nexus
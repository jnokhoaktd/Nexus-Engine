@echo off
echo Dang khoi chay Nexus Engine Local Server...
start /b "" "D:\nghien-cuu-ck\.venv\Scripts\python.exe" "D:\nghien-cuu-ck\nexus-main\examples\server.py"
timeout /t 3 /nobreak >nul
start http://127.0.0.1:8000/nexus
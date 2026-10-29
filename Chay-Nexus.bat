@echo off
:: 1. Chay Python FastAPI Server ngam
start /b "" "D:\nghien-cuu-ck\.venv\Scripts\python.exe" "D:\nghien-cuu-ck\nexus-main\examples\server.py"

:: 2. Cho 5 giay de AI Model nap xong va mo cong 8000
timeout /t 5 /nobreak >nul

:: 3. Mo trinh duyet Web UI Nexus Giao dien Sang
start http://127.0.0.1:8000/nexus
@echo off
cd /d "C:\Users\Dell\My_portfolio_10"
"C:\Users\Dell\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload > "C:\Users\Dell\My_portfolio_10\server-out.log" 2> "C:\Users\Dell\My_portfolio_10\server-err.log"

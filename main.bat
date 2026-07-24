@echo off
python main.py
if %errorlevel% neq 0 (
    python3 main.py
)
pause
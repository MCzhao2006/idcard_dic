#!/bin/bash
if command -v python3 >/dev/null 2>&1; then
    python3 main.py
else
    python main.py
fi
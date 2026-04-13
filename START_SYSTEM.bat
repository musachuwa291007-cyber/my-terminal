@echo off
title Iron Cross Terminal Launcher

:: Start the Svelte Dashboard
start cmd /k "cd /d %~dp0\ICC_DASHBOARD && npm run dev"

:: Start the Python Engine
start cmd /k "cd /d %~dp0\ICC_ENGINE && python engine.py"

echo Iron Cross Systems Engaged.
pause
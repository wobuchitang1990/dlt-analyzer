@echo off
chcp 65001 >nul
title 大乐透智能分析投注助手

cd /d "%~dp0"

:: 检查 Python
where python >nul 2>&1
if %errorlevel% equ 0 (
    python server.py
    goto :end
)

:: 没有 Python
echo.
echo   ⚠ 未检测到 Python
echo   💡 安装方法：打开命令行运行 winget install python
echo   📂 或使用 Firefox 浏览器直接打开 index.html
echo.
start "" "%~dp0index.html"
pause

:end

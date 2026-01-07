#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import time
from pathlib import Path

try:
    import keyboard
except ImportError:
    print("'keyboard' нема")
    print("!pip install keyboard")
    sys.exit(1)

from s import open_firefox_with_urls, URLS

def on_hotkey_pressed():
    """Win+O"""
    print(f"[{time.strftime('%H:%M:%S')}]")
    open_firefox_with_urls(URLS)

def main():
    print("zero condition Daemon")
    print("start: Win + O")
    print("exit: Ctrl+C")

    
    # Регистрируем горячую клавишу Super+O
    # На Windows Win клавиша = 'win'
    try:
        keyboard.add_hotkey('win+o', on_hotkey_pressed)
        print("Super button")
        print(" Нажмите Win+O для запуска Firefox\n")
    except Exception as e:
        print(f"✗: {e}")
        print("нужна админка")
        sys.exit(1)
    
    # Держим скрипт запущенным
    try:
        keyboard.wait()  # Блокирует выполнение до нажатия Ctrl+C
    except KeyboardInterrupt:
        print("\n\n✗ Daemon остановлен")
        sys.exit(0)

if __name__ == "__main__":
    # Проверяем права администратора (рекомендуется для глобальных горячих клавиш)
    if os.name == 'nt':  # Windows
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if not is_admin:
                print("⚠ ")
                print("рекомендуется запускать скрипт от имени администратора")
                print("(правый клик -> Запуск от имени администратора)\n")
        except:
            pass

    #TODO:докастомить переносом функционала из Linux
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import time
from pathlib import Path

try:
    import keyboard
except ImportError:
    print("✗ Ошибка: библиотека 'keyboard' не установлена")
    print("  Установите её командой: pip install keyboard")
    sys.exit(1)

from s import open_firefox_with_urls, URLS

def on_hotkey_pressed():
    """Обработчик нажатия горячей клавиши Win+O"""
    print(f"[{time.strftime('%H:%M:%S')}] Горячая клавиша Win+O нажата - запуск Firefox...")
    open_firefox_with_urls(URLS)

def main():

    print("zero condition Daemon")

    print("start: Win + O")
    print("exit: Ctrl+C")

    
    # Регистрируем горячую клавишу Win+O
    # На Windows Win клавиша = 'windows' или 'win'
    try:
        keyboard.add_hotkey('win+o', on_hotkey_pressed)
        print("✓ Горячая клавиша зарегистрирована")
        print("  Нажмите Win+O для запуска Firefox\n")
    except Exception as e:
        print(f"✗ Ошибка при регистрации горячей клавиши: {e}")
        print("  Возможно, нужны права администратора")
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
    
    main()


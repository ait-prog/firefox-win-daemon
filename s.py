#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для запуска Firefox с набором ссылок
"""

import subprocess
import sys
import os

# Список URL для открытия
URLS = [
    "https://www.kaggle.com/",
    "https://music.yandex.kz/playlists/fea3c86d-2953-7929-a27f-26407ebf442a",
    "https://github.com/ait-prog?tab=repositories"
]

def find_firefox_path():
    """Находит путь к Firefox на Windows"""
    possible_paths = [
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
        os.path.expanduser(r"~\AppData\Local\Mozilla Firefox\firefox.exe"),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    # Если не найден, пробуем через PATH
    return "firefox"

def open_firefox_with_urls(urls):
    """Запускает Firefox с указанными URL"""
    firefox_path = find_firefox_path()
    
    try:
        # Запускаем Firefox с несколькими URL (каждый URL откроется в новой вкладке)
        cmd = [firefox_path] + urls
        subprocess.Popen(cmd, shell=False)
        print(f"✓ Firefox запущен с {len(urls)} вкладками")
        return True
    except FileNotFoundError:
        print(f"✗ Ошибка: Firefox не найден по пути {firefox_path}")
        print("  Убедитесь, что Firefox установлен или добавьте его в PATH")
        return False
    except Exception as e:
        print(f"✗ Ошибка при запуске Firefox: {e}")
        return False

if __name__ == "__main__":
    open_firefox_with_urls(URLS)


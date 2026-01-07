#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для запуска Firefox с набором ссылок
"""

import subprocess
import sys
import os

# Список URL пополняйте по надобности
URLS = [
    "https://www.kaggle.com/",
    "https://apotify.com",
    "https://github.com"
]

def find_firefox_path():
    """path"""
    possible_paths = [
        r"C:\",
        r"C:\",
        os.path.expanduser(r"~\AppData\Local\..."),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    # Если не найден, пробуем через PATH
    return "firefox"

def open_firefox_with_urls(urls):
    firefox_path = find_firefox_path()
    
    try:
        cmd = [firefox_path] + urls
        subprocess.Popen(cmd, shell=False)
        print(f"✓ Firefox  {len(urls)}")
        return True
    except FileNotFoundError:
        print(f"✗  {firefox_path}")
        print("  Убедитесь, что Firefox установлен")
        return False
    except Exception as e:
        print(f"✗ {e}")
        return False

if __name__ == "__main__":
    open_firefox_with_urls(URLS)



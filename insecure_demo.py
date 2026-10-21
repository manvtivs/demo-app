import hashlib
import pickle
import random
import sqlite3
import subprocess
import requests
import yaml
import hmac
import secrets
import os

DB_PASSWORD = os.getenv("DB_PASSWORD") # извлечение пароля из переменных окружения

def get_user(username):
 conn = sqlite3.connect("app.db")
 query = "SELECT * FROM users WHERE name = ?" # использование параметризованного запроса
 return conn.execute(query, (username,)).fetchall()

def ping(host):
 # передача аргументов в виде списка строк и отключение shell=True
 return subprocess.run(["ping", "-c", "1", host], shell=False)

def hash_password(password):
 # использование криптографически стойкой хэш-функции SHA-256
 return hashlib.sha256(password.encode()).hexdigest()

def make_reset_token():
 return secrets.token_hex(16) # использование криптографически стойкого CSPRNG

def load_config(text):
 return yaml.safe_load(text) # использование безопасного метода загрузки YAML

def load_session(data):
 # в реальных условиях вместо pickle лучше использовать безопасный JSON
 import json
 return json.loads(data)

def fetch(url):
 return requests.get(url, verify=True) # проверка TLS включена

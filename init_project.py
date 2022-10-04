import os
import sys
from sys import stdout
os.system("")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def initialize_python_modules():
    os.chdir(BASE_DIR)
    os.system("pip install -r requirements.txt")

def initialize_npm_modules():
    path_ = os.path.join(BASE_DIR, "UmfrageApp/static")
    os.chdir(path_)
    os.system("npm install")


def initialize_databases():
    os.chdir(BASE_DIR)
    os.system("py manage.py makemigrations")
    os.system("py manage.py migrate")


if __name__ == '__main__':
    initialize_python_modules()
    initialize_npm_modules()
    initialize_databases()
    print("\033[95m Setup complete.\033[0m") #\033[0m \033[F \033[K",end="\r"


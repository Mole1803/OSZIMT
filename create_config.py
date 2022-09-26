import os


def create_environment():
    os.system("pip freeze > requirements.txt")


if __name__ == '__main__':
    create_environment()

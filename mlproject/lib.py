# mlproject/lib.py

def hello_world():
    return "Hello world from mlproject"

def try_me():
    print('Dis camion')
    camion = input().lower()
    if camion == 'camion':
        print('pouet pouet')
        return
    else:
        try_me()
        return
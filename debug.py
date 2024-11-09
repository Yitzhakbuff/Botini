import os


def title():
    with open('banner.txt', 'r', encoding='utf-8') as banner:
        c = 124
        for line in banner:
            c+=1
            print(f"\x1b[38;5;{c}m{line}", end='')
        print("\x1b[38;5;129mmadeby: laruga \x1b[37m\n", end='')
def clear():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")

def info(text):
    print(f"\x1b[37m[\x1b[38;5;44mINFO\x1b[37m]\x1b[38;5;130m {text}")
def error(text):
    print(f"\x1b[37m[\x1b[31mERRO\x1b[37m]\x1b[38;5;130m {text}")
def prompt(text):
    return input(f"\x1b[37m[\x1b[38;5;34m/\x1b[37m]\x1b[38;5;130m {text}")
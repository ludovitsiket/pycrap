import subprocess
import sys


def pings(addr, num):
    i = 0
    while i < num:
        x = subprocess.check_output(["ping", "-c", "1", addr])
        print(x)
        i = i+1


def syntax():
    print('Syntax: python3 pycrap.py <ADDRESS> <number_of_pings>')


def main():
    try:
        ip = sys.argv[1]
        num = int(sys.argv[2])
        pings(ip, num)
    except (IndexError, ValueError) as e:
        print(e)
        syntax()


main()

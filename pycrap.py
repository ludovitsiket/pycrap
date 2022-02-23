import subprocess
import sys


def pings(addr, num):
    i = 0
    while i < num:
        print(subprocess.check_output(["ping", "-c", "1", addr]))
        i = i+1


def syntax():
    print('Syntax: python3 pycrap.py <number_of_pings>')
    print('ip.txt contain address for ping')


def count_lines(file_name):
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def read_urls(some_file, number, result):
    i = 0
    with open(some_file, 'r') as f:
        while i < number:
            value = f.readline().replace('\n', '')
            result.append(value)
            i += 1
    return result


def address(addr):
    i = 0
    address = read_urls(addr, count_lines(addr), [])
    return address[i]


def main():
    try:
        pings(address('ip.txt'), int(sys.argv[1]))
    except (IndexError, ValueError, subprocess.CalledProcessError) as e:
        print(e)
        syntax()


main()

from tools import keygen
from tools import server
import sys


def start(port=None):
    if not port:
        port = 8080

    server.start(port)

def key_s(num=None):
    if not num:
        num = 1
    keygen.main(num)

def main():
    argv = sys.argv
    port = None
    num = None
    for par in argv:
        if par == '--start':
            if len(argv) == 2:
                start()
            if len(argv) == 3:
                port = argv[argv.index('--start') +1]
                start(port)
        if par == '--keygen':
            if len(argv) == 2:
                key_s()
            if len(argv) == 3:
                num = argv[argv.index('--keygen') +1]
                key_s(num)



if __name__ ==  '__main__':
    main()


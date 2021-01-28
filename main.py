import time, logging, argparse, start, setup

parser = argparse.ArgumentParser(prog='airmon', usage='%(prog)s [start] [setup] [-h]')
parser.add_argument('command', choices=['start', 'setup'])
args = parser.parse_args()

if args.command == 'start':
    start.main()
elif args.command == 'setup':
    setup.main()
else:
    parser.print_help()

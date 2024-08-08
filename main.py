import threading 
import argparse
from queue import Queue
import subprocess
from colorama import init

# from colorama - https://pypi.org/project/colorama/
init()  

# Instantiate the parser
parser = argparse.ArgumentParser(description='JubJub : some sort of network swiss army knife')

# print help screen
parser.add_argument('--sweep', action='store_true',
                    help='Runs a ping sweep')


# define a lock that we can use later to keep
# prints from writing over itself
# main.pprint_lock = threading.Lock()
import http.client
import config
import json
import subprocess
from termcolor import colored

def colored_by_ratio(text, ratio, thres=[0.5, 0.999999]):
    if ratio < thres[0]:
        clr = 'green'
    elif ratio < thres[1]:
        clr = 'yellow'
    # elif ratio < thres[2]:
        # clr = 'orange'
    else:
        clr = 'red'
    return colored(text, clr)

def thres_red(text, val, thres=1):
    if val < thres:
        return colored(text, 'red')
    else:
        return colored(text, 'white')

def run_cmd(args):
    if isinstance(args, str):
        args = args.split()
    p = subprocess.run(args, stdout=subprocess.PIPE, check=True)
    return p.stdout.decode().strip()

def uniq(arr):
    # ref: https://mail.python.org/pipermail/python-dev/2017-December/151283.html
    return list(dict.fromkeys(arr))

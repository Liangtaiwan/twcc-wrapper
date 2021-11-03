import re
import subprocess
from subprocess import PIPE


def get_nodes():
    p = subprocess.run(['sinfo', '-Nho', '%N'], stdout=PIPE)
    if p.returncode != 0:
        raise ValueError('sinfo failed!')
    return p.stdout.decode().strip().split('\n')


def get_partitions():
    p = subprocess.run(['sinfo', '-ho', '%R'], stdout=PIPE)
    if p.returncode != 0:
        raise ValueError('sinfo failed!')
    return p.stdout.decode().strip().split('\n')


def get_qos_settings():
    p = subprocess.run(
        ['sacctmgr', '-Pn', 'list', 'qos', 'normal', 'Format=MaxTRESPA'],
        stdout=PIPE
    )
    if p.returncode != 0:
        raise ValueError('sacctmgr failed!')
    max_billing_per_account = p.stdout.decode().strip()
    if len(max_billing_per_account) == 0:
        max_billing_per_account = 'UNLIMITED'

    p = subprocess.run(
        ['sacctmgr', '-Pn', 'list', 'qos', 'spot', 'Format=UsageFactor'],
        stdout=PIPE
    )
    if p.returncode != 0:
        raise ValueError('sacctmgr failed!')
    spot_billing_ratio = float(p.stdout.decode().strip())

    return max_billing_per_account, spot_billing_ratio


def get_priority_max_age():
    p = subprocess.run(
        ['scontrol', 'show', 'config'],
        stdout=PIPE
    )
    if p.returncode != 0:
        raise ValueError('scontrol failed!')
    regex = re.compile(r'PriorityMaxAge\s+=\s+(\d+)-(\d+):(\d+):(\d+)')
    for line in p.stdout.decode().split('\n'):
        match = regex.fullmatch(line)
        if match is not None:
            sec = 0
            for x, p in zip(match.groups(), (1, 24, 60, 60)):
                sec = sec * p + int(x)
            return sec


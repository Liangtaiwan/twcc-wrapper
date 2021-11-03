import getpass
import http.client
from urllib.parse import urlencode
import os
import json
import slurm


cpu_min = 1
cpu_max = 1024
mem_min = 0.1
mem_max = 1024
gpu_max = 8
#TODO: Need to customize the following
partitions = ['gp1d','gp2d', 'gp4d', 'express', 'gtest']
age_factor_max_seconds = slurm.get_priority_max_age()
# too slow
# max_billing_per_account, spot_billing_ratio = slurm.get_qos_settings()
max_billing_per_account = 'UNLIMITED'
spot_billing_ratio = 0.2

cookie = None


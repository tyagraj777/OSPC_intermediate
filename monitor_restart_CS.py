#Purpose: Monitor instances and restart those in an ERROR state.

import os
import subprocess

os.system("source ~/openstack_credentials.sh")

instances = subprocess.check_output("openstack server list -f value -c ID -c Status", shell=True).decode('utf-8').splitlines()
for line in instances:
    instance_id, status = line.split()
    if status == "ERROR":
        print(f"Restarting instance: {instance_id}")
        os.system(f"openstack server reboot {instance_id}")

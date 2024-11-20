#Purpose: Configure a load balancer and attach instances dynamically.

import os
import subprocess

os.system("source ~/openstack_credentials.sh")

# Create load balancer
lb_id = subprocess.check_output("openstack loadbalancer create --vip-subnet-id <SUBNET_ID> -f value -c id", shell=True).strip().decode('utf-8')

# Add members
instances = subprocess.check_output("openstack server list -f value -c Networks -c ID", shell=True).decode('utf-8').splitlines()
for line in instances:
    instance_id, network = line.split()
    ip = network.split('=')[1]
    os.system(f"openstack loadbalancer member create --subnet-id <SUBNET_ID> --address {ip} --protocol-port 80 {lb_id}")
    print(f"Added instance {instance_id} with IP {ip} to load balancer.")

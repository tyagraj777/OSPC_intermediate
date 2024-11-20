#Purpose: Scale up or down instances based on CPU usage.

#!/bin/bash

source ~/openstack_credentials.sh

threshold=80
cpu_usage=$(openstack hypervisor stats show -f value -c vcpus_used)

if [[ $cpu_usage -gt $threshold ]]; then
  echo "Scaling up: Launching a new instance..."
  openstack server create --image <IMAGE> --flavor <FLAVOR> --network <NETWORK> scale-up-instance
else
  echo "CPU usage within limits."
fi

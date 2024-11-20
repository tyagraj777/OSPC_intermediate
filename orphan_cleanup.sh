#Purpose: Identify and delete unused instances, volumes, and networks.

#!/bin/bash

source ~/openstack_credentials.sh

echo "Cleaning up orphaned resources..."

# Delete instances in SHUTOFF state
for id in $(openstack server list --status SHUTOFF -f value -c ID); do
  echo "Deleting instance $id..."
  openstack server delete $id
done

# Delete unused volumes
for vol in $(openstack volume list --status available -f value -c ID); do
  echo "Deleting volume $vol..."
  openstack volume delete $vol
done

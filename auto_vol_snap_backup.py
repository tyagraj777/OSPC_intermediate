#Purpose: Create volume snapshots and export them for backup.

import os
import subprocess

os.system("source ~/openstack_credentials.sh")

volumes = subprocess.check_output("openstack volume list -f value -c ID", shell=True).decode('utf-8').splitlines()
for volume_id in volumes:
    snapshot_name = f"{volume_id}_snapshot"
    print(f"Creating snapshot for volume {volume_id}")
    os.system(f"openstack volume snapshot create --volume {volume_id} {snapshot_name}")

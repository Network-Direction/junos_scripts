
'''
'SW' is the 'Software Utility' class
This is used for upgrades, file copies, reboots, etc
'''

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import RpcError
from datetime import datetime


USER = 'admin'
PASS = 'GalacticPower!1'
HOST = '10.36.20.15'

# Create a datetime object, representing the time to reboot
# Format this in juniper time
junos_time = datetime(year=2023, month=2, day=14, hour=3, minute=0)
junos_format = junos_time.strftime("%y%m%d%H%M")

print("Connecting...")
try:
    with Device(host=HOST, user=USER, passwd=PASS) as dev:
        sw = SW(dev)
        # print(sw.reboot(in_min=30))
        print(sw.reboot(at=junos_format))
except ConnectError as err:
    print(f"There has been a connection error: {err}")
except RpcError as err:
    if 'another shutdown is running' in str(err):
        print("Unable to reboot, another reboot/shutdown has been scheduled")
    else:
        print(f"RPC Error has occurred: {err}")
except Exception as err:
    print(f"Error was: {err}")

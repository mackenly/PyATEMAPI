# Filename: scratch.py
# Created By: Mackenly Jones on 07/13/2022
# Web: mackenly.com
# Twitter: @mackenlyjones
import PyATEMMax

switcher = PyATEMMax.ATEMMax()
switcher.ping("127.0.0.1")
alive = switcher.waitForConnection()
print(f'Connected: {alive}')
print(switcher.topology.dVEs)
switcher.disconnect()

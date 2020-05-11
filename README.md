# ABB_export_limit
Fork of aurorapy by Claudio Catterina https://code.energievalsabbia.it/ccatterina/aurorapy/tree/master/aurorapy

Requirements:

"flake8" = "*"
pylint = "*"
mock = "*"

pyserial = "==3.2.1"
future = "==0.16.0"
six = "*"

Added power limiting feature, service mode enable and generation of service mode password from serial number request.

Please use with caution, do not modify the service mode requests as poking around with registers here could damage your inverter.

Tested on ABB Power One 3.6 OUTD PV inverter.

#!/usr/bin/env python3
#Python script to run Operating System, Hardware and Platform information.

import platform

print('**************Beginning of the script*************')

print('Python Version: ', platform.python_version())
print('System        :', platform.system())
print('Node          :', platform.node())
print('Release       :', platform.release())
print('Version       :', platform.version())
print('Machine       :', platform.machine())
print('Processor     :', platform.processor())

print('**************End of the script*******************')

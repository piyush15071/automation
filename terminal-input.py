import os
from subprocess import Popen, PIPE

p = os.popen("ls","r")

while(True):
	line = (p.readline()).strip()
	if not line: break
	print(line)
import os
import re

dir_name = 'apps_installation'
directory = os.listdir(dir_name)

files = [file for file in directory if file.startswith('installation')]
for file in files:
	os.remove(os.path.join(dir_name, file))
	



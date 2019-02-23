import re
import datetime

date = datetime.datetime.now().strftime('%d-%m-%y')

history_1 = open("/var/log/apt/history.log.1", 'r')
history_2 = open("/var/log/apt/history.log", 'r')
install = open((f'/home/dean/Documents/python_files/apps_installation/installation_file{date}.txt'),'w')

finds = re.findall("apt install.*", (history_1.read()))
finds += re.findall("apt install.*", (history_2.read()))

for i in range(len(finds)):
	finds[i] = (f'sudo {finds[i]}') 
	install.write(finds[i]+'\n')


import os
import subprocess
import time

def recall() :

	print('recall func')
	
	checkMongod1 = subprocess.check_output("pgrep -lf \"mongod -f /tmp/run_replica/rs01-conf/mongod01.conf\" | wc -l", shell=True)
	checkMongod2 = subprocess.check_output("pgrep -lf \"mongod -f /tmp/run_replica/rs01-conf/mongod02.conf\" | wc -l", shell=True)
	checkMongod3 = subprocess.check_output("pgrep -lf \"mongod -f /tmp/run_replica/rs01-conf/mongod03.conf\" | wc -l", shell=True)

	while True :
		if int(checkMongod1) <= 1:
			subprocess.run(['mongod', '-f', '/tmp/run_replica/rs01-conf/mongod01.conf'])
			time.sleep(10)
			subprocess.run(['mongo', '-port','37018','<', 'mongodb-agent-shard01-rep.js'])

		elif int(checkMongod2) <= 1:
			subprocess.run(['mongod', '-f', '/tmp/run_replica/rs01-conf/mongod02.conf'])
			time.sleep(10)
			subprocess.run(['mongo', '-port','37018','<', 'mongodb-agent-shard01-rep.js'])

		elif int(checkMongod3) <= 1:
			subprocess.run(['mongod', '-f', '/tmp/run_replica/rs01-conf/mongod03.conf'])
			time.sleep(10)
			subprocess.run(['mongo', '-port','37018','<', 'mongodb-agent-shard01-rep.js'])

		else:
			print('check')
			time.sleep(3)

	checkMongod1 = subprocess.check_output("pgrep -lf \"mongod -f /tmp/run_replica/rs01-conf/mongod01.conf\" | wc -l", shell=True)
	checkMongod2 = subprocess.check_output("pgrep -lf \"mongod -f /tmp/run_replica/rs01-conf/mongod02.conf\" | wc -l", shell=True)
	checkMongod3 = subprocess.check_output("pgrep -lf \"mongod -f /tmp/run_replica/rs01-conf/mongod03.conf\" | wc -l", shell=True)


def kill() :

	os.system('kill -9 a.out')
	
	print('kill func')





while True :
	kill()
	recall()




import os
import subprocess

checkProc = subprocess.check_output("pgrep -lf ssh | wc -l", shell=True)
checkProc2 = subprocess.check_output("ps -ef | grep ssh", shell=True)
checkMongodb = subprocess.check_output("ps -ef | grep \"mongod -f /tmp/run_replica/rs01-conf/mongod01.conf\"", shell=True)

print 'checkProc : ', checkProc
print 'checkProc2 : ', checkProc2
print 'checkMongodb: ', checkMongodb

if int(checkProc) == 0:
	print 'no process'

else:
	print 'check process'



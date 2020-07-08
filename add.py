import subprocess, urllib2, sys, time, threading
# Created by Kaden for ASN Scrape
if len(sys.argv) < 2:
    print "\033[37mUsage: python "+sys.argv[0]+" ASN List \033[37m"
    sys.exit()

def run(cmd):
    subprocess.call(cmd, shell=True)

run('ulimit -n 999999')
run('chmod 777 scraper')
print("Running! This might take a little bit!")
asns = open(sys.argv[1], "r")
line = asns.readline()
while line:
    run('./scraper ' + line)
    line = asns.readline()
asns.close()


#Made by Leaned#0969
prefix = 'ip rule add blackhole iif eth0 from '

with open('ranges.lst', 'r') as src:
    with open('abh.txt', 'w') as dest:
       dest.write("#Leaned Auto Range Drop\n")
       for line in src:
           dest.write('%s%s\n' % (prefix, line.rstrip('\n')))
       dest.write("#Lenaed Auto Range Drop\n")

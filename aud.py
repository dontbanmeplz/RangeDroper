#Made by Leaned#0969
prefix = 'sudo ufw deny from '

with open('ranges.lst', 'r') as src:
    with open('ufw.txt', 'w') as dest:
       dest.write("#Lenaed Auto Range Drop\n")
       for line in src:
           dest.write('%s%s\n' % (prefix, line.rstrip('\n')))
       dest.write("#Lenaed Auto Range Drop\n")

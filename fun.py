import re

with open("REV-1.TXT") as f:
    ch = int(input("ENTER YOUR choice: \n1: select \n2: RAM \n"))
    c = open("command.txt",'w')
    while f.readline():
        line = f.readline()
        if ch==1:
            if line.startswith('SQL> SELECT'):
                    line = line.replace("SQL> ",'')
                    c.write(line)
                    print(line)

        elif ch==2:
            if line.startswith('SQL> REM'):
                line = line.replace("SQL> ",'')
                c.write(line)
                print(line)
    c.close()
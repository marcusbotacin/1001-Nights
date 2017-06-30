# Marcus Botacin
# Tool to desobfuscate a simple obfuscation
# Ex: "var f = (700-650,650-650,710-650..."
# This tool is part of the "1001 nights" paper

import sys  # args
import re   # regex

# open file
f=open(sys.argv[1],"r")
# for each line
for line in f:
    # empty string
    clear=[]
    # get all comma-separated values between ()s
    m=re.search(r'\((.*)\)',line.strip()).group().split(",")
    # for each one of these
    for entry in m:
        # remove the () in case of double ones
        e=entry.replace("(","").replace(")","").strip()
        # split with and without whitespace (each time a distinct approach)
        ops=e.split(" - ")
        ops2=e.split("-")
        # check which one is correct
        if len(ops2)>len(ops):
            ops=ops2
        # ignore fake statements
        ops[1]=ops[1].split(";")[0]
        # compute the ord() value and thus convert to char()
        char=chr(int(ops[0])-int(ops[1]))
        # add as a string character
        clear.append(char)
    # On this case, only the first line was obfuscated
    # thus print the string
    print(''.join(clear))
    # and quit
    sys.exit(0)

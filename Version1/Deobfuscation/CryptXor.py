# Marcus Botacin
# XOR-based deobfuscation tool
# This tool is part of the "1001 nights" paper

import sys  # args

# deobfuscatio nfunction (string,key)
def CryptXor(StringUse,Password):
    # empty string
    retstr=""
    # for each char
    for i in xrange(1,len(StringUse)+1):
        # string char
        c_use=StringUse[i-1]
        # key char
        c_pwd=Password[i % len(Password)]
        # xor-ing
        retstr=retstr+chr(ord(c_use) ^ ord(c_pwd))
    # final string
    return retstr

# Get values
_str=sys.argv[1]
_pwd=sys.argv[2]
# deobfuscate
_ret=CryptXor(_str,_pwd)
# print
print(_str,_pwd,_ret)

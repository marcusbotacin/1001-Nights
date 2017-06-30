# Marcus Botacin
# tool to deobfuscate some JS code
# This tool is part of the "1001 nights" paper

import sys  # args

# deobfuscation function
def dec(z):
    u=269863 # magic numbers found in the code
    for q in xrange(0,len(z)):
            i=u*(q+118)+(u%39272)
            f=u*(q+177)+(u%44074)
            # modular math
            r = i % len(z)
            j = f % len(z)
            # swap
            y = z[r]
            z[r]=z[j]
            z[j]=y
            u=(i+f) % 4206333
    return z

# print the substring, since remaining values make no sense
print(''.join(dec(list(sys.argv[1]))[:11]))

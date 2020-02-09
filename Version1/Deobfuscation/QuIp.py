# Marcus Botacin
# A random string generator found on many samples
# You can use it to recover the generate strings
# Thit tool is part of the "1001 nights" paper

import random    # random number generation

# function
def func():
    # empty string
    _str=""
    # for each char until a given length
    while len(_str)<8:
        # random number
        L=int((122-1+1)*random.random()+1)
        # check if it is on a given range (char/ascii range, in this case)
        if((L>=48 and L<=57) or (L>=65 and L<=90) or (L>=97 and L<=122)):
            # append
            _str=_str+chr(L)
    # final string
    print(_str+".")

# call function
# you may also want to import it as a module
func()

import os
import sys


def __std_input__():
    "Return None normally"
    length = len(sys.argv)
    if length > 1:
        for i in range(1,length):
            if os.path.exists(i) and os.path.isfile(i):
                file_name = os.path.split(i)[1] # (foo1,foo2)<-Tuple[1]
                with open(i) as f:
                    for line in f:
                        print(line)
                        return None
            else:
                return 'wrong path'
    else:
        return 'Missing Parameters'

__std_input__()
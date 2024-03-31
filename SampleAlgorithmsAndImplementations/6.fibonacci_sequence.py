"""FIBONACCI SEQUENCE"""

def fun(num):
    lst = []
    fst = -1
    snd = +1
    for i in range(num):
        trd = fst + snd
        lst.append(trd)
        fst = snd
        snd = trd
    return lst

if __name__ == '__main__':
    n = int(input("Enter number for generate fibonacci sequence: "))
    print(fun(n))
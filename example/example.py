
# coding: utf-8

from benchmark_func as bf

def main():
    print(bf.__all__)
    test = bf.Zakharov(10)
    test.plot()

if __name__ == '__main__':
    main()


# coding : utf-8

from opteval.benchmark_func import *
import opteval.benchmark_func as bf

def main():
    print('Available function list is \n', bf.__all__)
    print('One arguments function list is \n', bf.__oneArgument__)
    print('Two arguments function list is \n', bf.__twoArgument__)
    print('Three arguments function list is \n', bf.__threeArgument__)
    for func_name in bf.__oneArgument__:
        instance = eval(func_name)()
        print('Plot figure now is ',func_name,' ...')
        instance.plot()
    for func_name in bf.__twoArgument__:
        print('Plot figure now is ',func_name,' ...')
        instance = eval(func_name)(2)
        instance.plot()
    for func_name in bf.__threeArgument__:
        print('Plot figure now is ',func_name,' ...')
        instance = eval(func_name)(2,0.5)
        instance.plot()

if __name__ == '__main__':
    main()

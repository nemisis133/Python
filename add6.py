#Add 6

from module import Add # used to connect two py files

# or import module(file name)
def main2():
    print(__name__)
    n=int(input())
    m = int(input())
    Sum=Add(n,m)   #using module.Add(n,m)
    print(Sum)


if __name__== "__main__":
    main2()


#Any .py file which contains a funtion which we need to share




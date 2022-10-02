def main():
    Arr=list()
    print("No of elements:")
    size=int(input())

    for i in range(0,size):
        no = int(input())
        Arr.append(no)
    print(Arr)

if __name__=="__main__":
    main()

def Max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2


def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    max=Max(Value1,Value2)
    print("Larger is: ",max)

if __name__== "__main__":
    main()



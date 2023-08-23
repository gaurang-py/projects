
B=1
while B==1:
    print("\t","\t","\t","\t","Hello World","\t")
    print("\t","\t","\t","\t","Welcome to calculator")
    print("\t","\t","\t","\t","1.Addition")
    print("\t","\t","\t","\t","2.Subtraction")
    print("\t","\t","\t","\t","3.Multiple")
    print("\t","\t","\t","\t","4.Divison")
    print("\t","\t","\t","\t","5.Square")
    print("\t","\t","\t","\t","6.Square Root")
    print("\t","\t","\t","\t","7.Cube")
    print("\t","\t","\t","\t","8.Cube Root")
    print("\t","\t","\t","\t","9.TOTAL WITH GST")
    print("\t","\t","\t","\t","10.PERCENTAGE")
    print("\t","\t","\t","\t","What's Your choice")
    A=int(input("Enter Your choice:"))
    if A==1:
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        c=a+b
        print("\t","\t","\t","=",c)
    if A==2:
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        c=a-b
        print("\t","\t","\t","=",c)
    if A==3:
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        c=a*b
        print("\t","\t","\t","=",c)
    if A==4:
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        c=a/b
        print("\t","\t","\t","=",c)
    if A==5:
        a=int(input("Enter the Number:"))
        c=a*a
        print("\t","\t","\t","=",c)
    if A==6:
        a=int(input("Enter the Number:"))
        c=a**0.5
        print("\t","\t","\t","\t",c)
    if A==7:
        a=int(input("Enter the Number:"))
        c=a*a*a
        print("\t","\t","\t","=",c)
    if A==8:
        a=int(input("Enter the Number:"))
        c=a**1/3
        print("\t","\t","\t","=",c)
    if A==9:
        a=int(input("Enter total no of products:"))
        sum=0
        for i in range(0,a):
            b=int(input("Enter price of products:"))
            sum=sum+b
        print("\t","\t","\t","\t","1. 5% GST")
        print("\t","\t","\t","\t","2. 12% GST")
        print("\t","\t","\t","\t","3. 18% GST")
        print("\t","\t","\t","\t","4. 27% GST")
        c=int(input("ENTER YOUR CHOICE:"))
        if c==1:
            q=sum*5
            r=q/100
            sum=r+sum
            print("TOTAL AMOUNT AFTER ADDITION OF GST IS",sum)
        if c==2:
            q=sum*12
            r=q/100
            sum=r+sum
            print("TOTAL AMOUNT AFTER ADDITION OF GST IS",sum)
        if c==3:
            q=sum*18
            r=q/100
            sum=r+sum
            print("TOTAL AMOUNT AFTER ADDITION OF GST IS",sum)
        if c==4:
            q=sum*27
            r=q/100
            sum=r+sum
            print("TOTAL AMOUNT AFTER ADDITION OF GST IS",sum)
    if A==10:
        a=int(input("Enter SCORED marks:"))
        b=int(input("Enter TOTAL marks:"))
        c=a/b
        d=c*100
        print(d)
            
            

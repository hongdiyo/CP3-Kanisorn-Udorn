a = int(input("Enter number: "))
for x in range(a):
    s = " "*(a-x)
    d = "*"*((x*2)+1)
    print(s,d)
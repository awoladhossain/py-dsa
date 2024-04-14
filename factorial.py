def recursion(x):
    if(x==0 or x==1):
        return 1
    else:
        return x*recursion(x-1)

print("enter the number: ")
x=int(input())
result = recursion(x)
print(result)
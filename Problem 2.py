#Author: Nikhil Pachkor
print("Enter the number")
n=int(input())
for i in range(1,n+1,1):
    for j in range(1,2*i,1):
        if j>i:
            print(j-i,end="")
        else:
            print(j,end="")
    print("")


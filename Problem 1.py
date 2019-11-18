#Auhtor: Nikhil Pachkor
print("Enter the number")
n=int(input())
l=[]
for i in range(n):
    email=input()
    t=0
    x=0
    for j in range(0,len(email),1):
        if email[j]=="@":
            t=j
        if email[j]==".":
            x=j
    if email[len(email)-4:]==".com" and "@" in email and x-t>1 and t!=0:
        l.append(email)
for k in range(len(l)):
    print(l[k])

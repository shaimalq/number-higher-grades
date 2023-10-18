t=[]
n=int(input("saisir un nombre:"))
for i in range(1,n+1):
     print("t[" ,i ,"]=",end=" ")
     t.append(float(input()))
m=sum(t)/len(t)
nbr=0
for n in t:
     if n>=m:
          nbr+=1
print("la moyenne est",m)    
print("le nombres des notes superieur a la moyenne est",nbr)  
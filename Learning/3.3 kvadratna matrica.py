#I način
#n=int(input('Unesi broj kolona za kvadratnu matricu. '))
#suma=0

#for i in range(1,n+1):
#    for j in range(1,n+1):
#        suma+=i*j

#print('Suma je', suma)

#II način
n=int(input('Unesi broj kolona za kvadratnu matricu. '))
suma=n*n

for i in range(1,n):
    suma+=i*i
    for j in range(i+1,n+1):
        suma+=2*i*j

print('Suma je', suma)

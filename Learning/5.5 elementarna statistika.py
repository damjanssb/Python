#Izračunava srednju vrednost i standardno odstupanje uzorka slučajne promenljive x

def statistika(uzorak):
    so, n=0, len(uzorak)
    if n==0:
        return (None, None)
    elif n==1:
        return (uzorak[0],0)
    else:
        sv=sum(uzorak)/n
        for i in uzorak:
            so+=(i-sv)**2
        so=(so/(n-1))**0.5
        return (sv,so)

x=[1,2,3,4,5,4,3,2,1]
stat=statistika(x)
sr_vrednost, odstupanje=stat
print(x)
print(stat)
print('     Srednja vrednost je: ',stat[0])
print('     Srednja vrednost je: ',sr_vrednost)
print('Standardno odstupanje je: ',stat[1])
print('Standardno odstupanje je: ',odstupanje)

ulog,parnost=int(input("Koliko ulažeš?")),int(input("Unesite 0 za parnu ili 1 za neparnu vrednost."))
provera=ulog
print("")

while not(parnost==0 or parnost==1):
    print("Vrednost koju ste uneli nije ni 0 ni 1.")
    parnost=int(input("Unesite 0 za parnu ili 1 za neparnu vrednost."))
    print("")

ulog=ulog*2
if provera%2!=parnost:
    ulog=0

print("Tvoj trenutni saldo iznosi", ulog, "dinara.")

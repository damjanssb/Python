import itertools as it
'''a=[1,2,3,4]
for i in a:
    for j in a:
        if a.index(i) < a.index(j) and abs(i-j)==abs((i,j).index(i)-(i,j).index(j)):
            print((i, j))'''

#lista = [i for i in range(1,9)]
potencijalna_rešenja = list(it.permutations([i for i in range(1,9)]))
print(potencijalna_rešenja[3])

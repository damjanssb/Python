# kopira tekst datoteke uz prevođenje latinica->ćirilica

def prevedi_red(red, r):
    ćir_red, n, i = [], len(red), 0
    dupla_slova = {'lj', 'Lj', 'nj', 'Nj', 'dž', 'Dž'}
    while i < n-1:
        s, ss = red[i], red[i]+red[i+1]
        if ss in dupla_slova:
            ćir_red.append(r.get(ss, ss))
            i += 2
        else:
            ćir_red.append(r.get(s, s))
            i += 1
    if i == n-1:
        ćir_red.append(r.get(red[i], red[i]))

    return ''.join(ćir_red)

def prevedi(lat, ćir, r):
    try:
        with open(lat, encoding = 'utf-8') as dlat, \
             open(ćir, 'w', encoding = 'utf-8') as dćir:
            for red in dlat:
                dćir.write(prevedi_red(red, r))        
    except:
        print('Greška pri prevođenju.')
        
def uvoz_rečnika(p):
    r = {}
    try:
        with open(p, encoding = 'utf-8') as rečnik:
            for i in rečnik:
                par = i.strip().split(',')
                r[par[0]] = par[1]
    except:
        print('Greška sa uvozom rečnika.')
        r = {}
    return r

# test
# latinica: 'D:\\Programi\\New folder\\Python\\AgonijaSrpski.txt'
# ćirilica: 'D:\\Programi\\New folder\\Python\\AgonijaSrpski_ćir.txt'
#   rečnik: 'D:\\Programi\\New folder\\Python\\rečnik.txt'
lat = input('adresa datoteke za pervod: ')
ćir = input('adresa datoteke za čuvanje prevoda: ')
rečnik = input('adresa rečnika: ')
r = uvoz_rečnika(rečnik)
prevedi(lat, ćir, r)

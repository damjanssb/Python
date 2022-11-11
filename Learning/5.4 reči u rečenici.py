#formira listu reči iz zadate rečenice

def ukloni_interpunkciju(reč):
    '''Čisti unetu reč od interpunkciskih znakova sa početka i kraja reči.'''
    interpunkcija=['.', ',', '!', '?', ':', ';', '\'', '"']
    n=len(reč)
    levo=0
    while levo<n and reč[levo] in interpunkcija:
        levo+=1
    desno=n-1
    while desno>-1 and reč[desno] in interpunkcija:
        desno-=1
    return reč[levo:desno+1]

def reči(rečenica):
    '''Kreira listu reči iz rečenice.'''
    reči=[]
    for reč in rečenica.split():
        r=ukloni_interpunkciju(reč)
        if r!='':
            reči.append(r)
    return reči

rečenica=input('Unesi rečenicu: ')
print(reči(rečenica))

#poziva se iz 4.2 test modula površine
#sadrži funkcije za izračunavanje površina paralelograma, trapeza i kruga

paralelogram=1
trapez=2
krug=3

def p_paralelogram(a,h):
    '''Računa površinu paralelograma stranice a i visine h.''' 
    return a*h

def p_trapez(a,b,h):
    '''Računa površinu trapeza osnovica a i b i visine h.'''
    return (a+b)*h/2

def p_krug(r):
    '''Računa površinu kruga poluprečnika r.'''
    return r*r*3.14

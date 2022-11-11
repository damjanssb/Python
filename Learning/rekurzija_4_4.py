#poziva se iz 4.4 drugovi faktorijel i fibonači
#sadrži rekurzivne funkcije za izračunavanje faktorijela i fibonačija

def faktorijel(n):
    '''Vraća faktorijel za vrednosti n>=0'''
    if n<0:
        print('Da bi se izračunao faktorijel, n ne sme biti negativno.')
    elif n==1 or n ==0:
        return 1
    else:
        return n*faktorijel(n-1)
    
def fibonaci(n):
    '''Vraća Fibonačijev broj za vrednost n>=0'''
    if n<0:
        print('Da bi se izračunao Fibonači, n ne sme biti negativno.')
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)

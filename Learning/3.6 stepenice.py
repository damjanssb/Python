n= int(input('Unesi broj stepenica. '))

if n<1:
    print('Mora postojati najmanje jedan stepenik.')
elif n==1:
    print('Na jedan stepenik se može popeti na jedan način.')
elif n==2:
    print('Na dva stepenika se može popeti na dva načina.')
else:
    fi_2,fi_1=1,2
    for i in range(3,n+1):
        fi=fi_2+fi_1
        fi_2,fi_1=fi_1,fi
    
    print('Na', n, 'stepenika se može popeti na', fi, 'načina.')

'''user = 2 primary colors
    error if input is not prmary colors '''
    
def color_mixing():
    
    while True:
        kid1 = str(input('Primary color 1: '))
        kid2 = str(input('Primary color 2: '))
        
        if kid1 == 'red'  and kid2 == 'blue':
            print(f" {kid1} + {kid2} = Purple! ")
            ask = input('Again?')
            if ask != 'y':
                break
            else:
                continue
        elif kid1 == 'blue'  and kid2 == 'red':
            print(f" {kid1} + {kid2} = Purple! ")
            ask = input('Again?')
            if ask != 'y':
                break
            else:
                continue
            
        elif kid1 == 'red'  and kid2 == 'yellow':
            print(f" {kid1} + {kid2} = Orange! ")
            ask = input('Again?')
            if ask != 'y':
                break
            else:
                continue 
        elif kid1 == 'yellow'  and kid2 == 'red':
            print(f" {kid1} + {kid2} = Orange! ")
            ask = input('Again?')
            if ask != 'y':
                break
            else:
                continue      
        elif kid1 == 'blue'  and kid2 == 'yellow' :
            print(f" {kid1} + {kid2} = Green! ")
            ask = input('Again?')
            if ask != 'y':
                break
            else:
                continue
        elif kid1 == 'yellow'  and kid2 == 'blue' :
            print(f" {kid1} + {kid2} = Green! ")
            ask = input('Again?')
            if ask != 'y':
                break
            else:
                continue
        else:
            print('Please put a primary color.')
            ask = input('Again?')
            if ask != 'y':
                break
            else:
                continue
            
color_mixing()
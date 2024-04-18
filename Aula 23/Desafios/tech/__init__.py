

def lin(str):
        print ('-'*50)
        print ('{:^50}'.format(f'{str}'))
        print ('-'*50)

def menu(lst):
     l = 0
     k = len(lst)
     for c in lst:
        l = l + 1 
        if l == k:
            print (f'\033[93m {l} - \033[94m {c}\033[0;0m')
        else:
          print (f'\033[93m {l} - \033[94m {c}')
    
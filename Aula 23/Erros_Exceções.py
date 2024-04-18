

#### No python existem diversos tipos de erros que são chamadas de exceções, para evitar um mensagem de erro ou que programa pare de funcionar fazemos o seguinte:

### DESCRIÇÃO DO EXEMPLO ABAIXO: Tenta fazer algo que pode falhar, se falhar executa a ação 'except', se a tentativa (try) funcionar, o código vai para o else, o finally é o que acontece independentemente de o programa dar certo ou errado.
## ATENÇÃO: O uso de else e o finally são opicionais.

## try:
#    OPERAÇÃO DO CÓDIGO

## except:
#    FALHOU

## else:
#    DEU CERTO

## finally:
#    CERTO / FALHOU

# Ex 1:

try:
    print ()
    a = int(input('Digite o Númerador: '))
    b = int(input('Digite o Denominador: '))
    r = a/b
except Exception as erro:
    print ()
    print ('Infelizmente ocorreu um erro :( ')
    print (f'A classe do erro foi {erro.__class__}')
    


else:
    print (f'O resultado da divisão de {a} por {b} é igual a  {r:.2f}')

finally:
    print ('\n>> Volte sempre\n')
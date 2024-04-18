import requests
url = "https://pudim.com.br/"

try:
    requests.get(url).status_code == 200
        
except:
        print ('\n\033[91m   Não consegui acessar o site Pudim \033[0;0m\n')
else:
    print ('\n\033[93m   Consegui acessar o site Pudim \033[0;0m\n')
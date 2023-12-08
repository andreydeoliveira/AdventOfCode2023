import re

with open("input.txt", "r") as arquivo:
    
    resultado = 0
    
    while like := arquivo.readline():
        # print(like.strip())        
        # print(re.search("[0-9]", like.strip()).group())
        # print(re.search("[0-9]", like.strip()[::-1]).group())
        
        resultado += int(re.search("[0-9]", like.strip()).group()+re.search("[0-9]", like.strip()[::-1]).group())
     
    print(resultado)
    
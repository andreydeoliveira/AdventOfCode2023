import os 
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

resultado1 = 0
resultado2 = 0

with open(dir_path+"/input.txt", "r") as arquivo:
    while game := arquivo.readline():
        valor = re.sub('Game ([0-9]*):', '', game.strip())
        
        padrao = re.compile(r'(\d+)\s+(\w+)')
        arrays = padrao.findall(valor)
        
        green = 0
        blue = 0
        red = 0
        
        for numero, cor in arrays:
            if cor == 'blue' and blue < int(numero):
                blue = int(numero)
                
            if cor == 'red' and red < int(numero):
                red = int(numero)
                
            if cor == 'green' and green < int(numero):
                green = int(numero)
                                      
        if red <= 12 and green <= 13 and blue <= 14:
            # print(game.strip().replace(valor, "").replace("Game ", "").replace(":", ""))
            resultado1 += int(game.strip().replace(valor, "").replace("Game ", "").replace(":", ""))
        
        resultado2 += red*blue*green
        

print(resultado1)
print(resultado2)
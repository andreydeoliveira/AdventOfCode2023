import re
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))


def nameToNumber(name): 
    if name == 'one':
        return '1'
    if name == 'two':
        return '2'
    if name == 'three':
        return '3'
    if name == "four":
        return '4'
    if name == 'five':
        return '5'
    if name == 'six':
        return '6'
    if name == 'seven':
        return '7'
    if name == 'eight':
        return '8'
    if name == 'nine':
        return '9'
    return name


resultado01 = 0
resultado02 = 0 

with open(dir_path+"/input.txt", "r") as arquivo:
    
    while like := arquivo.readline():
        # print(like.strip())        
        # print(re.search("[0-9]", like.strip()).group())
        # print(re.search("[0-9]", like.strip()[::-1]).group())
        
        resultado01 += int(re.search("[0-9]", like.strip()).group()+re.search("[0-9]", like.strip()[::-1]).group())
       
with open(dir_path+"/input.txt", "r") as arquivo:
    
    while like := arquivo.readline():
        # lista = re.findall('one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9', like.strip())
        
        regex1 = r'(?=(one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9))'
        regex =  '(one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9)'
        lista = re.findall(regex, like.strip())
        
        if re.findall(regex, like.strip()) != re.findall(regex1, like.strip()):
            print(like.strip())
            print(re.findall(regex, like.strip()))
            print(re.findall(regex1, like.strip()))
            print('-----------')
        
        valor = nameToNumber(lista[0])+nameToNumber(lista[-1])
        # print(valor+' - '+like.strip())
        resultado02 += int(valor)

print("Resultado 01:")
print(resultado01)
        
print("Resultado 02:")
print(resultado02)
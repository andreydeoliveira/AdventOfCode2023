import os 

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(dir_path+"/input.txt", "r") as arquivo:
    
    minha_string = arquivo.read()
    
    # Dividindo a string em linhas
    linhas = minha_string.split('\n')   
    
    # Criando a matriz
    matriz = [list(linha) for linha in linhas]
    
    
    # Percorrendo a matriz usando índices de linha e coluna
    print("Percorrendo a matriz com índices:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor = matriz[i][j]
            print(f"Valor na linha {i}, coluna {j}: {valor}")
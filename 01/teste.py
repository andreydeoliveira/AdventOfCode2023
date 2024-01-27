import re

texto = "onetwothree"


# Expressão regular com lookahead positivo
regex1 = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
matches1 = re.findall(regex1, texto)

# Expressão regular sem lookahead positivo
regex = 'one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9'
matches = re.findall(regex, texto)

# Imprimindo as correspondências
print("Usando lookahead positivo:")
print(matches1)

print("\nSem lookahead positivo:")
print(matches)
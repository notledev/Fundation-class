name = input("Informe o nome \n")
idade = int(input("Informe a idade \n"))
altura = float(input("Informe a altura \n"))
profissional = bool(input("É profissional?\n"))

print("\n")
print("\n")

#Alternativa 1

# print("Dados do Participante")
# print("=====================")
# print("O nome é:", name)
# print("idade é:", idade)
# print("A altura é: ",altura)
# print("É profissional: ", profissional)

#Alternativa 2

print("Dados do Participante")
print("=====================")
print("O nome é:", name, "\n Idade é: ", idade, "\n altura é: ", altura, "\n É profissional?", profissional )

# Alternativa 3 FSTRING

print( f"Nome é {name} \n"
       f"Idade é: {idade}\n"
       f"Altura é: {altura}\n")
import random

resultado = ''
enquanto = 5
# Estas inha de comando verifica se 'enquanto' é menor que zero 
# E esecuta o codigo enquanto for verdade
while enquanto > 0:
    # O inport.randint serve para sortear numerros aleatorios.
    num_sorteado = random.randint(0, 9)
        # Transforma  os numerros sorteados en estring, acrecentando 
    #O numerro sorteado ao resultado gerando a sequencia da senha.
    resultado = str(resultado) + str(num_sorteado)
    enquanto = enquanto - 1    
x = (resultado)


def verificação(s, x):
    # Foi definido uma função para verificar a senha.
    r = []
    s = str(s)
    for i in range(len(s)):
    # A função lé a senha sorteada
        if s[i] in x:
            # Inporta o numero selecionado para a variavel 'i'
            if s[i] == x[i]:
                #Identifica se o numero esta no lugar
                r.append(1)
                #É se a linha anterior for verdade '1' sera adisionado alista
            else:
                # Se a linha anterior for falsa sera esecutada esta linha
                r.append(0)
                # O '0' sera idicionado a lista
        else:
            # Casa a primeira linha de codigo for falsa.
            r.append(-1)
            # O '-1' sera sera adicionado a lista 
    return r
    # A variavel 'r' resetara seu valor


s = input("digitea senha:")
# Foi definido a variavel 's'
print(verificação(s, x))
# Mostrara oresultado do codigo
    

vogais = ['a','e', 'i', 'o', 'u']
frequencia = [0, 0, 0, 0, 0]

palavra = input("Digite uma palavra: ")
for i in palavra.lower():
    if i in vogais:
        indexVogais = vogais.index(i)
        value = frequencia[indexVogais]
        frequencia[indexVogais] = value + 1

print("ocorrências com a vogal A: ", frequencia[0])
print("ocorrências com a vogal E: ", frequencia[1])
print("ocorrências com a vogal I: ", frequencia[2])
print("ocorrências com a vogal O: ", frequencia[3])
print("ocorrências com a vogal U: ", frequencia[4])
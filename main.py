def substituir_digitos(digitos, substituto):
    resultado = ''
    for c in digitos: #para cada caractere nos digitos
        if '0' <= c <= '9': #se for entre 0 e 9
            resultado += substituto #concatena o substituto, começa vazio
        else:
            resultado += c #se nao for digito, repete o caractere na string final
    return resultado


def substituir_set_caracteres(string_original, substituir ,substituto):
    conjunto = substituir[1:-1]  #pega os indices retirando os colchetes []
    resultado = ''
    for c in string_original: #para cada caractere na string
        if c in conjunto: #se estiver nos caracteres a ser substituído
            resultado += substituto #concatena o substituto, começa vazio
        else:
            resultado += c # se não, apenas repete o caractere que tinha na string original
    return resultado

def substituir_range_letras(string_original, substituir, substituto):
    resultado = ''
    for c in string_original: #para cada caractere na string
        if substituir[1] <= c <= substituir[3]: #se o caractere for uma letra no range do alfabeto
            resultado += substituto #concatena o substituto, começa vazio
        else:
            resultado += c # se não, apenas repete o caractere que tinha na string original
    return resultado

def substituir_grupos(string_original, substituir, substituto):
    grupo = substituir[1:-1] #pega os indices retirando os parenteses ()
    tamanho = len(grupo)
    resultado = ''
    i = 0
    while i < len(string_original): #enquanto a string não for vazia
        if string_original[i:i+tamanho] == grupo: #compara um pedaço da string original (indice atual + tamanho do grupo)
            resultado += substituto #se for igual ao grupo concatena o substituto com a nova string
            i += tamanho #salto de tamanho do grupo
        else:
            resultado += string_original[i] #se não for igual ao grupo, concatena o pedaço atual da string original no resultado
            i += 1 #incrementa 1 indice
    return resultado

def juntarListas(l1, l2):
    l3 = []
    for x in l1:
        if x not in l3:
            l3.append(x)
    for y in l2:
        if y not in l3:
            l3.append(y)
    return l3
# aqui vai fazer a união de conjuntos
def juntarConjunto(c1, c2):
    c1 = c1[1:-1]  
    c2 = c2[1:-1]
    resultado = ""
    for c in c1 + c2:
        if c not in resultado:
            resultado += c
    return "[" + resultado + "]"
# Teste
#print(substituir_digitos("975li90", "ya"))
#print(substituir_set_caracteres("975i0a", "ia0", "t"))
#print(substituir_range_letras("je3s5560lv", "[j-s]", "z"))
#print(substituir_grupos("vgu69utc", "(utc)", "*"))
# faz a junção, mas sem repetir
L1 = ["a", "ab", "abc","x"]
L2 = ["b", "ab", "bc","bcd"]
print("list 1:", L1)
print("list 2:", L2)
juntar = juntarListas(L1, L2)
print("Listas juntas:", juntar)

c1 = "[abcxx]"
c2 = "[bcdxxx]"
print("Conj 1:", c1)
print("Conj 2:", c2)
print("União de conjuntos:", juntarConjunto(c1, c2))

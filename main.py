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


#print(substituir_digitos("975li90", "ya"))
#print(substituir_set_caracteres("975i0a", "ia0", "t"))
#print(substituir_range_letras("je3s5560lv", "[j-s]", "z"))
#print(substituir_grupos("vgu69utc", "(utc)", "*"))
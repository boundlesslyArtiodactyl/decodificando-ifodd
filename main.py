import string

def decodificar_texto(texto):
    linhas = texto.splitlines()
    resultados = []
    
    for linha in linhas:
        if not linha.strip():
            continue
            
        tem_virgula_no_final = linha.rstrip().endswith(',')
        palavras = linha.split()
        letras_escondidas = []
        
        for palavra in palavras:
            palavra_limpa = palavra.translate(str.maketrans('', '', string.punctuation))
            tamanho = len(palavra_limpa)
            
            if tamanho == 0 or tamanho % 2 == 0:
                continue
                
            indice_meio = tamanho // 2
            letra_meio = palavra_limpa[indice_meio]
            letras_escondidas.append(letra_meio)
            
        palavra_final = "".join(letras_escondidas)
        
        if tem_virgula_no_final:
            palavra_final += ","
            
        resultados.append(palavra_final)
        
    return "\n".join(resultados)

if __name__ == "__main__":
    texto_teste = """"""
    
    resultado = decodificar_texto(texto_teste)
    print(resultado)


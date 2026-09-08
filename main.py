import string

def decodificar_texto(texto):
    linhas = texto.splitlines()
    resultados = []
    
    for linha in linhas:
        linha_limpa = linha.strip()
        if not linha_limpa:
            continue
            
        ultimo_caractere = linha_limpa[-1] if linha_limpa else ""
        tem_pontuacao_no_final = ultimo_caractere in string.punctuation
        
        palavras = linha_limpa.split()
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
        
        if tem_pontuacao_no_final:
            palavra_final += ultimo_caractere
            
        resultados.append(palavra_final)
        
    return "\n".join(resultados)

if __name__ == "__main__":
    texto_teste = """"""
    
    resultado = decodificar_texto(texto_teste)
    print(resultado)

    print(resultado)


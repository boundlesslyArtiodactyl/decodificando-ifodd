import string

def decodificar_frase(frase):
    tem_virgula_no_final = frase.rstrip().endswith(',')
    
    palavras = frase.split()
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
        
    return palavra_final

if __name__ == "__main__":
    frase_teste = "" 
    resultado = decodificar_frase(frase_teste)
    print(f"Frase original: {frase_teste}")
    print(f"Palavra escondida: {resultado}")

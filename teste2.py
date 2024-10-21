def minusculas(palavra):

    palavra_minuscula = palavra.lower()
    contagem = palavra_minuscula.count('a')
    
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vez(es) na palavra.")
    else:
        print(f"A letra 'a' não aparece na palavra.")

texto = input("Digite uma palavra: ")

minusculas(texto)

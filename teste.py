def fibonacci(num):
    a = 0
    b = 1
    sequencia = [a,b]
    
    while b < num :
        a, b = b, a+b 
        sequencia.append(b)
        
    print(sequencia)
    return(sequencia)

def tem_num(num):
    temaki = fibonacci(num) 
    
    if num in temaki:
        print(f"O numero {num} pertence a sequencia")
    else:
        print(f"O numero {num} nao pertence a sequencia")

entrada = int(input("numero desejado:"))

tem_num(entrada)
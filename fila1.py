fila=[1]
rodando=True
while rodando :
    print(fila)
    operacao=input("operacao a fazer:")
    for sigla in operacao:
        sigla=sigla.lower()
        if sigla=="a":
            fila.pop(0)
        if sigla=="f":
            fila.insert(len(fila),fila[-1]+1)
        if sigla == "s":
            rodando = False
            break

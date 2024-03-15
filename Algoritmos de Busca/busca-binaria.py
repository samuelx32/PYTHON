
def buscar(vetor,num):
    meio = int(len(vetor) / 2)
    while (meio > 0 and meio <= len(vetor)):
        if num == vetor[meio]:
            valor = vetor[meio]
            meio = 20000
        elif num < vetor[meio]:
            meio = int(meio / 2)
        elif num > vetor[meio]:
            meio = int((int(len(vetor)) - meio) / 2)  + meio
        
        if meio > 0 or meio <= len(vetor):
            valor = None
    return valor



def main():
    vetor = [2,7,10,15,17,17,20,23,25,29,31,33,37,39,41,42,58,62,67,77]

    resposta = buscar(vetor,62)
    print(resposta)

if __name__ == '__main__':
    main()


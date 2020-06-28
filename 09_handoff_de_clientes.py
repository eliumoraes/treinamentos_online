"""
Problema que resolvi no site geekhunter

5
3 6 8 4 7
4
3

7
1

def processInput ( input ):
    "Aqui você deve criar seu algoritmo para processar a entrada e depois retorna-la."
    return input

#Este bloco de código geralmente não precisa ser alterado, a não ser que julgue necessário.
value = input()
while (value):
    print(processInput(value))
    try:
        value = input()
    except EOFError:
        break
    
"""
def processInput (itens, arr, clientes, x):
    temp = []
    itens = int(itens)
    clientes = int(clientes)
    x = int(x)
    for i in range(clientes):
        temp = arr[1:]
        temp.append(arr[0])
        arr = temp
        temp = []
        #print(arr)

    print(arr[0])
    print(arr.index(x))

if __name__ == '__main__':
    itens = str(input())
    arr = list(map(int, input().rstrip().split()))
    clientes = str(input())
    x = str(input())

    processInput(itens, arr, clientes, x)
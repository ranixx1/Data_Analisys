pesquisas=[]

while(True):
    print("1 - Registrar pesquisa")
    print("0 - Sair")
    op = int(input("Digite a opção: "))
    if op == 0:
        break
    tcsat = int(input())
    dcsat = int(input())
    type = input()

    pesquisa_atual = [tcsat,dcsat,type]
    pesquisas.append(pesquisa_atual)

print(pesquisas)
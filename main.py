from regras import regras
from elevador import Elevador

def main():
    e = Elevador()

    print('Andar atual: 1')
    while True:
        andarEscolhido = input('Informe o andar ou uma sequência de andares: ')
        e.chamadaElevador(andarEscolhido)
        e.funcoes()

main()
""" if __name__ == '__main__':
    main() """
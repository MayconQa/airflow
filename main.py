from time import sleep

def primeiro_atividade():
    print("Essa é a primeira atividade do curso de Python.")
    sleep(5)

def segunda_atividade():
    print("Essa é a segunda atividade do curso de Python.")
    sleep(5)

def terceira_atividade():
    print("Essa é a terceira atividade do curso de Python.")
    sleep(5)

def pipeline():
    primeiro_atividade()
    segunda_atividade()
    terceira_atividade()
    print("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    while True:
        pipeline()
        sleep(5)
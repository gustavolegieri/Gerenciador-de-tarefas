import os
tarefas = []
a
global nome
global desc
global urgencia

def menu():
    print("|-------------------------------------|")
    print("| Bem-vindo ao gerenciador de tarefas |")
    print("|                                     |")
    print("|      O que deseja fazer?            |")
    print("|                                     |")
    print("|  1 - Criar tarefas                  |")
    print("|  2 - Listar tarefas                 |")
    print("|  3 - Editar tarefa                  |")
    print("|  4 - Excluir tarefa                 |")
    print("|  5 - Sair                           |")
    print("|                                     |")
    print("|-------------------------------------|")
    escolha = int(input("----> "))
    return escolha

def criar_tarefas():
    print("Informe os dados da tarefa que deseja criar")
    nome = input("Informe o nome da tarefa: ")
    desc = input("Informe a descrição da tarefa: ")
    urgencia = int(input("Informe o grau de urgência da tarefa: "))
    print()
    tarefas.append({
        "Nome": nome,
        "Descrição": desc,
        "Urgência": urgencia
    })
    print("Tarefa adicionada!")
    print()
    print("Deseja adicionar outra tarefa?")
    print()
    print("1 - Sim")
    print("2 - Não")
    escolha2 = int(input("---> "))
    if escolha2 == 1:
        criar_tarefas()
    else:
        limpa_console()

def listar_tarefas():
    x = 0
    print("Listar tarefas")
    print()
    if not tarefas:
        print("Nenhuma tarefa no sistema")
    else:
        for tarefa in tarefas:
            x += 1
            print(f"{x}° Tarefa ")
            print(f"Nome: {tarefa['Nome']}")
            print(f"Descrição: {tarefa['Descrição']}")
            print(f"Urgência: {tarefa['Urgência']}")
            print("-----------------------------")
    limpa_console()

def editar_tarefas():
    listar_tarefas()
    nome_editar = input("Digite o nome da tarefa que deseja editar: ")
    for tarefa in tarefas:
        if tarefa["Nome"] == nome_editar:
            print("Informe os novos dados da tarefa")
            tarefa["Nome"] = input("Novo nome da tarefa: ")
            tarefa["Descrição"] = input("Nova descrição da tarefa: ")
            tarefa["Urgência"] = int(input("Novo grau de urgência da tarefa: "))
            print("Tarefa atualizada!")
            limpa_console()
            break
        else:
            print("Tarefa não encontrada! ")
        limpa_console()

def excluir_tarefas():
    listar_tarefas()
    nome_excluir = input("Digite o nome da tarefa que deseja excluir: ")
    for tarefa in tarefas:
        if tarefa["Nome"] == nome_excluir:
            tarefas.remove(tarefa)
            print("Tarefa removida!")
            limpa_console()
            break
        else:
            print("Tarefa não encontrada")
        limpa_console()


def limpa_console():
    os.system("pause")
    os.system("cls")



os.system("pause")
from funcoes import *
import os
sair = 1
while sair == 1:
    escolha = menu()

    if escolha == 1:
        criar_tarefas()

    if escolha == 2:
        listar_tarefas()
    
    if escolha == 3:
        editar_tarefas()
    
    if escolha == 4:
        excluir_tarefas()
    
    if escolha == 5:
        sair = 0








os.system("pause")
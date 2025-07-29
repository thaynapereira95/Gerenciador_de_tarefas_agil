import json 
import os

DATA_FILE = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def salvar_tarefas(tarefas):
    with open(DATA_FILE, 'w') as file:
        json.dump(tarefas, file, indent=4)

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['titulo']} - {tarefa['status']}")

def adicionar_tarefas():
    titulo = input("Título da tarefa: ")
    tarefa = {"titulo": titulo, "status": "A Fazer"}
    tarefas = carregar_tarefas()
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso")

def atualizar_tarefas():
    listar_tarefas()
    index = int(input("Número da tarefa para atualizar: ")) - 1
    tarefas = carregar_tarefas()
    if 0 <= index < len(tarefas):
        tarefas[index]["status"] = input("Novo status (A Fazer / Em Progresso / Concluído): ")
        salvar_tarefas(tarefas)
        print("Tarefa atualizada")
    else:
        print("Tarefa inválida")

def deletar_tarefas():
    listar_tarefas()
    index = int(input("Número da tarefa para excluir: ")) - 1
    tarefas = carregar_tarefas()
    if 0 <= index < len(tarefas):
        tarefas.pop(index)
        salvar_tarefas(tarefas)
        print("Tarefa removida!")
    else:
        print("Tarefa inválida!")

def main(): 
    while True:
        print("\n[1] Listar [2] Adicionar [3] Atualizar [4] Excluir [0] Sair")
        option = input("Escolha uma opção: ")
        if option == "1":
            listar_tarefas()
        elif option == "2":
            adicionar_tarefas()
        elif option == "3":
            atualizar_tarefas()
        elif option == "4":
            deletar_tarefas()
        elif option == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

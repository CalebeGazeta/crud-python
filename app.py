import json  # módulo para trabalhar com arquivos JSON

# arquivo onde vamos salvar nossas tarefas
DATABASE_FILE = 'database.json'

# Função para carregar tarefas do arquivo JSON
def load_tasks():
    try:
        with open(DATABASE_FILE, 'r') as file:
            tasks = json.load(file)  # lê e transforma o JSON em lista
            return tasks
    except FileNotFoundError:
        return []  # se o arquivo não existir, retorna lista vazia

# Função para salvar tarefas no arquivo JSON
def save_tasks(tasks):
    # reorganiza os IDs para que fiquem sequenciais
    for index, task in enumerate(tasks):
        task['id'] = index + 1
    with open(DATABASE_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)  # salva a lista como JSON

# Função para adicionar uma tarefa
def add_task():
    tasks = load_tasks()
    task_name = input("Digite o nome da tarefa: ")
    task = {"id": len(tasks)+1, "name": task_name}  # cria a tarefa com ID sequencial
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarefa '{task_name}' adicionada com sucesso!")

# Função para listar todas as tarefas
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n===== Tarefas =====")
    for task in tasks:
        print(f"{task['id']} - {task['name']}")
    print("==================")

# Função para atualizar uma tarefa
def update_task():
    tasks = load_tasks()
    list_tasks()  # mostra a lista antes de atualizar
    try:
        task_id = int(input("Digite o ID da tarefa que deseja atualizar: "))
        found = False
        for task in tasks:
            if task['id'] == task_id:
                new_name = input("Digite o novo nome da tarefa: ")
                task['name'] = new_name
                save_tasks(tasks)
                print(f"Tarefa ID {task_id} atualizada com sucesso!")
                found = True
                break
        if not found:
            print("ID não encontrado. Tente novamente.")
    except ValueError:
        print("ID inválido! Digite apenas números.")

# Função para deletar uma tarefa
def delete_task():
    tasks = load_tasks()
    list_tasks()  # mostra a lista antes de deletar
    try:
        task_id = int(input("Digite o ID da tarefa que deseja deletar: "))
        new_tasks = [task for task in tasks if task['id'] != task_id]
        if len(new_tasks) == len(tasks):
            print("ID não encontrado. Nenhuma tarefa deletada.")
        else:
            save_tasks(new_tasks)
            print(f"Tarefa ID {task_id} deletada com sucesso!")
    except ValueError:
        print("ID inválido! Digite apenas números.")

# Função principal com menu
def main():
    while True:
        print("\n===== CRUD de Tarefas =====")
        print("1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Atualizar tarefa")
        print("4 - Deletar tarefa")
        print("5 - Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Saindo... até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

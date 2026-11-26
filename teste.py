#Aqui vou desenvolver meu código de teste para a revisão.
# Lista (array) que armazena os motores em memória durante a execução
motores = []


def cadastrar_motor():
    print("\n--- CADASTRAR NOVO MOTOR ---")
    codigo = input("Código/Série do motor: ").strip()

    # Evita duplicidade de código
    for m in motores:
        if m["codigo"].lower() == codigo.lower():
            print("Erro: Já existe um motor cadastrado com esse código!")
            return

    modelo = input("Modelo (ex: W22 IR3): ").strip()
    potencia = input("Potência (ex: 5 CV / 3.7 kW): ").strip()
    tensao = input("Tensão (ex: 220/380V): ").strip()
    rotacao = input("Rotação (ex: 1750 RPM): ").strip()

    motor = {
        "codigo": codigo,
        "modelo": modelo,
        "potencia": potencia,
        "tensao": tensao,
        "rotacao": rotacao,
    }

    motores.append(motor)
    print(f"Motor '{modelo}' (Cód: {codigo}) cadastrado com sucesso!")


def listar_motores():
    print("\n--- LISTA DE MOTORES CADASTRADOS ---")
    if not motores:
        print("Nenhum motor cadastrado ainda.")
        return

    for i, m in enumerate(motores, start=1):
        print(
            f"{i}. Cód: {m['codigo']} | Modelo: {m['modelo']} | "
            f"Potência: {m['potencia']} | Tensão: {m['tensao']} | RPM: {m['rotacao']}"
        )


def buscar_motor():
    print("\n--- BUSCAR MOTOR ---")
    termo = input("Digite o código ou modelo para buscar: ").strip().lower()

    encontrados = [
        m
        for m in motores
        if termo in m["codigo"].lower() or termo in m["modelo"].lower()
    ]

    if not encontrados:
        print("Nenhum motor encontrado com esse termo.")
        return

    for m in encontrados:
        print(
            f"-> Cód: {m['codigo']} | Modelo: {m['modelo']} | "
            f"Potência: {m['potencia']} | Tensão: {m['tensao']} | RPM: {m['rotacao']}"
        )


def remover_motor():
    print("\n--- REMOVER MOTOR ---")
    codigo = input("Digite o código do motor que deseja remover: ").strip()

    for i, m in enumerate(motores):
        if m["codigo"].lower() == codigo.lower():
            removido = motores.pop(i)
            print(f"Motor '{removido['modelo']}' removido com sucesso!")
            return

    print("Motor não encontrado.")


def menu():
    while True:
        print("="*30)
        print("   SISTEMA DE MOTORES (TESTE)")
        print("="*30)
        print("1 - Cadastrar motor")
        print("2 - Listar todos os motores")
        print("3 - Buscar motor")
        print("4 - Remover motor")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            remover_motor()
        elif opcao == "0":
            print("Encerrando o sistema. PLAU!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
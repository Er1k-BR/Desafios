from processamento import (
    cadastrar_funcionario,
    processar_salario,
    salvar_relatorio,
    gerar_relatorio,
)


def main():
    """Função principal do programa."""
    funcionarios = []
    while True:
        print("\n1. Cadastrar funcionário")
        print("2. Gerar relatório")
        print("3. Salvar relatório em arquivo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcionario = cadastrar_funcionario()
            resultado = processar_salario(funcionario)
            funcionarios.append(resultado)
            print(f"Funcionário {resultado['nome']} cadastrado com sucesso!")
        elif opcao == "2":
            if not funcionarios:
                print("Nenhum funcionário cadastrado!")
            else:
                gerar_relatorio(funcionarios)
        elif opcao == "3":
            if not funcionarios:
                print("Nenhum funcionário cadastrado!")
            else:
                salvar_relatorio(funcionarios)
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()

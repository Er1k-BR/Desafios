from calculos import (
    calcular_salario_clt,
    calcular_salario_estagiario,
    calcular_salario_freelancer,
)


def cadastrar_funcionario():
    """Cadastra um funcionário e retorna seus dados."""
    while True:
        try:
            nome = input("Digite o nome do funcionário: ")
            if not nome.strip():
                print("Nome não pode ser vazio!")
                continue
            tipo = input(
                "Digite o tipo de funcionário (estagiario/clt/freelancer): "
            ).lower()
            if tipo not in ["estagiario", "clt", "freelancer"]:
                print(
                    "O tipo de funcionário deve ser "
                    "'estagiario', 'clt' ou 'freelancer'!"
                )
                continue

            if tipo == "estagiario":
                salario = float(input("Digite o salário fixo (R$): "))
                if salario <= 0:
                    print("Salário deve ser maior que zero!")
                    continue
                return {"nome": nome, "tipo": tipo, "salario": salario}

            elif tipo == "clt":
                salario = float(input("Digite o salário bruto (R$): "))
                if salario <= 0:
                    print("Salário deve ser maior que zero!")
                    continue
                return {"nome": nome, "tipo": tipo, "salario": salario}

            elif tipo == "freelancer":
                horas = float(input("Digite o número de horas trabalhadas: "))
                valor_hora = float(input("Digite o valor por hora (R$): "))
                if horas <= 0 or valor_hora <= 0:
                    print("Horas e valor por hora devem ser maiores que zero!")
                    continue
                return {
                    "nome": nome,
                    "tipo": tipo,
                    "valor_hora": valor_hora,
                    "horas": horas,
                }
        except ValueError:
            print(
                "Entrada inválida! Use números para salário, "
                "horas ou valor por hora."
            )
        except Exception as e:
            print(f"Erro: {e}")


def processar_salario(funcionario):
    """Processa o salário com base no tipo de funcionário."""
    if funcionario["tipo"] == "estagiario":
        res = calcular_salario_estagiario(funcionario["salario"])
        return {"nome": funcionario["nome"], "tipo": "Estagiário", **res}

    elif funcionario["tipo"] == "clt":
        res = calcular_salario_clt(funcionario["salario"])
        return {"nome": funcionario["nome"], "tipo": "CLT", **res}

    elif funcionario["tipo"] == "freelancer":
        res = calcular_salario_freelancer(
            funcionario["valor_hora"], funcionario["horas"]
        )
        return {"nome": funcionario["nome"], "tipo": "Freelancer", **res}

    else:
        raise ValueError("Tipo de funcionário inválido!")


def salvar_relatorio(funcionarios):
    """Salva o relatório em um arquivo de texto."""
    caminho_arquivo = "relatorio_folha.txt"
    with open(caminho_arquivo, "w", encoding="utf-8") as file:
        file.write("=== Relatório de Folha de Pagamento ===\n")
        total_pago = 0
        for func in funcionarios:
            file.write(f"Nome: {func['nome']}\n")
            file.write(f"Tipo: {func['tipo']}\n")
            file.write(f"Salário Bruto: R$ {func['bruto']:.2f}\n")
            file.write(f"Desconto INSS: R$ {func['inss']:.2f}\n")
            file.write(f"Desconto IRRF: R$ {func['irrf']:.2f}\n")
            file.write(f"Salário Líquido: R$ {func['liquido']:.2f}\n")
            file.write("-" * 30 + "\n")
            total_pago += func["liquido"]
        file.write(f"Total pago pela empresa: R$ {total_pago:.2f}\n")
    print(f"Relatório salvo em '{caminho_arquivo}'.")


def gerar_relatorio(funcionarios):
    """Exibe os detalhes de todos os funcionários e o total pago."""
    print("\n=== Relatório de Folha de Pagamento ===")
    total_pago = 0
    for func in funcionarios:
        print(f"Nome: {func['nome']}")
        print(f"Tipo: {func['tipo']}")
        print(f"Salário Bruto: R$ {func['bruto']:.2f}")
        print(f"Desconto INSS: R$ {func['inss']:.2f}")
        print(f"Desconto IRRF: R$ {func['irrf']:.2f}")
        print(f"Salário Líquido: R$ {func['liquido']:.2f}")
        print("-" * 30)
        total_pago += func["liquido"]
    print(f"Total pago pela empresa: R$ {total_pago:.2f}")

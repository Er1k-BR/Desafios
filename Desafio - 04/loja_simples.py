from datetime import datetime
from pathlib import Path
from typing import List, Optional, TypedDict


DESCONTO_QUANTIDADE = 10
PERCENTUAL_DESCONTO = 0.05
ARQUIVO_RELATORIO_PADRAO = "relatorio_vendas.txt"


class Produto(TypedDict):
    nome: str
    preco: float
    estoque: int


class Venda(TypedDict):
    data: str
    cliente: str
    produto: str
    quantidade: int
    valor_bruto: float
    desconto: float
    valor_final: float


def formatar_moeda(valor: float) -> str:
    return f"R$ {valor:.2f}"


def ler_texto_obrigatorio(mensagem: str) -> str:
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Entrada obrigatoria. Tente novamente.")


def ler_float_positivo(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor > 0:
                return valor
            print("Informe um numero maior que zero.")
        except ValueError:
            print("Valor invalido. Digite um numero, exemplo: 50 ou 50.90.")


def ler_inteiro(
    mensagem: str, minimo: Optional[int] = None, maximo: Optional[int] = None
) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Informe um numero maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Informe um numero menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Valor invalido. Digite um numero inteiro.")


def buscar_produto_por_nome(produtos: List[Produto], nome: str) -> Optional[Produto]:
    nome_normalizado = nome.strip().lower()
    for produto in produtos:
        if produto["nome"].lower() == nome_normalizado:
            return produto
    return None


def cadastrar_produto(produtos: List[Produto]) -> None:
    print("\n=== Cadastro de Produto ===")
    while True:
        nome = ler_texto_obrigatorio("Nome do produto: ")
        if buscar_produto_por_nome(produtos, nome) is None:
            break
        print("Ja existe um produto com esse nome. Use outro nome.")

    preco = ler_float_positivo("Preco do produto: R$ ")
    estoque = ler_inteiro("Estoque inicial: ", minimo=0)

    produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
    print(f"Produto '{nome}' cadastrado com sucesso.")


def listar_produtos(
    produtos: List[Produto], apenas_disponiveis: bool = False
) -> List[Produto]:
    produtos_para_exibir = [
        produto for produto in produtos if not apenas_disponiveis or produto["estoque"] > 0
    ]

    if not produtos_para_exibir:
        print("Nenhum produto encontrado.")
        return []

    titulo = "Produtos Disponiveis" if apenas_disponiveis else "Produtos Cadastrados"
    print(f"\n=== {titulo} ===")
    for indice, produto in enumerate(produtos_para_exibir, start=1):
        print(
            f"{indice}. {produto['nome']} - {formatar_moeda(produto['preco'])} "
            f"- Estoque: {produto['estoque']}"
        )
    return produtos_para_exibir


def selecionar_produto(
    produtos: List[Produto], apenas_disponiveis: bool = True
) -> Optional[Produto]:
    produtos_exibidos = listar_produtos(produtos, apenas_disponiveis=apenas_disponiveis)
    if not produtos_exibidos:
        return None

    while True:
        selecao = input("Selecione por numero ou nome do produto: ").strip()

        if selecao.isdigit():
            indice = int(selecao)
            if 1 <= indice <= len(produtos_exibidos):
                return produtos_exibidos[indice - 1]
            print("Numero de produto inexistente.")
            continue

        produto = buscar_produto_por_nome(produtos_exibidos, selecao)
        if produto is not None:
            return produto
        print("Produto nao encontrado. Tente novamente.")


def calcular_venda(cliente: str, produto: Produto, quantidade: int) -> Venda:
    valor_bruto = produto["preco"] * quantidade
    desconto = valor_bruto * PERCENTUAL_DESCONTO if quantidade > DESCONTO_QUANTIDADE else 0
    valor_final = valor_bruto - desconto

    produto["estoque"] -= quantidade

    return {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "cliente": cliente,
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final,
    }


def realizar_venda(produtos: List[Produto], vendas: List[Venda]) -> None:
    print("\n=== Realizar Venda ===")
    if not produtos:
        print("Cadastre produtos antes de realizar vendas.")
        return

    cliente = ler_texto_obrigatorio("Nome do cliente: ")
    produto = selecionar_produto(produtos)
    if produto is None:
        return

    quantidade = ler_inteiro(
        f"Quantidade desejada (estoque: {produto['estoque']}): ",
        minimo=1,
        maximo=produto["estoque"],
    )

    venda = calcular_venda(cliente, produto, quantidade)
    vendas.append(venda)

    print("\nVenda realizada com sucesso!")
    print(f"Valor bruto: {formatar_moeda(venda['valor_bruto'])}")
    print(f"Desconto: {formatar_moeda(venda['desconto'])}")
    print(f"Valor final: {formatar_moeda(venda['valor_final'])}")


def montar_relatorio(vendas: List[Venda]) -> str:
    linhas = ["=== Relatorio de Vendas ==="]

    if not vendas:
        linhas.append("Nenhuma venda realizada.")
        return "\n".join(linhas)

    for venda in vendas:
        linhas.extend(
            [
                "",
                f"Data: {venda['data']}",
                f"Cliente: {venda['cliente']}",
                f"Produto: {venda['produto']}",
                f"Quantidade: {venda['quantidade']}",
                f"Valor Bruto: {formatar_moeda(venda['valor_bruto'])}",
                f"Desconto: {formatar_moeda(venda['desconto'])}",
                f"Valor Final: {formatar_moeda(venda['valor_final'])}",
            ]
        )

    total = sum(venda["valor_final"] for venda in vendas)
    linhas.extend(["", f"Total arrecadado pela loja: {formatar_moeda(total)}"])

    ultimas_vendas = vendas[-5:][::-1]
    linhas.append("\n=== Ultimas 5 Vendas ===")
    for venda in ultimas_vendas:
        linhas.append(
            f"{venda['data']} - {venda['cliente']} comprou "
            f"{venda['quantidade']}x {venda['produto']} por "
            f"{formatar_moeda(venda['valor_final'])}"
        )

    return "\n".join(linhas)


def gerar_relatorio(vendas: List[Venda]) -> None:
    print()
    print(montar_relatorio(vendas))


def salvar_relatorio(vendas: List[Venda]) -> None:
    print("\n=== Salvar Relatorio ===")
    caminho_digitado = input(
        f"Arquivo para salvar [{ARQUIVO_RELATORIO_PADRAO}]: "
    ).strip()
    caminho = Path(caminho_digitado or ARQUIVO_RELATORIO_PADRAO)

    try:
        caminho.write_text(montar_relatorio(vendas), encoding="utf-8")
        print(f"Relatorio salvo em: {caminho.resolve()}")
    except OSError as erro:
        print(f"Nao foi possivel salvar o relatorio: {erro}")


def atualizar_estoque(produtos: List[Produto]) -> None:
    print("\n=== Atualizar Estoque ===")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    produto = selecionar_produto(produtos, apenas_disponiveis=False)
    if produto is None:
        return

    novo_estoque = ler_inteiro("Novo estoque: ", minimo=0)
    produto["estoque"] = novo_estoque
    print(f"Estoque de '{produto['nome']}' atualizado para {novo_estoque}.")


def mostrar_menu() -> None:
    print(
        "\n=== Loja Simples ===\n"
        "1. Cadastrar produto\n"
        "2. Realizar venda\n"
        "3. Gerar relatorio\n"
        "4. Salvar relatorio em arquivo\n"
        "5. Atualizar estoque\n"
        "6. Listar produtos\n"
        "0. Sair"
    )


def main() -> None:
    produtos: List[Produto] = []
    vendas: List[Venda] = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            realizar_venda(produtos, vendas)
        elif opcao == "3":
            gerar_relatorio(vendas)
        elif opcao == "4":
            salvar_relatorio(vendas)
        elif opcao == "5":
            atualizar_estoque(produtos)
        elif opcao == "6":
            listar_produtos(produtos)
        elif opcao == "0":
            print("Programa encerrado. Ate logo!")
            break
        else:
            print("Opcao invalida. Escolha uma opcao do menu.")


if __name__ == "__main__":
    main()

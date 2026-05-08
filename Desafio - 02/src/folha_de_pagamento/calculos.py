def calcular_salario_estagiario(salario_fixo):
    """Calcula o salário do estagiário (sem descontos)."""
    return {
        "bruto": salario_fixo,
        "inss": 0.0,
        "irrf": 0.0,
        "liquido": salario_fixo
    }


def calcular_salario_clt(salario_bruto):
    """
    Calcula o salário CLT com descontos de INSS (8%)
    e IRRF (10% se salário > 2000).
    """
    inss = salario_bruto * 0.08
    irrf = salario_bruto * 0.10 if salario_bruto > 2000 else 0
    salario_liquido = salario_bruto - inss - irrf

    return {
        "bruto": salario_bruto,
        "inss": inss,
        "irrf": irrf,
        "liquido": salario_liquido
    }


def calcular_salario_freelancer(valor_hora, horas_trabalhadas):
    """Calcula o salário freelancer com desconto fixo de 5%."""
    salario_bruto = valor_hora * horas_trabalhadas
    desconto = salario_bruto * 0.05
    salario_liquido = salario_bruto - desconto

    return {
        "bruto": salario_bruto,
        "inss": desconto,
        "irrf": 0.0,
        "liquido": salario_liquido
    }

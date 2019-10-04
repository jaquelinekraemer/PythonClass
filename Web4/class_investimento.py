# 04/10/2019

# Investimento:
# Categoria
# Tipo
# Aporte (valor inicial)
# Rentabilidade (%)
# Perído Rentabilidade (dia, mes, ano)
# Valor

class Investimentos:
    def __init__(self, categoria, tipo, aporte, rentabilidade, periodo_rentabilidade):
        self.categoria = categoria
        self.tipo = tipo
        self.aporte = aporte
        self.rentabilidade = rentabilidade
        self.periodo_rentabilidade = periodo_rentabilidade

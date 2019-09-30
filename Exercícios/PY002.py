# 29/09/2019

# Criar um programa que utilize o método 50-20-10-20: (PaginaSobreMetodos)
# 1. Leia o salário líquido informado pelo usuário.
# 2. Organize os valores de acordo com o método citado.
# 3. Informe ao usuário qual o valor que ele deve destinar para cada categoria.
# Método 50-20-10-20 (50% gastos, 20% investimentos a longo prazo, 10% investimentos a curto prazo, 20% livre).

gastos = 0
longo_prazo = 0
curto_prazo = 0
livre = 0
print('='*60)
print('Organize as suas finanças com o método 50/20/10/20 a partir de agora!')
#Imprimindo salário
print('')
salario_liq = float(input('Informe o valor do seu salário líquido: '))
gastos = salario_liq * 50 / 100
longo_prazo = salario_liq * 20 / 100
curto_prazo = salario_liq * 10 / 100
livre = salario_liq * 20 / 100
print('')
print('Abaixo mostramos o quanto você pode gastar em cada categoria, de acordo com o valor do seu salário líquido!')
print('{}Valor do salário líquido: {} R${:8.2f}'.format(' '*5,' '*10, salario_liq))
print('{}Para os gastos você deve destinar {} R${:8.2f}'.format(' '*5,' '*10, gastos))
print('{}Para os investimentos a longo prazo você deve destinar {} R${:8.2f}'.format(' '*5,' '*10, longo_prazo))
print('{}Para os investimentos a curto prazo você deve destinar {} R${:8.2f}'.format(' '*5,' '*10, curto_prazo))
print('{}E livre você tem: {} R${:8.2f}'.format(' '*5,' '*10, livre))
print('')
print('Fim do programa. Volte sempre!')
print('='*60)
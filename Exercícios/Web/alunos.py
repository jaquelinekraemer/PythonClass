class Alunos:
    def __init__(self, nome, sobrenome, telefone):
        self.Nome = nome
        self.Sobrenome = sobrenome
        self.Telefone = telefone
        
    def nome_completo(self):
        nomecompleto = self.Nome + ' ' + self.Sobrenome
        return nomecompleto

#def define o método
#Método é uma funcionalidade da classe
#O uso do self é obrigatório
#A classe agrupa um conjunto de caracteristicas e pode ser acessada por uma variavel
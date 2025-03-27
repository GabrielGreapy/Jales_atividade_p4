class Funcionario():
    def __init__(self, nome , salario_base):
        self.nome = nome
        self.salario_base = salario_base
    def calcular_salario(self, salario_base):
        return salario_base

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        self.nome = nome
        self.salario_base = salario_base
        self.bonus = bonus
    def calcular_salario(self):
        return self.salario_base + self.salario_base*(self.bonus/100)

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao):
        self.nome = nome
        self.salario_base = salario_base
        self.comissao = comissao
    def calcular_salario(self):
        return self.salario_base + self.comissao
    
f1 = Gerente('Antony', 20, 10)
f2 = Gerente('Beatriz', 1, 30) 
f3 = Gerente('Anderson', 21, 314)
f4 = Vendedor('Gabriel', 2000, 999999)

lista = [f1, f2, f3, f4]

def Folha_De_Pagamento(lista):
    for i in lista:
        print(f"Nome: {i.nome}, Salário: {i.calcular_salario()}")
print(Folha_De_Pagamento(lista))

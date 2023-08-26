# Padrão de Projeto Strategy para uma Calculadora

# Definindo a classe base "Operation" que será usada para criar as operações específicas.
class Operation:
    def execute(self, a, b):
        pass


# Definindo as classes para operações específicas (adição, subtração, Multiplicação e Divisão.).
class AddOperation(Operation):
    def execute(self, a, b):
        return a + b


# (As outras classes "SubtractOperation", "MultiplyOperation" e "DivideOperation" seguem o mesmo padrão.)

class SubtractOperation:
    def execute(self, a, b):
        return a - b


class MultiplyOperation:
    def execute(self, a, b):
        return a * b


class DivideOperation:
    def execute(self, a, b):
        return a * b

# Definindo a classe "Calculator" que recebe uma operação como parâmetro.


class Calculator:
    def __init__(self, operation):
        self.operation = operation

    def calculate(self, a, b):
        result = self.operation.execute(a, b)
        operator = self.get_operator()
        return f"Resultado: {a} {operator} {b} = {result:.2f}"

    def get_operator(self):
        if isinstance(self.operation, AddOperation):
            return "+"
        elif isinstance(self.operation, SubtractOperation):
            return "-"
        elif isinstance(self.operation, MultiplyOperation):
            return "*"
        elif isinstance(self.operation, DivideOperation):
            return "/"


# Função auxiliar para obter entrada de número do usuário
def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


# Exemplo de uso
print("Escolha uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
choice = input("Digite o número da operação desejada: ")

# Condições para escolher a operação com base na escolha do usuário.
if choice == "1":
    operation = AddOperation()
elif choice == "2":
    operation = SubtractOperation()
elif choice == "3":
    operation = MultiplyOperation()
elif choice == "4":
    operation = DivideOperation()
else:
    print("Operação inválida.")
    exit()

# Solicitação de entrada de números do usuário.
num1 = get_number_input("Digite o primeiro número: ")
num2 = get_number_input("Digite o segundo número: ")

# Criação da instância da classe Calculator e cálculo da operação escolhida.
calculator = Calculator(operation)
result = calculator.calculate(num1, num2)

# Exibição do resultado.
print(result)

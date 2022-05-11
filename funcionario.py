class Funcionario():
    def __init__(self, nome):
        self.nome = nome

    def registra_hora(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caleum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caleum')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster():
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caleum, Hipster):
    pass

# jose = Junior()
# jose.busca_perguntas_sem_resposta()

luan = Pleno('Igor')
print(luan)

# luan.busca_cursos_do_mes()
# luan.busca_perguntas_sem_resposta()

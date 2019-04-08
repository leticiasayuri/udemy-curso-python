from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def adiciona(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procura(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def conclui(self):
        self.feito = True

    def __str__(self):
        status = []

        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)


def main():
    tarefas_casa = Projeto('Tarefas de Casa')
    tarefas_casa.adiciona('Passar roupa', datetime.now())
    tarefas_casa.adiciona('Lavar prato')
    print(tarefas_casa)

    tarefas_casa.procura('Lavar prato').conclui()
    for tarefa in tarefas_casa:
        print(f'- {tarefa}')

    print(tarefas_casa)

    tarefas_mercado = Projeto('Compras no mercado')
    tarefas_mercado.adiciona('Frutas secas')
    tarefas_mercado.adiciona('Carne')
    tarefas_mercado.adiciona('Tomate', datetime.now() +
                             timedelta(days=3, minutes=12))
    print(tarefas_mercado)

    comprar_carne = tarefas_mercado.procura('Carne')
    comprar_carne.conclui()

    for tarefa in tarefas_mercado:
        print(f'- {tarefa}')
    print(tarefas_mercado)


if __name__ == '__main__':
    main()

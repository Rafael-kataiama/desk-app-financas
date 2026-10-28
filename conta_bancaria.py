from banco_de_dados import Banco_de_dados
from transacoes import*
# Categoria das contas bancarias:

class Conta_bancaria:

    def __init__(self, usuario, numero_conta, saldo_inicial=0):
        
        self._usuario = usuario
        self._numero_conta = numero_conta
        
        # Inicializa o banco de dados (que carrega o JSON se ele existir)
        self.informacoes_do_usuario = Banco_de_dados(self._usuario, self._numero_conta, saldo_inicial)
        
        # Pega diretamente o saldo que o banco de dados resolveu (seja do arquivo ou o inicial)
        self._saldo = self.informacoes_do_usuario._saldo

    def processar_receitas(self, descricao, valor, categoria): #processar receita

        receita = Receita(descricao, valor, categoria) #cria instacia de classe receita
        self._saldo = receita.processar_saldo(self._saldo) #lanca a receita e atualiza o saldo
        self.informacoes_do_usuario.registrar_dados(self._saldo, receita) #registra a receita no banco de dados
        print(self._saldo)

    def processar_despesas(self, descricao, valor, categoria): #processar despesa

        despesa = Despesa (descricao, valor, categoria)
        self._saldo = despesa.processar_saldo(self._saldo)
        self.informacoes_do_usuario.registrar_dados(self._saldo, despesa)
        print(self._saldo)

    def imprimir_transacoes(self):

        for transacao in self.informacoes_do_usuario.lista_de_transacoes:
            print(transacao)
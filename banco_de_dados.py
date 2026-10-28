import json

#classe banco de dados:

class Banco_de_dados:

    def __init__(self, usuario, numero_conta, saldo_inicial=0):
        
        self._usuario = usuario
        self._numero_conta = numero_conta
        self._saldo = saldo_inicial
        self.lista_de_transacoes = []
        self.arquivo = f"{usuario}.json"

        self.carregar_dados()

    

    def carregar_dados(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                self._saldo = dados.get("saldo", self._saldo)
                # aplica o .get() no dicionario 'dados'
                self.lista_de_transacoes = dados.get("transacoes", [])

        except FileNotFoundError:
            # Se o arquivo não existir ainda (primeiro acesso), segue normal
            pass


    def __str__(self):
        return f"Usuario: {self._usuario}, Numero da conta: {self._numero_conta}, Saldo: {self._saldo}"

    
    def registrar_dados(self, novo_saldo, transacao=None):

        self._saldo = novo_saldo

        if transacao:

            dados_de_transacao = {
                "descricao" : transacao.descricao,
                "valor" : transacao._valor,
                "categoria" : transacao.categoria
            } # receita = Receita(descricao, valor, categoria)

            self.lista_de_transacoes.append(dados_de_transacao)


        dados_do_usuario = {
                        "usuario" : self._usuario,
                        "numero da conta" : self._numero_conta,
                        "saldo" : self._saldo,
                        "transacoes" : self.lista_de_transacoes
                    }
        
        with open(self.arquivo, "w") as arquivo:
            json.dump(dados_do_usuario, arquivo)
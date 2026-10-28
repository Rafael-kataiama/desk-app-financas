from abc import ABC, abstractclassmethod
#categoria de transacoes:

class Transacao (ABC): # CLASSE ABSTRATA: Serve como modelo/contrato base.

    def __init__(self, descricao, valor, categoria):
        self.descricao = descricao
        self._valor = valor  # Guardado com underline para encapsulamento
        self.categoria = categoria

    def mostrar_valor(self):
        """Retorna o valor guardado."""
        return self._valor

    @abstractclassmethod
    def processar_saldo(self, saldo_atual):
        """Será implementado nas classes filhas (Polimorfismo)."""
        pass

    @abstractclassmethod
    def get_tipo(self):
        """Será implementado nas classes filhas."""
        pass

class Receita(Transacao):

    def __init__(self, descricao, valor, categoria):
        super().__init__(descricao, valor, categoria)

    def __str__(self):
        return f"Receita: {self.descricao}, Valor: {self.mostrar_valor()}, Categoria: {self.categoria}"

    def processar_saldo(self, saldo_atual): #pega saldo e processa a receita, retornando o novo saldo
        return saldo_atual + self._valor

    def get_tipo(self):
        return f"Receita, descricao: {self.descricao}"

class Despesa(Transacao):

    def __init__(self, descricao, valor, categoria):
        super().__init__(descricao, valor, categoria)

    def __str__(self):
        return f"Despesa: {self.descricao}, Valor: {self.mostrar_valor()}, Categoria: {self.categoria}"

    def processar_saldo(self, saldo_atual):
        return saldo_atual - self._valor

    def get_tipo(self):
        return f"Despesa, descricao: {self.descricao}"
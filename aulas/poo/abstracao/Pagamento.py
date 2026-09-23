from abc import ABC, abstractmethod
# ABC -> Abstract Base Class
# Anotações de abstração

#classe PAI
#DEFINIR INTERFACE
class Pagamento(ABC): # Classe ABSTRATA
    @abstractmethod
    def pagar(self, valor): # metodo ABSTRATO
        #Defino a INTERFACE
        #NÃO defino sua IMPLEMENTAÇÃO
        pass
    def amortizar(self, parcela, metodo):
        print(f"Amortizando a {parcela}º parcela via {metodo}")

#classe FLHA
#DEFINIR INTERFACE
class Pix(Pagamento):
    def pagar(self, valor):
        print(f"Desconto de 10% no PIX")
        desconto = valor  * 0.10
        valor_final = valor - desconto
        print(f"Pagando R$ {valor_final:.2f} via PIX")
        #Defino a IMPLEMENTAÇÃO do metodo herdado

#DEFINIR INTERFACE
class Boleto(Pagamento):
    def pagar(self, valor):
        print(f"Pagando R$ {valor} via BOLETO")

#DEFINIR INTERFACE
class Cartao(Pagamento):
    def pagar(self, valor):
        print(f"Pagando R$ {valor} no débito via CARTÃO")

    def parcelar(self, valor):
        print(f"Pagando R$ {valor} parcelado via CARTÃO")

#DEFINIR AS IMPLEMENTAÇÕES
class Principal:
    def efetuar_pagamento(metodo_pagamento: Pagamento, valor: float):
        print(f"Efetuando pagamento")
        metodo_pagamento.pagar(valor)

        print("====== EFETUANDO PAGAMENTOS ======")

    efetuar_pagamento(Pix(), 100.00)

    pagamento_pix = Pix()
    pagamento_boleto = Boleto()
    pagamento_cartao = Cartao()

    pagamento_pix.pagar(100)
    pagamento_pix.amortizar(12, "PIX")
    pagamento_boleto.pagar(100)
    pagamento_cartao.pagar(2000)
    pagamento_cartao.parcelar(5000)
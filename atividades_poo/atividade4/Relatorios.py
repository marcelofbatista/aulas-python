from abc import ABC, abstractmethod

class Relatorio(ABC):
    @abstractmethod
    def exportar(self, valor):
        pass

class PDF(Relatorio):
    def exportar(self, valor):
        if valor =
        print("Exportar para PDF")

exportar_pdf = PDF()

exportar_pdf.exportar(50)
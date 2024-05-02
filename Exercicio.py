from abc import ABC, abstractmethod

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Produto(ABC):
    def __init__(self, modelo, cor, preço, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preço = preço
        self.categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preço}, Categoria: {self.categoria.nome}"

    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(Produto):
    def __init__(self, modelo, cor, preço, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preço, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Potência da Fonte: {self._potenciaDaFonte}"

    # Getter e Setter para potenciaDaFonte
    def get_potenciaDaFonte(self):
        return self._potenciaDaFonte

    def set_potenciaDaFonte(self, potenciaDaFonte):
        self._potenciaDaFonte = potenciaDaFonte

class Notebook(Produto):
    def __init__(self, modelo, cor, preço, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preço, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Tempo de Bateria: {self.__tempoDeBateria}"

    # Getter e Setter para tempoDeBateria
    def get_tempoDeBateria(self):
        return self.__tempoDeBateria

    def set_tempoDeBateria(self, tempoDeBateria):
        self.__tempoDeBateria = tempoDeBateria

# Teste das classes
if __name__ == "__main__":
    # Criando uma categoria
    categoria_pc = Categoria(1, "Computadores")

    # Criando um Desktop
    desktop = Desktop("Modelo1", "Preto", 1500, categoria_pc, "500W")

    # Criando um Notebook
    notebook = Notebook("Modelo2", "Branco", 1200, categoria_pc, "6 horas")

    # Testando os métodos de informação
    print(desktop.getInformacoes())
    print(notebook.getInformacoes())

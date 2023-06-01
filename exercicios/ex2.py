'''
3. Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_lados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura
    
    def ret_lados(self):
        return(self.base, self.altura)

    def calc_area(self):
        return (self.altura) * (self.base)
    
    def perimetro(self):
        return (self.base*2) + (self.altura*2)

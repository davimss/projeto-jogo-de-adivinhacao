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

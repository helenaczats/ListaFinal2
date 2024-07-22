import math

# Funções Area Cubo, Area Paralelogramo e Area Piramide

def area_cubo(aresta):
    if aresta < 0:
        raise ValueError("O comprimento da aresta não pode ser negativo")
    return (aresta ** 2) * 6

def area_paralelogramo(base,altura):
    return base * altura
    
def area_piramide(aresta, altura):
    if aresta < 0 or altura < 0:
        raise ValueError("O comprimento da aresta e/ou da altura não pode ser negativo")
    # Área da base (quadrada)
    area_base = aresta ** 2
    
    # Meia-diagonal da base
    meia_diagonal = (aresta * math.sqrt(2)) / 2
    
    # Altura lateral usando o teorema de Pitágoras
    altura_lateral = math.sqrt(altura ** 2 + meia_diagonal ** 2)
    
    # Área das faces laterais (4 triângulos)
    area_lateral = 2 * aresta * altura_lateral
    
    # Área total
    area_total = area_base + area_lateral
    
    return area_total
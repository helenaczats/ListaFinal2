import pytest
from area.area import area_cubo, area_paralelogramo, area_piramide
from utils.utils import ler_csv

#Teste de Unidade Simples Positivo

def test_area_cubo_positivo():
    
    aresta = 4
    resultado_esperado = 96
    resultado_obtido = area_cubo(aresta)
    assert resultado_esperado == resultado_obtido

def test_paralelogramo():
    
    base = 6
    altura = 4
    resultado_esperado = 24
    
    resultado_obtido = area_paralelogramo(base, altura)
    
    assert resultado_esperado == resultado_obtido
    
def test_area_piramide():
    
    aresta = 10
    altura = 6
    resultado_esperado = 285.47
    
    resultado_obtido = area_piramide(aresta, altura)
    
    assert round(resultado_obtido, 2) == round(resultado_esperado, 2), \
        f"Resultado esperado: {round(resultado_esperado, 2)}, mas obteve: {round(resultado_obtido, 2)}"

    
#Teste de Unidade Simples Negativo
    
def test_calcular_area_cubo_negativo():
    a = -4
    with pytest.raises(ValueError) as excinfo:
        area_cubo(a)
    assert str(excinfo.value) == "O comprimento da aresta não pode ser negativo"
    
    
#Teste Piramide, com Arquivo CSV, Positivo
    
@pytest.mark.parametrize("aresta, altura, resultado_esperado",
                         ler_csv("./fixtures/massa_piramide_positivo.csv")
                         )
    
def test_area_piramide_csv(aresta, altura, resultado_esperado):
    resultado_obtido = area_piramide(float(aresta), float(altura))
    print("resultado:",resultado_obtido)
    assert round(float(resultado_obtido), 2) == round(float(resultado_esperado), 2), \
        f"Resultado esperado: {float(resultado_esperado, 2)}, mas obteve: {float(resultado_obtido, 2)}"


#Teste Piramide, com Arquivo CSV, Negativo 

@pytest.mark.parametrize("aresta, altura, resultado_esperado",
                         ler_csv("./fixtures/massa_piramide_negativa.csv")
                         )
    
def test_area_piramide_negativo_csv(aresta, altura, resultado_esperado):
    with pytest.raises(ValueError) as excinfo:
        area_piramide(float(aresta), float(altura))
    assert str(excinfo.value) == resultado_esperado
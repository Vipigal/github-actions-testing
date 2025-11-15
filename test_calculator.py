import pytest
from calculator import Calculator


class TestCalculator:
    """Testes para a classe Calculator"""
    
    def setup_method(self):
        """Setup executado antes de cada teste"""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Teste 1: Soma de números positivos"""
        result = self.calc.add(5, 3)
        assert result == 8
    
    def test_add_negative_numbers(self):
        """Teste 2: Soma com números negativos"""
        result = self.calc.add(-5, -3)
        assert result == -8
    
    def test_subtract(self):
        """Teste 3: Subtração"""
        result = self.calc.subtract(10, 4)
        assert result == 6
    
    def test_multiply(self):
        """Teste 4: Multiplicação"""
        result = self.calc.multiply(7, 6)
        assert result == 42
    
    def test_divide(self):
        """Teste 5: Divisão normal"""
        result = self.calc.divide(15, 3)
        assert result == 5
    
    def test_divide_by_zero(self):
        """Teste 6: Divisão por zero deve lançar exceção"""
        with pytest.raises(ValueError, match="Não é possível dividir por zero"):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Teste 7: Potenciação"""
        result = self.calc.power(2, 3)
        assert result == 8
    
    def test_power_zero(self):
        """Teste 8: Qualquer número elevado a zero é 1"""
        result = self.calc.power(5, 0)
        assert result == 1
    
    def test_multiply_by_zero(self):
        """Teste 9: Multiplicação por zero"""
        result = self.calc.multiply(999, 0)
        assert result == 0

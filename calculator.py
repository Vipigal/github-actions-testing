class Calculator:
    """Classe calculadora com operações matemáticas básicas"""
    
    def add(self, a: float, b: float) -> float:
        """Soma dois números"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtrai b de a"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiplica dois números"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide a por b"""
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b
    
    def power(self, base: float, exponent: float) -> float:
        """Calcula base elevado ao expoente"""
        return base ** exponent

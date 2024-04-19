from typing import Optional


class Bond:
    """Класс облигаций"""
    
    def __init__(self,
                 nominal: float,
                 price: float,
                 isin: Optional[str] = None):
        self.nominal = nominal
        self.price = price
        self.isin = isin
        self.discount = self.nominal - self.price if self.nominal - self.price > 0 else 0
        self.premium = self.price - self.nominal if self.price - self.nominal > 0 else 0
        pass

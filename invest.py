from typing import Optional, Union
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td
from datetime import date


class Bond:
    """Класс облигаций"""

    Percent = float
    
    def __init__(self,
                 nominal: float,
                 market_price: float,
                 date_of_maturity: Union[dt, str],
                 nkd: Optional[float] = None,
                 calculation_date: Optional[dt] = None,
                 basis: int = 365):
        self.nominal = nominal
        """Номинальная стоимость облигации"""

        self.market_price = market_price
        """Рыночная стоимость облигации"""

        self.date_of_maturity = date_of_maturity if isinstance(date_of_maturity, date) else dt.fromisoformat(date_of_maturity)
        """Дата погашения облигации / Дата оферты"""

        self.nkd = nkd
        """НКД"""

        self.calculation_date = dt.now().date() if calculation_date is None else calculation_date
        """Дата расчета"""

        self.term = (self.date_of_maturity - self.calculation_date).days
        """Срок до погашения"""

        self.basis = basis
        """Базис"""
    
    def get_simple_yield(self,
                         coupons: pd.Series) -> Percent:
        Y = round(((self.nominal - self.market_price)/self.market_price)*(self.basis/self.term)*100, 3)
        """Доходность бескупонной облигации"""

        if self.nkd is None:
            return Y

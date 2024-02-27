class Bill:
    """
    Represents a bill consisting of the total amount and
    period of the bill.
    """

    def __init__(self, amount: float, period: str):
        self.amount = amount
        self.period = period
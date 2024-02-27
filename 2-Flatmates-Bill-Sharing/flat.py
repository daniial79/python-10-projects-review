


class Flatmate:
    """
    Represents flatmate who lives in flat and pays the share of the bill
    """

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house
        self.amount_to_pay = 0


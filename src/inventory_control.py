class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self._data = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, customer, order, day):
        if order == "hamburguer":
            if (
                self._data["pao"] < 50 and
                self._data["carne"] < 50 and
                self._data["queijo"] < 100
            ):
                self._data["pao"] += 1
                self._data["carne"] += 1
                self._data["queijo"] += 1
            else:
                return False
        elif order == "pizza":
            if (
                self._data["massa"] < 50 and
                self._data["molho"] < 50 and
                self._data["queijo"] < 100
            ):
                self._data["massa"] += 1
                self._data["queijo"] += 1
                self._data["molho"] += 1
            else:
                return False
        elif order == "misto-quente":
            if (
                self._data["pao"] < 50 and
                self._data["presunto"] < 50 and
                self._data["queijo"] < 100
            ):
                self._data["pao"] += 1
                self._data["presunto"] += 1
                self._data["queijo"] += 1
            else:
                return False
        elif order == "coxinha":
            if (
                self._data["massa"] < 50 and
                self._data["frango"] < 50
            ):
                self._data["massa"] += 1
                self._data["frango"] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self._data

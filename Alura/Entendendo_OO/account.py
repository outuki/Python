
class Account:
    
    def __init__(self, number: int, client: str, balance: float, limit: float):
        self._number = number
        self._client = client
        self._balance = balance
        self._limit = limit

    def saldo(self):
        print(f"Saldo de {self._balance} do Titular {self._name}")

    def deposita(self, value: float):
        self._balance += value

    def saca(self, value: float):
        if (value <= self._balance + self._limit):
            self._balance -= value
        else:
            print("limite insuficiente")

    def transfere(self, value: float, destiny: str):
        self.saca(value)
        destiny.deposita(value)

    def get_saldo(self) -> float:
        return self._balance

    def get_cliente(self) -> int:
        return self._client

    @property
    def limite(self) -> float:
        return self._limit

    @limite.setter
    def limite(self, limit: float):
        self._limit = limit
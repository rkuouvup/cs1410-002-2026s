from decimal import Decimal
# Decimal ("-12.3")
# sign (0), digits(1, 2, 3), exp (-1)

class InvalidWithDrawal(ValueError):
    def __init__(self) -> None:
        super().__init__(f"account doesn't have enough amount")

class InvalidDeposit(ValueError):
    def __init__(self):
        super().__init__(f"invalid deposit amount")

class BankAccount:
    def __init__(self, balance:Decimal = Decimal("0.0")) -> None:
        self._balance:Decimal = balance
    def withdrawal(self, amount:Decimal) -> None:
        if amount > self._balance:
            raise InvalidWithDrawal
        else:
            self._balance = self._balance - amount
    def deposit(self, amount:Decimal) -> None:
        if amount < 0:
            raise InvalidDeposit
        else:
            self._balance = self._balance - amount
    def __str__(self) -> str:
        return f"The balance is {self._balance:.2f}"
def main() -> None:
    b = BankAccount(Decimal("1000.0"))
    print(b)

    try:
        b.withdrawal(Decimal("1100"))
        print(b)
    except InvalidWithDrawal as ex:
        print(f"Error: {ex}")

    deposit_amount = input("Please enter the deposit amount: ")
    
    try:
        float(deposit_amount)
        b.deposit(Decimal(deposit_amount))
        print(b)
    
    except ValueError:
        print("Value Error")
    except InvalidDeposit:
        print("Invalid Deposit")
    

if __name__ == "__main__":
    main()
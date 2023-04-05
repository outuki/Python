def create_account(number, name, balance, limit):
    account = {"number": number, "name": name, "balance": balance, "limit": limit}
    return account

def deposit(account, value):
    account["balance"] += value

def withdraw(account, value):
    account["balance"] -= value

def statement(account):
    print(f'Balance: {account["balance"]}')
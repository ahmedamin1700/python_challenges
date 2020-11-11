class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({
                "amount": -1 * amount,
                "description": description
            })
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, cat):
        withdraw = self.withdraw(amount, "Transfer to " + cat.name)
        if withdraw:
            cat.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def __str__(self):
        message = ""
        message += "{:*^30}".format(self.name)
        message += "\n"
        for item in self.ledger:
            description = "{:.23}".format(item["description"])
            message += description
            message += "{:.2f}".format(item["amount"]).rjust(30 - len(description))
            message += "\n"
        message += "Total: {}".format(self.balance)
        return message


# def create_spend_chart(categories):


food = Category("food")
relax = Category("relax")
food.deposit(500, "Initial deposit")
food.transfer(200, relax)
print(food.balance, relax.balance)
print(food)

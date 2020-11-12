class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spent = 0

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
            self.spent += amount
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


def create_spend_chart(categories):
    result = "Percentage spent by category\n"

    # total spent amount for all categories.
    total = sum(x.spent for x in categories)
    # percentage for each category spent regarding previous total.
    percentages = [(x.spent / total) // 0.01 for x in categories]

    for x in range(100, -10, -10):
        result += str(x).rjust(3, " ") + '|'
        for y in percentages:
            if y >= x:
                result += ' o '
            else:
                result += '   '
        result += ' \n'
    result += '    ' + '-' * len(percentages) * 3 + '-\n'
    max_length = max(len(x.name) for x in categories)
    for x in range(max_length):
        result += '    '
        for y in categories:
            if x < len(y.name):
                result += ' ' + y.name[x] + ' '
            else:
                result += '   '
        result += ' \n'
    return result.rstrip() + '  '

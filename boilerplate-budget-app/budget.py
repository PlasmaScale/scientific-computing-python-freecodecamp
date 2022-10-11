class Category:
    number_of_cat = 0

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        Category.add_cat()

    @classmethod
    def add_cat(cls):
        cls.number_of_cat += 1

    @classmethod
    def get_num_of_cat(cls):
        return cls.number_of_cat

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})
        self.balance += amount

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": desc})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": f"Transfer to {target.name}"})
            self.balance -= amount
            target.ledger.append({"amount": amount, "description": f"Transfer from {self.name}"})
            target.balance += amount
            return True
        return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        return False

    def total_spent_in_category(self):
        spent = 0
        for i in range(len(self.ledger)):
            if self.ledger[i]["amount"] < 0:
                spent += self.ledger[i]["amount"]
        return abs(spent)

    def __str__(self):
        total = f"{self.name:*^30}\n"
        for i in range(len(self.ledger)):
            total += "{description:<23.23}{amount:>7.2f}\n".format(**self.ledger[i])
        total += f"Total: {self.balance:.2f}"
        return total

def longest_name_of_object(lst):
    lst = [len(item.name) for item in lst]
    return max(lst)

def add_whitespace(lst):
    names = []
    max_len = longest_name_of_object(lst)
    for item in lst:
      item = f"{item.name:<{max_len}}"
      names.append(item)
    return names

def total_spent(lst):
    total_spent = 0
    for item in lst:
        total_spent += item.total_spent_in_category()
    return total_spent

def plot_values(lst):
    values = []
    for item in lst:
        value = (item.total_spent_in_category() / total_spent(lst)) * 100
        value = int(value)
        values.append(value)
    return values

def values_into_points(lst):
    values = plot_values(lst)
    points = []
    for item in values:
        point = "o" * int((item / 10 + 1 ))
        point = f"{point:>11}"
        points.append(point)
    return points

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    points = values_into_points(categories)
    for i in range (100, -10, -10):
        chart += f"{str(i):>3}| "
        for point in points:
            index = int((100 - i) / 10)
            chart += f"{point[index]}  "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    names = add_whitespace(categories)
    for i in range(len(names[0])):
        chart += "     "
        for item in names:
            chart += f"{item[i]}  "
        chart += "\n"

    return chart.rstrip() + "  "

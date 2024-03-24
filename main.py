class Formula:
    def __init__(self, formula, *args):
        self.formula: str = formula
        self.args = args

    def calc(self, *args):
        if len(self.args) != len(args):
            raise ValueError()
        for n in range(len(self.args)):
            exec(f"{self.args[n]} = {args[n]}")
        ans = eval(self.formula)
        return ans


# f = Formula("x**2 + 4*y + 4", "x", "y")
# print(f.calc(4, 3))

class Limit:
    def __init__(self, min_limit, max_limit):
        self.min = min_limit
        self.max = max_limit

    def check(self, num):
        if self.max == "infinity":
            if self.min == "infinity":
                return True
            else:
                if self.min <= num:
                    return True
                else:
                    return False
        else:
            if self.min == "infinity":
                if self.max >= num:
                    return True
                else:
                    return False
            else:
                if self.max >= num:
                    if self.min <= num:
                        return True
                    else:
                        return False
                else:
                    return False


# lenge1 = Limit("infinity", "infinity")
# print(lenge1.check(500))

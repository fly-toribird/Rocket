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
    def __init__(self, value, min_limit, max_limit):
        self.value = value
        self.min = min_limit
        self.max = max_limit

    def check(self, num, value):
        if value != self.value :
            raise ValueError()
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

class LimitedFormula :
    def __init__(self,formula,*limits):
        self.formula: formula = formula
        self.limits = limits

    def calc(self, *args):
        for i in range(len(self.limits)):
            if not self.limits[i].check(args[i]):
                return None

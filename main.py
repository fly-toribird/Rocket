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
    def __init__(self, min_limit, value, max_limit, mode_min="e", mode_max="e"):
        self.min = min_limit
        self.mode_min = mode_min
        self.value = value
        self.mode_max = mode_max
        self.max = max_limit
        if not (mode_min == "n" or mode_min == "e"):
            raise ValueError()
        if not (mode_max == "n" or mode_max == "e"):
            raise ValueError()

    def check(self, value, num):
        if value != self.value:
            raise ValueError()
        if self.max == "infinity":
            if self.min == "infinity":
                return True
            else:
                if self.mode_min == "e":
                    return self.min <= num
                else:
                    return self.min < num
        else:
            if self.min == "infinity":
                if self.mode_max == "e":
                    return self.max > num
                else:
                    return self.max >= num
            else:
                if self.mode_max == "e":
                    if self.max >= num:
                        if self.mode_min == "e":
                            return self.min <= num
                        else:
                            return self.min < num
                    else:
                        return False
                else:
                    if self.max > num:
                        if self.mode_min == "e":
                            return self.min <= num
                        else:
                            return self.min < num
                    else:
                        return False


lenge1 = Limit(2, "x", 10)
print(lenge1.check("x", 1))


class LimitedFormula:
    def __init__(self, formula, *limits):
        self.formula: formula = formula
        self.limits = limits

    def calc(self, *args):
        for i in range(len(self.limits)):
            if not self.limits[i].check(self.formula.args[1], args[i]):
                return None

import TBFLib as fl
import sympy

runch_pad = fl.LimitedFormula(fl.Formula("x ** 2 / 12"), fl.Limit(0, "x", 12))
runch_padd = fl.LimitedFormula(sympy.diff(runch_pad.formula.getformula()), runch_pad.limits[0])
print(runch_pad.formula.getformura(), runch_padd.formula.getformula())

import random


origin_formulas = ["+", "-", "*", "/"]

class formula:
    def __init__(self,formula):
        self.formula:list = formula

    def add(self,new_formula):
        self.formula.append(new_formula)

    def remove(self,number):
        del self.formula[number]


def calculate(formula,num1,num2):
    for f in formula.formula :
        if f == "+":
            num1 = num1 + num2
        elif f == "-":
            num1 = num1 - num2
        elif f == "*":
            num1 = num1 * num2
        elif f == "/":
            num1 = num1 / num2
    return num1


example_formula = formula(["+","-","*","/"])


class Math_animal:
    def __init__(self,unique_number,unique_formulas,gene,input,output):
        self.unique_number = unique_number
        self.unique_formulas:set = unique_formulas
        self.gene:formula = gene
        self.input:formula = input
        self.output:formula = output
    
    def info(self):
        print(self.unique_number)
        print(self.unique_formulas)
        print(self.gene.formula)
        print(self.input.formula)
        print(self.output.formula)

    def inherit(self):
        """UN:unique_number, UF:unique_formula"""
        new_UN = random.int(self.unique_number - 1, self.unique_number + 1)
        self.unique_formulas.add(self.gene)
        new_UFs = self.unique_formulas
        new_gene = random.choice(new_UFs).append(random.choice(origin_formulas))
        new_input = random.choice(new_UFs)
        new_output = random.choice(new_UFs)
        return (Math_animal(new_UN,new_UFs,new_gene,new_input,new_output))
    
    def test(self) :
        print("aaa")

animals_list = []
manimal = Math_animal(1,formula(origin_formulas),formula(["+","x"]),formula("+"),formula("-"))
manimal.info
import random


origin_formulas = {"+", "-", "*", "/"}

class formula:
    def __init__(self,formula):
        self.formula:list = formula

    def fadd(self,new_formula):
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

    def pre_inherit(self):
        """UN:unique_number, UF:unique_formula"""
        new_UN = random.randint(self.unique_number - 1, self.unique_number + 1)
        old_UFs = self.unique_formulas
        old_UFs.add(self.gene)
        new_UFs = list(old_UFs)
        new_gene = formula(list(random.choice(new_UFs)))
        new_gene.fadd(random.choice(list(origin_formulas)))
        new_input = formula(random.choice(new_UFs))
        new_output = formula(random.choice(new_UFs))
        animals_list.append(Math_animal(new_UN,new_UFs,new_gene,new_input,new_output))

    def inherit(self,num):
        for k in range(num):
            self.pre_inherit()

animals_list = []
animals_list.append(Math_animal(1,
                                origin_formulas,
                                formula(["+","x"]),
                                formula("+"),
                                formula("-")))
animals_list[0].inherit(2)
print(animals_list)
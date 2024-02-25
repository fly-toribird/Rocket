import random


origin_formulas = ["+", "-", "*", "/"]


class formula:
    def __init__(self,formula):
        self.formula = formula

    def add(self,new_formula):
        self.formula.append(new_formula)

    def remove(self,number):
        del self.formula[number]


class Math_animal:
    def __init__(self,unique_number,unique_formulas,gene,input,output):
        self.unique_number = unique_number
        self.unique_formulas:set = unique_formulas
        self.gene:formula = gene
        self.input:formula = input
        self.output:formula = output

    def inherit(self):
        """UN:unique_number, UF:unique_formula"""
        new_UN = random.int(self.unique_number - 1, self.unique_number + 1)
        self.unique_formulas.add(self.gene)
        new_UFs = self.unique_formulas
        new_gene = random.choice(new_UFs).append(random.choice(origin_formulas))
        new_input = random.choice(new_UFs)
        new_output = random.choice(new_UFs)
        animal_list.append(Math_animal(new_UN,new_UFs,new_gene,new_input,new_output))

animal_list = []

animal_list.append(Math_animal(1,["+"],["+"],["-"]))
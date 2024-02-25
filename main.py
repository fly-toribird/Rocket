class formula:
    def __init__(self,formula):
        self.formula = formula


def gen_formula(formula):
    return formula(formula)

class Math_animal:
    def __init__(self,unique_number,gene,input,output):
        self.unique_number = unique_number
        self.gene:int = gene
        self.input:int = input
        self.output:int = output
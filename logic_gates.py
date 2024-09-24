def nand_gate(a, b):
    return not (a and b)

def and_gate(a, b):
    ab_nand = nand_gate(a, b)
    return nand_gate(ab_nand, ab_nand)

def not_gate(a):
    return nand_gate(a, a)

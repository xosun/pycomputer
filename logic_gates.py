def nand_gate(a, b):
    return not (a and b)


def and_gate(a, b):
    ab_nand = nand_gate(a, b)
    return nand_gate(ab_nand, ab_nand)


def not_gate(a):
    return nand_gate(a, a)


def or_gate(a, b):
    aa_nand = nand_gate(a, a)
    bb_nand = nand_gate(b, b)
    return nand_gate(aa_nand, bb_nand)

def xor_gate(a, b):
    ab_nand = nand_gate(a, b)
    a_and_ab_nand = nand_gate(a, ab_nand)
    b_and_ab_nand = nand_gate(b, ab_nand)
    return nand_gate(a_and_ab_nand, b_and_ab_nand)
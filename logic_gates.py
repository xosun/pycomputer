def nand_gate(a, b):
    return 1 if a == 0 or b == 0 else 0


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


def mux_circuit(a, b, sel):
    c = nand_gate(a, sel)
    d = nand_gate(sel, sel)
    e = nand_gate(b, d)
    return nand_gate(c, e)


def dmux_circuit(sel, data):
    not_sel = nand_gate(sel, sel)
    not_sel_data = nand_gate(not_sel, data)
    sel_data = nand_gate(sel, data)
    a = nand_gate(not_sel_data, not_sel_data)
    b = nand_gate(sel_data, sel_data)
    return a, b

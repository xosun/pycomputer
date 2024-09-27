import inspect


def nand_gate(a: int, b: int) -> int:
    return 1 if a == 0 or b == 0 else 0


def and_gate(a: int, b: int) -> int:
    ab_nand = nand_gate(a, b)
    return nand_gate(ab_nand, ab_nand)


def not_gate(a: int) -> int:
    return nand_gate(a, a)


def or_gate(a: int, b: int) -> int:
    aa_nand = nand_gate(a, a)
    bb_nand = nand_gate(b, b)
    return nand_gate(aa_nand, bb_nand)


def xor_gate(a: int, b: int) -> int:
    ab_nand = nand_gate(a, b)
    a_and_ab_nand = nand_gate(a, ab_nand)
    b_and_ab_nand = nand_gate(b, ab_nand)
    return nand_gate(a_and_ab_nand, b_and_ab_nand)


def mux(a: int, b: int, sel: int) -> int:
    c = nand_gate(a, sel)
    d = nand_gate(sel, sel)
    e = nand_gate(b, d)
    return nand_gate(c, e)


def dmux(sel: int, data: int) -> tuple[int, int]:
    not_sel = nand_gate(sel, sel)
    not_sel_data = nand_gate(not_sel, data)
    sel_data = nand_gate(sel, data)
    a = nand_gate(not_sel_data, not_sel_data)
    b = nand_gate(sel_data, sel_data)
    return a, b


def x16_x(func, args):
    print(args)
    return [func(args[0][idx]) for idx in range(16)]


def x16_xy(func, args):
    return [func(args[0][idx], args[1][idx]) for idx in range(16)]


def x16_xysel(func, args):
    return [func(args[0][idx], args[1][idx], args[2]) for idx in range(16)]


def not16(a: list[int]) -> list[int]:
    return x16_x(not_gate, [a])


def and16(a: list[int], b: list[int]) -> list[int]:
    return x16_xy(and_gate, [a, b])


def or16(a: list[int], b: list[int]) -> list[int]:
    return x16_xy(or_gate, [a, b])


def mux16(a: list[int], b: list[int], sel: int) -> list[int]:
    return x16_xysel(mux, [a, b, sel])

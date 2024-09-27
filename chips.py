def nand_gate(x: int, y: int) -> int:
    return 1 if x == 0 or y == 0 else 0


def and_gate(x: int, y: int) -> int:
    xy_nand = nand_gate(x, y)
    return nand_gate(xy_nand, xy_nand)


def not_gate(x: int) -> int:
    return nand_gate(x, x)


def or_gate(x: int, y: int) -> int:
    xx_nand = nand_gate(x, x)
    yy_nand = nand_gate(y, y)
    return nand_gate(xx_nand, yy_nand)


def xor_gate(x: int, y: int) -> int:
    xy_nand = nand_gate(x, y)
    x_and_xy_nand = nand_gate(x, xy_nand)
    y_and_xy_nand = nand_gate(y, xy_nand)
    return nand_gate(x_and_xy_nand, y_and_xy_nand)


def mux(x: int, y: int, sel: int) -> int:
    a = nand_gate(x, sel)
    b = nand_gate(sel, sel)
    c = nand_gate(y, b)
    return nand_gate(a, c)


def dmux(sel: int, x: int) -> tuple[int, int]:
    not_sel = nand_gate(sel, sel)
    not_sel_x = nand_gate(not_sel, x)
    sel_x = nand_gate(sel, x)
    a = nand_gate(not_sel_x, not_sel_x)
    b = nand_gate(sel_x, sel_x)
    return a, b


def x16_x(func, args):
    return [func(args[0][idx]) for idx in range(16)]


def x16_xy(func, args):
    return [func(args[0][idx], args[1][idx]) for idx in range(16)]


def x16_xysel(func, args):
    return [func(args[0][idx], args[1][idx], args[2]) for idx in range(16)]


def not16(x: list[int]) -> list[int]:
    return x16_x(not_gate, [x])


def and16(x: list[int], y: list[int]) -> list[int]:
    return x16_xy(and_gate, [x, y])


def or16(x: list[int], y: list[int]) -> list[int]:
    return x16_xy(or_gate, [x, y])


def mux16(x: list[int], y: list[int], sel: int) -> list[int]:
    return x16_xysel(mux, [x, y, sel])

def nand_gate(x: int, y: int) -> int:
    return 1 if x == 0 or y == 0 else 0


def and_gate(x: int, y: int) -> int:
    return nand_gate(nand_gate(x, y), nand_gate(x, y))


def not_gate(x: int) -> int:
    return nand_gate(x, x)


def or_gate(x: int, y: int) -> int:
    return nand_gate(nand_gate(x, x), nand_gate(y, y))


def xor_gate(x: int, y: int) -> int:
    xy = nand_gate(x, y)
    return nand_gate(nand_gate(x, xy), nand_gate(y, xy))


def mux(x: int, y: int, sel: int) -> int:
    return nand_gate(nand_gate(nand_gate(sel, sel), x), nand_gate(sel, y))


def dmux(x: int, sel: int) -> tuple[int, int]:
    nselx = nand_gate(nand_gate(sel, sel), x)
    selx = nand_gate(sel, x)
    return nand_gate(nselx, nselx), nand_gate(selx, selx)


def not16(x: list[int]) -> list[int]:
    return [not_gate(x[i]) for i in range(16)]


def and16(x: list[int], y: list[int]) -> list[int]:
    return [and_gate(x[i], y[i]) for i in range(16)]


def or16(x: list[int], y: list[int]) -> list[int]:
    return [or_gate(x[i], y[i]) for i in range(16)]


def mux16(x: list[int], y: list[int], sel: int) -> list[int]:
    return [mux(x[i], y[i], sel) for i in range(16)]


def or8way(x: list[int]) -> int:
    out = x[0]
    for i in range(1, len(x)):
        out = or_gate(out, x[i])
    return out


def mux4way16(
    a: list[int], b: list[int], c: list[int], d: list[int], sel: list[int]
) -> tuple[int]:
    return mux16(mux16(a, b, sel[1]), mux16(c, d, sel[1]), sel[0])


def mux8way16(
    a: list[int],
    b: list[int],
    c: list[int],
    d: list[int],
    e: list[int],
    f: list[int],
    g: list[int],
    h: list[int],
    sel: list[int],
) -> tuple[int]:
    return mux16(
        mux16(mux16(a, b, sel[2]), mux16(c, d, sel[2]), sel[1]),
        mux16(mux16(e, f, sel[2]), mux16(g, h, sel[2]), sel[1]),
        sel[0],
    )


def dmux4way(x, sel: list[int]) -> tuple[int]:
    a0, b0 = dmux(x, sel[0])
    return dmux(a0, sel[1]) + dmux(b0, sel[1])


def dmux8way(x, sel: list[int]) -> tuple[int]:
    a0, b0 = dmux(x, sel[0])
    a00, b00 = dmux(a0, sel[1])
    c00, d00 = dmux(b0, sel[1])
    return dmux(a00, sel[2]) + dmux(b00, sel[2]) + dmux(c00, sel[2]) + dmux(d00, sel[2])


def halfadder(a: int, b: int) -> tuple[int]:
    sum = xor_gate(a, b)
    carry = and_gate(a, b)
    return sum, carry

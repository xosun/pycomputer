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


def half_adder(a: int, b: int) -> tuple[int]:
    sum = xor_gate(a, b)
    carry = and_gate(a, b)
    return sum, carry


def full_adder(a: int, b: int, c: int) -> tuple[int]:
    ab, cab = half_adder(a, b)
    sum, s = half_adder(c, ab)
    carry = or_gate(cab, s)
    return sum, carry


def add16(a: list[int], b: list[int]) -> list[int]:
    out = [0] * 16
    out[15], c = half_adder(a[15], b[15])
    out[14], d = full_adder(a[14], b[14], c)
    out[13], e = full_adder(a[13], b[13], d)
    out[12], f = full_adder(a[12], b[12], e)
    out[11], g = full_adder(a[11], b[11], f)
    out[10], h = full_adder(a[10], b[10], g)
    out[9], i = full_adder(a[9], b[9], h)
    out[8], j = full_adder(a[8], b[8], i)
    out[7], k = full_adder(a[7], b[7], j)
    out[6], l = full_adder(a[6], b[6], k)
    out[5], m = full_adder(a[5], b[5], l)
    out[4], n = full_adder(a[4], b[4], m)
    out[3], o = full_adder(a[3], b[3], n)
    out[2], p = full_adder(a[2], b[2], o)
    out[1], q = full_adder(a[1], b[1], p)
    out[0], _ = full_adder(a[0], b[0], q)
    return out

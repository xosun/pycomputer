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


def validate16(func):
    def wrapper(data: list[int]) -> list[int]:
        if len(data) != 16:
            raise ValueError("Input list must be exactly 16 integers long")
        return func(data)

    return wrapper


def validate16x2(func):
    def wrapper(a: list[int], b: list[int], sel: int = 0) -> list[int]:
        if len(a) != 16 or len(b) != 16:
            raise ValueError("Input list must be exactly 16 integers long")
        num_params = len(inspect.signature(func).parameters)
        if num_params == 2:
            return func(a, b)
        else:
            return func(a, b, sel)

    return wrapper


@validate16
def not16(data: list[int]) -> list[int]:
    output = []
    for bit in data:
        output.append(not_gate(bit))
    return output


@validate16x2
def and16(a: list[int], b: list[int]) -> list[int]:
    output = []
    for idx in range(len(a)):
        output.append(and_gate(a[idx], b[idx]))
    return output


@validate16x2
def or16(a: list[int], b: list[int]) -> list[int]:
    output = []
    for idx in range(len(a)):
        output.append(or_gate(a[idx], b[idx]))
    return output


@validate16x2
def mux16(a: list[int], b: list[int], sel: int) -> list[int]:
    output = []
    for idx in range(len(a)):
        output.append(mux(a[idx], b[idx], sel))
    return output

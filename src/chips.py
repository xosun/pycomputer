def nand_gate(a: int, b: int) -> int:
    """Implements a NAND gate.

    Args:
        a: The first input bit.
        b: The second input bit.

    Returns:
        The output bit of the NAND gate.

    Examples:
        >>> nand_gate(0, 0)
        1
        >>> nand_gate(0, 1)
        1
        >>> nand_gate(1, 0)
        1
        >>> nand_gate(1, 1)
        0
    """
    return 1 if a == 0 or b == 0 else 0


def and_gate(a: int, b: int) -> int:
    """Implements an AND gate using NAND gates.

    Args:
        a: The first input bit.
        b: The second input bit.

    Returns:
        The output bit of the AND gate.

    Examples:
        >>> and_gate(0, 0)
        0
        >>> and_gate(0, 1)
        0
        >>> and_gate(1, 0)
        0
        >>> and_gate(1, 1)
        1
    """
    return nand_gate(nand_gate(a, b), nand_gate(a, b))


def not_gate(a: int) -> int:
    """Implements a NOT gate using a NAND gate.

    Args:
        a: The input bit.

    Returns:
        The output bit of the NOT gate.

    Examples:
        >>> not_gate(0)
        1
        >>> not_gate(1)
        0
    """
    return nand_gate(a, a)


def or_gate(a: int, b: int) -> int:
    """Implements an OR gate using NAND gates.

    Args:
        a: The first input bit.
        b: The second input bit.

    Returns:
        The output bit of the OR gate.

    Examples:
        >>> or_gate(0, 0)
        0
        >>> or_gate(0, 1)
        1
        >>> or_gate(1, 0)
        1
        >>> or_gate(1, 1)
        1
    """
    return nand_gate(nand_gate(a, a), nand_gate(b, b))


def xor_gate(a: int, b: int) -> int:
    """Implements an XOR gate using NAND gates.

    Args:
        a: The first input bit.
        b: The second input bit.

    Returns:
        The output bit of the XOR gate.

    Examples:
        >>> xor_gate(0, 0)
        0
        >>> xor_gate(0, 1)
        1
        >>> xor_gate(1, 0)
        1
        >>> xor_gate(1, 1)
        0
    """
    ab = nand_gate(a, b)
    return nand_gate(nand_gate(a, ab), nand_gate(b, ab))


def mux(a: int, b: int, sel: int) -> int:
    """Implements a multiplexer using NAND gates.

    Args:
        a: The first input bit.
        b: The second input bit.
        sel: The select bit.

    Returns:
        The output bit of the multiplexer.

    Examples:
        >>> mux(0, 1, 0)
        0
        >>> mux(0, 1, 1)
        1
        >>> mux(1, 0, 0)
        1
        >>> mux(1, 0, 1)
        0
    """
    return nand_gate(nand_gate(nand_gate(sel, sel), a), nand_gate(sel, b))


def dmux(a: int, sel: int) -> tuple[int, int]:
    """Implements a demultiplexer using NAND gates.

    Args:
        a: The input bit.
        sel: The select bit.

    Returns:
        A tuple containing the two output bits of the demultiplexer.

    Examples:
        >>> dmux(0, 0)
        (0, 0)
        >>> dmux(0, 1)
        (0, 0)
        >>> dmux(1, 0)
        (1, 0)
        >>> dmux(1, 1)
        (0, 1)
    """
    nsela = nand_gate(nand_gate(sel, sel), a)
    sela = nand_gate(sel, a)
    return nand_gate(nsela, nsela), nand_gate(sela, sela)


def not16(a: list[int]) -> list[int]:
    """Performs a bitwise NOT operation on a 16-bit input.

    Args:
        a: A list of 16 integers representing the input.

    Returns:
        A list of 16 integers representing the output.

    Example:
        >>> not16([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    return [not_gate(a[i]) for i in range(16)]


def and16(a: list[int], b: list[int]) -> list[int]:
    """Performs a bitwise AND operation on two 16-bit inputs.

    Args:
        a: A list of 16 integers representing the first input.
        b: A list of 16 integers representing the second input.

    Returns:
        A list of 16 integers representing the output.

    Example:
        >>> and16([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    return [and_gate(a[i], b[i]) for i in range(16)]


def or16(a: list[int], b: list[int]) -> list[int]:
    """Performs a bitwise OR operation on two 16-bit inputs.

    Args:
        a: A list of 16 integers representing the first input.
        b: A list of 16 integers representing the second input.

    Returns:
        A list of 16 integers representing the output.

    Example:
        >>> or16([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    return [or_gate(a[i], b[i]) for i in range(16)]


def mux16(a: list[int], b: list[int], sel: int) -> list[int]:
    """Performs a 16-bit multiplexer operation.

    Args:
        a: A list of 16 integers representing the first input.
        b: A list of 16 integers representing the second input.
        sel: The select bit.

    Returns:
        A list of 16 integers representing the output.

    Example:
        >>> mux16([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  1)
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    return [mux(a[i], b[i], sel) for i in range(16)]


def or8way(a: list[int]) -> int:
    """Performs an 8-way OR operation on a list of input bits.

    Args:
        a: A list of 8 integers representing the input bits.

    Returns:
        The output bit of the 8-way OR operation.

    Examples:
        >>> or8way([0, 0, 0, 0, 0, 0, 0, 0])
        0
        >>> or8way([1, 0, 0, 0, 0, 0, 0, 0])
        1
        >>> or8way([0, 1, 0, 0, 0, 0, 0, 0])
        1
        >>> or8way([0, 0, 1, 0, 0, 0, 0, 0])
        1
        >>> or8way([0, 0, 0, 1, 0, 0, 0, 0])
        1
        >>> or8way([0, 0, 0, 0, 1, 0, 0, 0])
        1
        >>> or8way([0, 0, 0, 0, 0, 1, 0, 0])
        1
        >>> or8way([0, 0, 0, 0, 0, 0, 1, 0])
        1
        >>> or8way([0, 0, 0, 0, 0, 0, 0, 1])
        1
        >>> or8way([1, 1, 1, 1, 1, 1, 1, 1])
        1
    """
    out = a[0]
    for i in range(1, len(a)):
        out = or_gate(out, a[i])
    return out


def mux4way16(
    a: list[int], b: list[int], c: list[int], d: list[int], sel: list[int]
) -> tuple[int]:
    """Performs a 4-way 16-bit multiplexer operation.

    Args:
        a: A list of 16 integers representing the first input.
        b: A list of 16 integers representing the second input.
        c: A list of 16 integers representing the third input.
        d: A list of 16 integers representing the fourth input.
        sel: A list of 2 integers representing the select bits.

    Returns:
        A tuple of 16 integers representing the output.

    Example:
        >>> a = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        >>> b = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
        >>> c = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
        >>> d = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        >>> sel = [1, 0]
        >>> mux4way16(a, b, c, d, sel)
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
    """
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
    """Performs an 8-way 16-bit multiplexer operation.

    Args:
        a - h: Lists of 16 integers representing the inputs.
        sel: A list of 3 integers representing the select bits.

    Returns:
        A tuple of 16 integers representing the output.

    Example:
        >>> a = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        >>> b = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
        >>> c = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
        >>> d = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        >>> e = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        >>> f = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
        >>> g = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
        >>> h = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
        >>> sel = [1, 1, 0]
        >>> mux8way16(a, b, c, d, e, f, g, h, sel)
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
    """
    return mux16(
        mux16(mux16(a, b, sel[2]), mux16(c, d, sel[2]), sel[1]),
        mux16(mux16(e, f, sel[2]), mux16(g, h, sel[2]), sel[1]),
        sel[0],
    )


def dmux4way(x, sel: list[int]) -> tuple[int]:
    """Performs a 4-way demultiplexer operation.

    Args:
        x: The input bit.
        sel: A list of 2 integers representing the select bits.

    Returns:
        A tuple of 4 integers representing the outputs.

    Example:
        >>> dmux4way(1, [0, 1])
        (0, 1, 0, 0)
    """
    a0, b0 = dmux(x, sel[0])
    return dmux(a0, sel[1]) + dmux(b0, sel[1])


def dmux8way(x, sel: list[int]) -> tuple[int]:
    """Performs an 8-way demultiplexer operation.

    Args:
        x: The input bit.
        sel: A list of 3 integers representing the select bits.

    Returns:
        A tuple of 8 integers representing the outputs.

    Example:
        >>> dmux8way(1, [1, 0, 1])
        (0, 0, 0, 0, 0, 1, 0, 0)
    """
    a0, b0 = dmux(x, sel[0])
    a00, b00 = dmux(a0, sel[1])
    c00, d00 = dmux(b0, sel[1])
    return dmux(a00, sel[2]) + dmux(b00, sel[2]) + dmux(c00, sel[2]) + dmux(d00, sel[2])


def half_adder(a: int, b: int) -> tuple[int]:
    """Implements a half-adder.

    Args:
        a: The first input bit.
        b: The second input bit.

    Returns:
        A tuple containing the sum and carry bits of the half-adder.

    Examples:
        >>> half_adder(0, 0)
        (0, 0)
        >>> half_adder(0, 1)
        (1, 0)
        >>> half_adder(1, 0)
        (1, 0)
        >>> half_adder(1, 1)
        (0, 1)
    """
    sum = xor_gate(a, b)
    carry = and_gate(a, b)
    return sum, carry


def full_adder(a: int, b: int, c: int) -> tuple[int]:
    """Implements a full-adder.

    Args:
        a: The first input bit.
        b: The second input bit.
        c: The carry-in bit.

    Returns:
        A tuple containing the sum and carry bits of the full-adder.

    Examples:
        >>> full_adder(0, 0, 0)
        (0, 0)
        >>> full_adder(0, 0, 1)
        (1, 0)
        >>> full_adder(1, 0, 0)
        (1, 0)
        >>> full_adder(1, 0, 1)
        (0, 1)
        >>> full_adder(0, 1, 1)
        (0, 1)
        >>> full_adder(1, 1, 0)
        (0, 1)
        >>> full_adder(1, 1, 1)
        (1, 1)
    """
    ab, cab = half_adder(a, b)
    sum, s = half_adder(c, ab)
    carry = or_gate(cab, s)
    return sum, carry


# In binary addition, we start from the least significant bit (LSB)
# and propagate the carry to the more significant bits. This is because
# the carry from a previous bit can affect the sum of the current bit.
# That is why we move from the end of the inputs to the start as we add.
#
# NOTE: The highest number you can make in binary with a length of 16 is 2^16 - 1.
#       This is equivalent to 65,535 in decimal.
#
def add16(a: list[int], b: list[int]) -> list[int]:
    """Performs a 16-bit addition operation on two lists of integers.

    Args:
        a: A list of 16 integers representing the first operand.
        b: A list of 16 integers representing the second operand.

    Returns:
        A list of 16 integers representing the sum.

    Example:
        >>> a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        >>> b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        >>> add16(a, b)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    """
    sum15, carry15 = half_adder(a[15], b[15])
    sum14, carry14 = full_adder(a[14], b[14], carry15)
    sum13, carry13 = full_adder(a[13], b[13], carry14)
    sum12, carry12 = full_adder(a[12], b[12], carry13)
    sum11, carry11 = full_adder(a[11], b[11], carry12)
    sum10, carry10 = full_adder(a[10], b[10], carry11)
    sum9, carry9 = full_adder(a[9], b[9], carry10)
    sum8, carry8 = full_adder(a[8], b[8], carry9)
    sum7, carry7 = full_adder(a[7], b[7], carry8)
    sum6, carry6 = full_adder(a[6], b[6], carry7)
    sum5, carry5 = full_adder(a[5], b[5], carry6)
    sum4, carry4 = full_adder(a[4], b[4], carry5)
    sum3, carry3 = full_adder(a[3], b[3], carry4)
    sum2, carry2 = full_adder(a[2], b[2], carry3)
    sum1, carry1 = full_adder(a[1], b[1], carry2)
    sum0, _ = full_adder(a[0], b[0], carry1)
    return [
        sum0,
        sum1,
        sum2,
        sum3,
        sum4,
        sum5,
        sum6,
        sum7,
        sum8,
        sum9,
        sum10,
        sum11,
        sum12,
        sum13,
        sum14,
        sum15,
    ]


def inc16(a: list[int]) -> list[int]:
    """Increments a 16-bit integer represented as a list of integers by 1.

    Args:
        a: A list of 16 integers representing the input.

    Returns:
        A list of 16 integers representing the incremented value.

    Example:
        >>> inc16([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    """
    one = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    return add16(a, one)

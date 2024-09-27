import pytest
from chips import (
    nand_gate,
    and_gate,
    not_gate,
    or_gate,
    xor_gate,
    mux,
    dmux,
    not16,
    and16,
    or16,
    mux16,
)


def test_nand_gate():
    assert nand_gate(0, 0) == 1
    assert nand_gate(0, 1) == 1
    assert nand_gate(1, 0) == 1
    assert nand_gate(1, 1) == 0


def test_and_gate():
    assert and_gate(0, 0) == 0
    assert and_gate(0, 1) == 0
    assert and_gate(1, 0) == 0
    assert and_gate(1, 1) == 1


def test_not_gate():
    assert not_gate(0) == 1
    assert not_gate(1) == 0


def test_or_gate():
    assert or_gate(0, 0) == 0
    assert or_gate(0, 1) == 1
    assert or_gate(1, 0) == 1
    assert or_gate(1, 1) == 1


def test_xor_gate():
    assert xor_gate(0, 0) == 0
    assert xor_gate(1, 0) == 1
    assert xor_gate(0, 1) == 1
    assert xor_gate(1, 1) == 0


def test_mux():
    assert mux(0, 0, 0) == 0
    assert mux(0, 0, 1) == 0
    assert mux(0, 1, 0) == 1
    assert mux(0, 1, 1) == 0
    assert mux(1, 0, 0) == 0
    assert mux(1, 0, 1) == 1
    assert mux(1, 1, 0) == 1
    assert mux(1, 1, 1) == 1


def test_dmux():
    assert dmux(0, 0) == (0, 0)
    assert dmux(0, 1) == (1, 0)
    assert dmux(1, 0) == (0, 0)
    assert dmux(1, 1) == (0, 1)


@pytest.mark.parametrize(
    "a, expected",
    [
        ([0] * 16, [1] * 16),
        ([1] * 16, [0] * 16),
        (
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
        ),
    ],
)
def test_not16(a, expected):
    assert not16(a) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([0] * 16, [1] * 16, [0] * 16),
        ([1] * 16, [1] * 16, [1] * 16),
        (
            [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        ),
    ],
)
def test_and16(a, b, expected):
    assert and16(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([0] * 16, [1] * 16, [1] * 16),
        (
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        ),
        (
            [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        ),
    ],
)
def test_or16(a, b, expected):
    assert or16(a, b) == expected


@pytest.mark.parametrize(
    "a, b, sel, expected",
    [
        ([0] * 16, [0] * 16, 0, [0] * 16),
        ([0] * 16, [0] * 16, 1, [0] * 16),
        ([0] * 16, [1] * 16, 0, [1] * 16),
        ([0] * 16, [1] * 16, 1, [0] * 16),
        ([1] * 16, [0] * 16, 0, [0] * 16),
        ([1] * 16, [0] * 16, 1, [1] * 16),
        ([1] * 16, [1] * 16, 0, [1] * 16),
        ([1] * 16, [1] * 16, 1, [1] * 16),
    ],
)
def test_mux16(a, b, sel, expected):
    assert mux16(a, b, sel) == expected


if __name__ == "__main__":
    pytest.main()

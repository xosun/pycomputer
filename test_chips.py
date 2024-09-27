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
    or8way,
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
    "x, expected",
    [
        ([0] * 16, [1] * 16),
        ([1] * 16, [0] * 16),
        (
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
        ),
    ],
)
def test_not16(x, expected):
    assert not16(x) == expected


@pytest.mark.parametrize(
    "x, y, expected",
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
def test_and16(x, y, expected):
    assert and16(x, y) == expected


@pytest.mark.parametrize(
    "x, y, expected",
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
def test_or16(x, y, expected):
    assert or16(x, y) == expected


@pytest.mark.parametrize(
    "x, y, sel, expected",
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
def test_mux16(x, y, sel, expected):
    assert mux16(x, y, sel) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        ([0, 0, 0, 0, 0, 0, 0, 0], 0),
        ([1, 0, 0, 0, 0, 0, 0, 0], 1),
        ([0, 1, 0, 0, 0, 0, 0, 0], 1),
        ([0, 0, 1, 0, 0, 0, 0, 0], 1),
        ([0, 0, 0, 1, 0, 0, 0, 0], 1),
        ([0, 0, 0, 0, 1, 0, 0, 0], 1),
        ([0, 0, 0, 0, 0, 1, 0, 0], 1),
        ([0, 0, 0, 0, 0, 0, 1, 0], 1),
        ([0, 0, 0, 0, 0, 0, 0, 1], 1),
        ([1, 1, 1, 1, 1, 1, 1, 1], 1),
        ([1, 0, 1, 0, 1, 0, 1, 0], 1),
        ([0, 1, 0, 1, 0, 1, 0, 1], 1),
    ],
)
def test_or8way(x, expected):
    assert or8way(x) == expected


if __name__ == "__main__":
    pytest.main()

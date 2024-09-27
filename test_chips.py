import csv
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
    mux4way16,
)


def read_csv_data(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        return [
            [
                [int(bit) for bit in value] if len(value) > 1 else int(value)
                for _, value in row.items()
            ]
            for row in reader
        ]


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
    assert mux(0, 1, 0) == 0
    assert mux(0, 1, 1) == 1
    assert mux(1, 0, 0) == 1
    assert mux(1, 0, 1) == 0
    assert mux(1, 1, 0) == 1
    assert mux(1, 1, 1) == 1


def test_dmux():
    assert dmux(0, 0) == (0, 0)
    assert dmux(0, 1) == (1, 0)
    assert dmux(1, 0) == (0, 0)
    assert dmux(1, 1) == (0, 1)


@pytest.mark.parametrize("a, out", read_csv_data("not16.csv"))
def test_not16(a, out):
    assert not16(a) == out


@pytest.mark.parametrize("a, b, out", read_csv_data("and16.csv"))
def test_and16(a, b, out):
    assert and16(a, b) == out


@pytest.mark.parametrize("a, b, out", read_csv_data("or16.csv"))
def test_or16(a, b, out):
    assert or16(a, b) == out


@pytest.mark.parametrize("a, b, sel, out", read_csv_data("mux16.csv"))
def test_mux16(a, b, sel, out):
    assert mux16(a, b, sel) == out


@pytest.mark.parametrize("a, out", read_csv_data("or8way.csv"))
def test_or8way(a, out):
    assert or8way(a) == out


@pytest.mark.parametrize("a, b, c, d, sel, out", read_csv_data("mux4way16.csv"))
def test_mux4way16(a, b, c, d, sel, out):
    assert mux4way16(a, b, c, d, sel) == out


if __name__ == "__main__":
    pytest.main()

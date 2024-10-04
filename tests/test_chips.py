import os
import csv
import pytest
from src.chips import (
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
    mux8way16,
    dmux4way,
    dmux8way,
    half_adder,
    full_adder,
    add16,
    inc16,
    alu,
    sr_latch,
)


def read_csv_data(csv_file):
    TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), "test_data")
    with open(os.path.join(TEST_DATA_PATH, "truth_tables", csv_file), "r") as file:
        reader = csv.DictReader(file)
        return [
            [
                [int(bit) for bit in value] if len(value) > 1 else int(value)
                for _, value in row.items()
            ]
            for row in reader
        ]


@pytest.mark.parametrize("a, b, out", read_csv_data("nand.csv"))
def test_nand_gate(a, b, out):
    assert nand_gate(a, b) == out


@pytest.mark.parametrize("a, b, out", read_csv_data("and.csv"))
def test_and_gate(a, b, out):
    assert and_gate(a, b) == out


@pytest.mark.parametrize("a, out", read_csv_data("not.csv"))
def test_not_gate(a, out):
    assert not_gate(a) == out


@pytest.mark.parametrize("a, b, out", read_csv_data("or.csv"))
def test_or_gate(a, b, out):
    assert or_gate(a, b) == out


@pytest.mark.parametrize("a, b, out", read_csv_data("xor.csv"))
def test_xor_gate(a, b, out):
    assert xor_gate(a, b) == out


@pytest.mark.parametrize("a, b, sel, out", read_csv_data("mux.csv"))
def test_mux(a, b, sel, out):
    assert mux(a, b, sel) == out


@pytest.mark.parametrize("x, sel, a, b", read_csv_data("dmux.csv"))
def test_dmux(x, sel, a, b):
    assert dmux(x, sel) == (a, b)


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


@pytest.mark.parametrize(
    "a, b, c, d, e, f, g, h, sel, out", read_csv_data("mux8way16.csv")
)
def test_mux8way16(a, b, c, d, e, f, g, h, sel, out):
    assert mux8way16(a, b, c, d, e, f, g, h, sel) == out


@pytest.mark.parametrize("x, sel, a, b, c, d", read_csv_data("dmux4way.csv"))
def test_dmux4way(x, sel, a, b, c, d):
    assert dmux4way(x, sel) == (a, b, c, d)


@pytest.mark.parametrize(
    "x, sel, a, b, c, d, e, f, g, h", read_csv_data("dmux8way.csv")
)
def test_dmux8way(x, sel, a, b, c, d, e, f, g, h):
    assert dmux8way(x, sel) == (a, b, c, d, e, f, g, h)


@pytest.mark.parametrize("a, b, sum, carry", read_csv_data("half_adder.csv"))
def test_half_adder(a, b, sum, carry):
    assert half_adder(a, b) == (sum, carry)


@pytest.mark.parametrize("a, b, c, sum, carry", read_csv_data("full_adder.csv"))
def test_full_adder(a, b, c, sum, carry):
    assert full_adder(a, b, c) == (sum, carry)


@pytest.mark.parametrize("a, b, out", read_csv_data("add16.csv"))
def test_add16(a, b, out):
    assert add16(a, b) == out


@pytest.mark.parametrize("a, out", read_csv_data("inc16.csv"))
def test_add16(a, out):
    assert inc16(a) == out


@pytest.mark.parametrize(
    "x, y, zx, nx, zy, ny, f, no, out, zr, ng", read_csv_data("alu.csv")
)
def test_alu(x, y, zx, nx, zy, ny, f, no, out, zr, ng):
    assert alu(x, y, zx, nx, zy, ny, f, no) == (out, zr, ng)


@pytest.mark.parametrize("s, r, q_before, q_after", read_csv_data("sr_latch.csv"))
def test_sr_latch(s, r, q_before, q_after):
    if s == 1 and r == 1:
        with pytest.raises(ValueError):
            assert sr_latch(s, r, q_before) == q_after
    else:
        assert sr_latch(s, r, q_before) == q_after


if __name__ == "__main__":
    pytest.main()

import pytest
from logic_gates import (
    nand_gate,
    and_gate,
    not_gate,
    or_gate,
    xor_gate,
    mux_circuit,
    dmux_circuit,
    not16,
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


def test_mux_circuit():
    assert mux_circuit(0, 0, 0) == 0
    assert mux_circuit(0, 0, 1) == 0
    assert mux_circuit(0, 1, 0) == 1
    assert mux_circuit(0, 1, 1) == 0
    assert mux_circuit(1, 0, 0) == 0
    assert mux_circuit(1, 0, 1) == 1
    assert mux_circuit(1, 1, 0) == 1
    assert mux_circuit(1, 1, 1) == 1


def test_dmux_circuit():
    assert dmux_circuit(0, 0) == (0, 0)
    assert dmux_circuit(0, 1) == (1, 0)
    assert dmux_circuit(1, 0) == (0, 0)
    assert dmux_circuit(1, 1) == (0, 1)


def test_not16():
    expected_io = [
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ],
        [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
        [
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        ],
        [
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
        ],
        [
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
        ],
    ]
    assert not16(expected_io[0][0]) == expected_io[0][1]
    assert not16(expected_io[1][0]) == expected_io[1][1]
    assert not16(expected_io[2][0]) == expected_io[2][1]
    assert not16(expected_io[3][0]) == expected_io[3][1]
    assert not16(expected_io[4][0]) == expected_io[4][1]


@pytest.mark.parametrize(
    "input_data, expected_error",
    [
        ([0] * 15, "Input list must be exactly 16 integers long"),
        ([0] * 17, "Input list must be exactly 16 integers long"),
    ],
)
def test_invalid_not16_length(input_data, expected_error):
    with pytest.raises(ValueError) as excinfo:
        not16(input_data)
    assert str(excinfo.value) == expected_error


if __name__ == "__main__":
    pytest.main()

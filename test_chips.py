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
    ]
    assert not16(expected_io[0][0]) == expected_io[0][1]
    assert not16(expected_io[1][0]) == expected_io[1][1]
    assert not16(expected_io[2][0]) == expected_io[2][1]


def test_and16():
    expected_io = [
        [
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
        ],
        [
            [
                [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
        ],
        [
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
        ],
    ]
    assert and16(expected_io[0][0][0], expected_io[0][0][1]) == expected_io[0][1][0]
    assert and16(expected_io[1][0][0], expected_io[1][0][1]) == expected_io[1][1][0]
    assert and16(expected_io[2][0][0], expected_io[2][0][1]) == expected_io[2][1][0]


def test_or16():
    expected_io = [
        [
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
        ],
        [
            [
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            ],
            [
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            ],
        ],
        [
            [
                [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            [
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            ],
        ],
    ]
    assert or16(expected_io[0][0][0], expected_io[0][0][1]) == expected_io[0][1][0]
    assert or16(expected_io[1][0][0], expected_io[1][0][1]) == expected_io[1][1][0]
    assert or16(expected_io[2][0][0], expected_io[2][0][1]) == expected_io[2][1][0]


@pytest.fixture(params=[15, 17])
def invalid_length(request):
    return request.param


def assert_invalid_length(func, length: int):
    with pytest.raises(ValueError) as excinfo:
        func([0] * length)
    assert str(excinfo.value) == "Input list must be exactly 16 integers long"


def assert_invalid_length_x2(func, length: int):
    with pytest.raises(ValueError) as excinfo:
        func([0] * length, [0] * length)
    assert str(excinfo.value) == "Input list must be exactly 16 integers long"


@pytest.mark.usefixtures("invalid_length")
def test_not16_invalid_length(invalid_length):
    assert_invalid_length(not16, invalid_length)


@pytest.mark.usefixtures("invalid_length")
def test_and16_invalid_length(invalid_length):
    assert_invalid_length_x2(and16, invalid_length)


@pytest.mark.usefixtures("invalid_length")
def test_or16_invalid_length(invalid_length):
    assert_invalid_length_x2(or16, invalid_length)


if __name__ == "__main__":
    pytest.main()

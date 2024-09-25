import unittest
from logic_gates import (
    nand_gate,
    and_gate,
    not_gate,
    or_gate,
    xor_gate,
    mux_circuit,
    dmux_circuit,
)


class TestLogicGates(unittest.TestCase):
    def test_nand_gate(self):
        self.assertEqual(nand_gate(0, 0), 1)
        self.assertEqual(nand_gate(0, 1), 1)
        self.assertEqual(nand_gate(1, 0), 1)
        self.assertEqual(nand_gate(1, 1), 0)

    def test_and_gate(self):
        self.assertEqual(and_gate(0, 0), 0)
        self.assertEqual(and_gate(0, 1), 0)
        self.assertEqual(and_gate(1, 0), 0)
        self.assertEqual(and_gate(1, 1), 1)

    def test_not_gate(self):
        self.assertEqual(not_gate(0), 1)
        self.assertEqual(not_gate(1), 0)

    def test_or_gate(self):
        self.assertEqual(or_gate(0, 0), 0)
        self.assertEqual(or_gate(0, 1), 1)
        self.assertEqual(or_gate(1, 0), 1)
        self.assertEqual(or_gate(1, 1), 1)

    def test_xor_gate(self):
        self.assertEqual(xor_gate(0, 0), 0)
        self.assertEqual(xor_gate(1, 0), 1)
        self.assertEqual(xor_gate(0, 1), 1)
        self.assertEqual(xor_gate(1, 1), 0)

    def test_mux_circuit(self):
        self.assertEqual(mux_circuit(0, 0, 0), 0)
        self.assertEqual(mux_circuit(0, 0, 1), 0)
        self.assertEqual(mux_circuit(0, 1, 0), 1)
        self.assertEqual(mux_circuit(0, 1, 1), 0)
        self.assertEqual(mux_circuit(1, 0, 0), 0)
        self.assertEqual(mux_circuit(1, 0, 1), 1)
        self.assertEqual(mux_circuit(1, 1, 0), 1)
        self.assertEqual(mux_circuit(1, 1, 1), 1)

    def test_dmux_circuit(self):
        print(dmux_circuit(0, 0), [0, 0])
        print(dmux_circuit(0, 1), [1, 0])
        print(dmux_circuit(1, 0), [0, 0])
        print(dmux_circuit(1, 1), [0, 1])


if __name__ == "__main__":
    unittest.main()

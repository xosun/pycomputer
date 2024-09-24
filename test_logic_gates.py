import unittest
from logic_gates import nand_gate, and_gate, not_gate, or_gate


class TestNandGate(unittest.TestCase):
    def test_nand_gate_both_false(self):
        self.assertEqual(nand_gate(0, 0), 1)

    def test_nand_gate_one_false(self):
        self.assertEqual(nand_gate(0, 1), 1)
        self.assertEqual(nand_gate(1, 0), 1)

    def test_nand_gate_both_true(self):
        self.assertEqual(nand_gate(1, 1), 0)


class TestAndGate(unittest.TestCase):
    def test_and_gate_both_false(self):
        self.assertEqual(and_gate(0, 0), 0)

    def test_and_gate_one_false(self):
        self.assertEqual(and_gate(0, 1), 0)
        self.assertEqual(and_gate(1, 0), 0)

    def test_and_gate_both_true(self):
        self.assertEqual(and_gate(1, 1), 1)


class TestNotGate(unittest.TestCase):
    def test_not_gate_0(self):
        self.assertEqual(not_gate(0), 1)

    def test_not_gate_1(self):
        self.assertEqual(not_gate(1), 0)


class TestOrGate(unittest.TestCase):
    def test_or_gate_both_false(self):
        self.assertEqual(or_gate(0, 0), 0)

    def test_or_gate_one_false(self):
        self.assertEqual(or_gate(1, 0), 1)
        self.assertEqual(or_gate(0, 1), 1)

    def test_or_gate_both_true(self):
        self.assertEqual(or_gate(1, 1), 1)


if __name__ == "__main__":
    unittest.main()
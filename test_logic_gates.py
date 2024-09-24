import unittest
from logic_gates import nand_gate, and_gate, not_gate, or_gate


class TestNandGate(unittest.TestCase):
    def test_nand_gate_all_false(self):
        self.assertEqual(nand_gate(0, 0), 1)

    def test_nand_gate_one_false(self):
        self.assertEqual(nand_gate(0, 1), 1)
        self.assertEqual(nand_gate(1, 0), 1)

    def test_nand_gate_both_true(self):
        self.assertEqual(nand_gate(1, 1), 0)


class TestAndGate(unittest.TestCase):
    def test_both_inputs_0(self):
        result = and_gate(0, 0)
        self.assertEqual(result, 0)

    def test_one_input_0(self):
        result = and_gate(0, 1)
        self.assertEqual(result, 0)

        result = and_gate(1, 0)
        self.assertEqual(result, 0)

    def test_both_inputs_1(self):
        result = and_gate(1, 1)
        self.assertEqual(result, 1)


class TestNotGate(unittest.TestCase):
    def test_input_0(self):
        result = not_gate(0)
        self.assertEqual(result, 1)

    def test_input_1(self):
        result = not_gate(1)
        self.assertEqual(result, 0)


class TestOrGate(unittest.TestCase):
    def test_both_inputs_0(self):
        result = or_gate(0, 0)
        self.assertEqual(result, 0)

    def test_one_input_0(self):
        result = or_gate(1, 0)
        self.assertEqual(result, 1)

        result = or_gate(0, 1)
        self.assertEqual(result, 1)

    def test_both_inputs_1(self):
        result = or_gate(1, 1)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()

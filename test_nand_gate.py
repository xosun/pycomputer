import unittest
from logic_gates import nand_gate

class TestNandGate(unittest.TestCase):
    def test_nand_gate_all_false(self):
        self.assertEqual(nand_gate(False, False), True)

    def test_nand_gate_one_false(self):
        self.assertEqual(nand_gate(False, True), True)
        self.assertEqual(nand_gate(True, False), True)

    def test_nand_gate_both_true(self):
        self.assertEqual(nand_gate(True, True), False)

if __name__ == '__main__':
    unittest.main()

import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_parse_input_correctly(self):
        input = """MMAMMMSAXAXXAXMASMMASAMXMAMMAMXXXXXSMSXMMMXMXXSXASAMXMAMMXSAMXXXXMSSMXMASMMMSMSSSSSXMXSASMSMMMMMXAMXAXMMSMMAXSSSXSXMXAMXMXSXSMSSXSAMXXXMXMXM
ASASAAMXMXMMMXAXAXSSMXSASASMSSXMMSMMSAMXMMSSMASAMXMXMMMSMMMASMXSAMAMMXMAMAAXAAXAAAAMMSAMXAAXAASMSSSMSSSMAAMXMAAXMMASMSSMMXMAXAAAASAMXSXMASAM
MSASMSSMMAAASMXSMMXAAMSAMASAAAMAAAASXMAXSAAAMSMMXAMAMAMAXAXAXAASMMAMMXMASXMSMSMMMMMAXMASMXMSXXMAAXAAAAASXMMAAMSMMSAMXAAXXAMXMMMSMSASAAASASXS
MMAMAXMASMSXXMASXMMMMMMMMMMMMXAXSMXMAMXXMMSSMMAMMAXXSASXSXMAMMMMXSMSMXXAMAASAMMXMASXXXXSXMMXMSMMMSMMMSMMSASMMXAAXAASMSMMSXSAXAAMXSAMMSMMASAA"""
        output = solution.parse_input(input)
        self.assertEqual(len(output), 4)
        for row in output:
            self.assertEqual(len(row), 140)
            
    def test_find_horizontal_forward(self):
        inputs = [
            """XMAS
XXXX
XXXX
XXXX""", 
            """XXMAS
XXXXX
XXXXX
XXXXX""", 
            """XMASS
XXXXX
XXXXX
XXXXX""", 
            """XXMASS
XXXXXX
XXXXXX
XXXXXX""",
            """XXXX
XMAS
XXXX
XXXX""", 
"""XXXX
XXXX
XMAS
XXXX""",
            """XXXX
XXXX
XXXX
XMAS""",
            """XMAS
XMAS
XMAS
XMAS""",
            """XMASXMAS
XXXXXXXX
XXXXXXXX
XXXXXXXX""",
            """XMASXXMASXXMAS
XXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXX""",
            """XMXAS
XMAXS
XMAAS"""
        ]
        matches = 0
        for input in inputs:
            parsed_input = solution.parse_input(input)
            matches += solution.find_xmas(parsed_input)
        self.assertEqual(matches, 16)
    
    def test_find_horizontal_backward(self):
        inputs = [
            """SAMX
XXXX
XXXX
XXXX""", 
            """XSAMX
XXXXX
XXXXX
XXXXX""", 
            """SAMXS
XXXXX
XXXXX
XXXXX""", 
            """XSAMXS
XXXXXX
XXXXXX
XXXXXX""",
            """XXXX
SAMX
XXXX
XXXX""", 
"""XXXX
XXXX
SAMX
XXXX""",
            """XXXX
XXXX
XXXX
SAMX""",
            """SAMX
SAMX
SAMX
SAMX""",
            """SAMXSAMX
XXXXXXXX
XXXXXXXX
XXXXXXXX""",
            """SAMXXSAMXXSAMX
XXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXX""",
            """SAAMX
SAXMX
SXAMX"""
        ]
        matches = 0
        for input in inputs:
            parsed_input = solution.parse_input(input)
            matches += solution.find_xmas(parsed_input)
        self.assertEqual(matches, 16)

if __name__ == "__main__":
    unittest.main()
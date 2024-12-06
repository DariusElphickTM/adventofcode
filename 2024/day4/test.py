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
        self.assertEqual(matches, 18)
    
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
        self.assertEqual(matches, 18)
    
    def test_find_vertical_down(self):
        inputs = [
            """XXXX
MXXX
AXXX
SXXX""", 
            """XXXXX
XXXXX
MXXXX
AXXXX
SXXXX""", 
            """XXXXX
MXXXX
AXXXX
SXXXX
SXXXX""", 
            """XXXXXX
MXXXXX
AXXXXX
SXXXXX
SXXXXX""",
            """XXXX
XMXX
XAXX
XSXX""", 
"""XXXX
XXMX
XXAX
XXSX""",
            """XXXX
XXXM
XXXA
XXXS""",
            """XXXX
MMMM
AAAA
SSSS""",
            """XXXX
MMMM
AAAA
SSSS
XXXX
MMMM
AAAA
SSSS""",
            """XXXX
MMMM
AAAA
SSSS
XXXX
XXXX
MMMM
AAAA
SSSS
XXXX
XXXX
MMMM
AAAA
SSSS"""
        ]
        matches = 0
        for input in inputs:
            parsed_input = solution.parse_input(input)
            matches += solution.find_xmas(parsed_input)
        self.assertEqual(matches, 43)
    
    def test_find_vertical_up(self):
        inputs = [
            """SXXX
AXXX
MXXX
XXXX""", 
            """SXXXX
AXXXX
MXXXX
XXXXX
XXXXX""", 
            """SXXXX
SXXXX
AXXXX
MXXXX
XXXXX""",
            """XSXX
XAXX
XMXX
XXXX""", 
"""XXSX
XXAX
XXMX
XXXX""",
            """XXXS
XXXA
XXXM
XXXX""",
            """SSSS
AAAA
MMMM
XXXX""",
            """SSSS
AAAA
MMMM
XXXX
SSSS
AAAA
MMMM
XXXX""",
            """SSSS
AAAA
MMMM
XXXX
XXXX
SSSS
AAAA
MMMM
XXXX
XXXX
SSSS
AAAA
MMMM
XXXX"""
        ]
        matches = 0
        for input in inputs:
            parsed_input = solution.parse_input(input)
            matches += solution.find_xmas(parsed_input)
        self.assertEqual(matches, 42)
    
    def test_find_diagonals(self):
        inputs = [
            """XXXX
XMXX
XXAX
XXXS""",
"""XXXX
XXMX
XAXX
SXXX""",
"""XXXS
XXAX
XMXX
XXXX""",
"""SXXX
XAXX
XXMX
XXXX""",
"""XXXXXX
XXXXXX
XXMXXX
XXXAXX
XXXXSX
XXXXXX""",
"""XXXXXX
XXXXXX
XXXMXX
XXAXXX
XSXXXX
XXXXXX""",
"""
XXXXXX
XXXXSX
XXXAXX
XXMXXX
XXXXXX
XXXXXX""",
"""XXXXXX
XSXXXX
XXAXXX
XXXMXX
XXXXXX
XXXXXX"""
        ]
        matches = 0
        for input in inputs:
            parsed_input = solution.parse_input(input)
            matches += solution.find_xmas(parsed_input)
        self.assertEqual(matches, 8)
    
    def test_find_grid(self):
        inputs = [
"""XXXXXXXXX
XSXXSXXSX
XXAXAXAXX 
XXXMMMXXX
XSAMXMASX
XXXMMMXXX
XXAXAXAXX
XSXXSXXSX
XXXXXXXXX
"""
        ]
        matches = 0
        for input in inputs:
            parsed_input = solution.parse_input(input)
            matches += solution.find_xmas(parsed_input)
        self.assertEqual(matches, 8)

if __name__ == "__main__":
    unittest.main()
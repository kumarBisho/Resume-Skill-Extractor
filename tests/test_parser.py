import unittest
from app.parser import parse_resume

class TestParser(unittest.TestCase):
    def test_parse_resume(self):
        # Add test logic
        result = parse_resume(None)
        self.assertIn("skills", result)

if __name__ == '__main__':
    unittest.main()

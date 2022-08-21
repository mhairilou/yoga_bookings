import unittest

from models.session import Session


class TestSession(unittest.TestCase):
    
    def setUp(self):
        self.session1 = Session("Hatha", 60)
        self.session2 = Session("Yin", 75)
        self.session3 = Session("Vinyasa", 45)

        
    def test_session_has_type(self):
        result = self.session1.yoga_type
        self.assertEqual("Hatha", result)

    
import unittest

from models.student import Student


class TestStudent(unittest.TestCase):
    
    def setUp(self):
        self.student1 = Student("Woody", "The Dog", 2)
        
    def test_student_has_first_name(self):
        result = self.student1.first_name
        self.assertEqual("Woody", result)

    def test_student_has_last_name(self):
        result = self.student1.last_name
        self.assertEqual("The Dog", result)
    
    def test_student_has_credits(self):
        result = self.student1.credits
        self.assertEqual(2, result)   

    def test_student_full_name(self):
        result = self.student1.full_name()
        self.assertEqual("Woody The Dog", result) 
        
class Student:

    def __init__(self, first_name, last_name, credits, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.credits = credits
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # def get_student_by_name(self, name):
    #    result =  self.full_name()
    #    if name == result:
    #     return s

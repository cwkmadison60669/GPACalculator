class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = {}
    def courses(self, name, grades, credits):

        self.courses[name] = (credits, grades)

    def Calculator(self, grade, GPA):

        self.Calculator
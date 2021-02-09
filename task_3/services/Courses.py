class Courses():
    def __init__(self, course_name: list, teacher_name: str):
        self._course = course_name
        self._name = teacher_name

    def course_list(self):
        return f"{self._course}"
    
    def course_assigned(self):
        return f"{self._course}, {self._name}"
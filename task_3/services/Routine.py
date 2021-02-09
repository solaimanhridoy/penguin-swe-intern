class Routine():
    
    def __init__(self, dayIndex:list, hourIndex:list, courseIndex:list):
        # super().__init__(course_name, teacher_name)
        self.day = dayIndex
        self.hour = hourIndex
        self.course = courseIndex
        
    def show_routine(self):
        courses = ["English Grammar", "Mathematics", "Physics", "Chemistry", "Biology"]
        for (i, j, k) in zip(self.day, self.hour, self.course):
            print(i + " " + j + " " + courses[int(k)])
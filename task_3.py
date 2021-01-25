class Courses():
    def __init__(self, course_name: list, teacher_name: str):
        self.course = course_name
        self.name = teacher_name

    def course_list(self):
        return f"{self.course}"
    
    def course_assigned(self):
        return f"{self.course}, {self.name}"
    
class Routine():
    
    def __init__(self, dayIndex:list, hourIndex:list, courseIndex:list):
        # super().__init__(course_name, teacher_name)
        self.day = dayIndex
        self.hour = hourIndex
        self.course = courseIndex
        
    def show_routine(self):
        courses = ["English Grammar", "Mathmetics", "Physics", "Chemistry", "Biology"]
        for (i, j, k) in zip(self.day, self.hour, self.course):
            print(i + " " + j + " " + courses[int(k)])

def menu():
    print("A. Create Routine\nB. Show Routine\nC. List Courses with Teachers Name")
    enter = input()

    obj1 = Courses("English Grammar", "John Smith")
    obj2 = Courses("Mathematics", "Lara Gilbert")
    obj3 = Courses("Physics", "Johanna Kabir")
    obj4 = Courses("Chemistry", "Danniel Robertson")
    obj5 = Courses("Biology", "Larry Cooper")
    obj = [obj1, obj2, obj3, obj4, obj5]

    if enter == 'A':
        j = int(1)
        for i in obj:
            print(str(j) + ". " + i.course_list())
            j+=1

        d = [] 
        h = [] 
        c = []
        print("\ndayIndex(0 - 4) hourIndex(0 - 3) courseIndex")
        for i in range(0, 4):
            l, m, p = input().split() 

            d.append(l)
            h.append(m)
            c.append(p)

            i+=1
        tmp = Routine(d, h, c)
        print("A. Create Routine\nB. Show Routine\nC. List Courses with Teachers Name")
        enter = input()
        if enter == 'B':
            print(tmp.show_routine())
            menu()
        else:
            menu()
        

    # tmp = Routine(d, h, c)
    # if enter == 'B':
    #     print("\ndayIndex(0 - 4) hourIndex(0 - 3) courseIndex")
    #     print(tmp.show_routine)

    if enter == 'C':
        for i in obj:
            print(i.course_assigned())
        menu()
 

if __name__ == "__main__":
    menu()
    
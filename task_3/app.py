import services

def main():
    print("A. Create Routine\nB. Show Routine\nC. List Courses with Teachers Name")
    enter = input()

    obj1 = services.Courses("English Grammar", "John Smith")
    obj2 = services.Courses("Mathematics", "Lara Gilbert")
    obj3 = services.Courses("Physics", "Johanna Kabir")
    obj4 = services.Courses("Chemistry", "Danniel Robertson")
    obj5 = services.Courses("Biology", "Larry Cooper")
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
        tmp = services.Routine(d, h, c)
        print("A. Create Routine\nB. Show Routine\nC. List Courses with Teachers Name")
        enter = input()
        if enter == 'B':
            print(tmp.show_routine())
            main()
        else:
            main()
        

    # tmp = Routine(d, h, c)
    # if enter == 'B':
    #     print("\ndayIndex(0 - 4) hourIndex(0 - 3) courseIndex")
    #     print(tmp.show_routine)

    if enter == 'C':
        for i in obj:
            print(i.course_assigned())
        main()
 

if __name__ == "__main__":
    main()
    

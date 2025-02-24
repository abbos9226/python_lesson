class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    
class Student(Person):
    def __init__(self, name, age, student_id, grades):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades
        
    def average_grade(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0.00

    def __str__(self):
        grade_str = ', '.join(map(str, self.grades))
        return f'{super().__str__()}, Student ID: {self.student_id},Grades: {grade_str}, avg_grades: {self.average_grade():.2f}'


# student1 = Student('John', 24,3, [1, 2, 3, 4])

class StudentCRUDSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        all_id = [s.student_id for s in self.students]
        if student.student_id in all_id:
            print('this id already exists')
        else:
            self.students.append(student)
            print (f'{student.name} has loaded')

    def view_students(self):
        if not self.students:
            print('\nNo students available\n')
            return
        for student in self.students:
            print(student)

    def update_student(self, student_id, name=None, age=None, grades=None):
        student = [student for student in self.students if student.student_id == student_id][0]
        if not name and not age and not grades:
            print('No student updated')
        else:
            if name:
                student.name = name
            if age:
                student.age = age
            if grades:
                student.grades = grades
            
            print(f'\nstudent{name} has been updated\n')

    def check_id(self, student_id):
        all_id = [s.student_id for s in self.students]
        return True if student_id in all_id else False
    
    def delete_students(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]
        print('Student deleted successfully')

    def save_data(self):
        try:
            with open('testing.txt', 'w') as test:
                for student in self.students:
                    grades_string = ', '.join(map(str, student.grades))
                    test.write(f"{student.student_id}|{student.name}|{student.age}|{grades_string}\n")
                print('Successfully loaded')
        except Exception as e:
            print(e)

    def load_from_data(self):
        try:
            with open('testing.txt', 'r') as test:
                for list in test:
                    student_id, name, age, grades = list.strip().split('|')
                    print(student_id, name, age, grades)
        except Exception as e:
            print(e)

# print(student1)


def main():
    crud = StudentCRUDSystem()
    while True:
        print('1. Add the data')
        print('2. See the data')
        print('3. Update the data')
        print('4. Delete the data')
        print('5. Save the data')
        print('6. load from the data')
        print('7. break')

        command = input("Enter your command: ")

        if command =='1':
            name = input('Enter your name: ')
            age = input('Enter your age: ')
            student_id = input('Enter your student id: ')
            grades = list(map(int, input('Enter your grades: (provide grades with space): ').split(' ')))

            student = Student(name, age, student_id, grades)
            crud.add_student(student)

        elif command =='2':
            crud.view_students()

        elif command == '3':
            student_id = input("Enter Student ID that you want to Update: ")
            if crud.check_id(student_id):
                name = input('Enter your New name: ')
                age = int(input('Enter your New age: '))
                grades = list(map(int, input('Enter your grades: (provide grades with space): ').split(' ')))
                crud.update_student(student_id, name or None, age or None, grades or None)
            else:
                print('No student with that ID')
        elif command == '4':
            student_id = input("Enter Student ID that you want to Update: ")
            if crud.check_id(student_id):
                crud.delete_students(student_id)
            else:
                print('not found')
        elif command =='5':
            crud.save_data()
        elif command =='6':
            crud.load_from_data()
        elif command =='7':
            break

main()
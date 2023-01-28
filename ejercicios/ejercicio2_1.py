# Pedimos nombre y edad de alumnos en clase

students = []
how_many = int(input('How many students came to the class: '))

def obtain_students_data(how_many_students):

    for _ in range(how_many_students):
        name = input('What is your name: ')
        age = int(input('how old are you: '))
        student = (name, age)
        students.append(student)


    students.sort(key = lambda x : x[1])
    asistent = students[0][0]
    teacher = students[-1][0]

    return asistent, teacher


asisstent, teacher = obtain_students_data(how_many)

print (f'the assistent is {asisstent} and the teacher is {teacher}')
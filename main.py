#Namedtuple
from collections import namedtuple



# Point =namedtuple('Point', 'x y z')
# p1 = Point(4,6,5)
# print(p1) #Hammasi chiqadi terminalga
# print(p1.y) #Faqat y chiqadi terminalga
# print(p1.x,p1.z) #Faqat x va z chiqadi terminalga
# print(p1.x+p1.y) #X va Z qo'shilgandagi yigindisi chiqadi terminalga





# student =('Omadbek', 18, 'Amity University')
# Student = namedtuple('Student', 'name age university')
# omadbek = Student(name='Omadbek', age=18, university='Amity University')
# print(omadbek) #Hammasi chiqadi terminalga
# print(omadbek.name) #Faqat ismi
# print(omadbek.age) #Faqat yoshi
# print(omadbek.university) #Faqat Universiteti





#Bunda o'zimiz default holatiga malumot berib ketsak boladi

# employee = namedtuple('Employee', 'name age gender', defaults=['25', 'male'])
# john = employee('John')
# print(john) #Hammasi chiqadi terminalga
# print(john.age) #faqat yoshi
# print(john.gender) #jinsi




#Make orali osonroq malumotlarni olamiz list orqali
#
# Person = namedtuple('Person', ['name', 'age', 'height'])
# l1 = ['Dilshod', 17, 1.82]
# dilshod = (Person._make(l1))
# print(dilshod)
# print(dilshod._asdict()) #yokida o'zi joylab beradi





#Db orqaliham qilishimiz mumkun

# Cars = namedtuple('Cars', ['model', 'color', 'year'])
# details = ['Toyota Camry', 'black', 2023]
#
# db = {'model': 'Chevrolet Tahoe', 'color': 'black', 'year': 2024}
# print(Cars(**db))
#
# chevrolet = Cars('Chevrolet Tahoe', 'black', 2023)
# new_car = chevrolet._replace(color='white')
# print(new_car.color)
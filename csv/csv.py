import csv

def function():
    with open("CSV/people.csv","r") as file:
        csv_reader=csv.DictReader(file)

        genc_yas=float("inf")
        name=None

        for user in csv_reader:  
            if yas<genc_yas:
                genc_yas=yas 
                name=user['Name']
        print(f'{name} isimli kişi en gençtir ve yaşı {genc_yas}')

function()


def function1():
    with open("CSV/people.csv", "r") as file:
        csv_reader = csv.DictReader(file)

        yasli_name = None
        meslek = None
        yas = float("-inf")

        for user in csv_reader:
            user_age = int(user['Age'])
            if user_age > yas:
                yas = user_age
                yasli_name = user['Name']
                meslek = user['Occupation']

        print(f"{yasli_name} en yaşlı kişidir ve yaş: {yas}, mesleği: {meslek}")

function1()


def function2():
    with open("CSV/people.csv", "r") as file:
        csv_reader = csv.DictReader(file)

        genc_yas = float("inf")
        name = None
        gender = None
        
        for user in csv_reader:
            user_age = int(user['Age'])
            if user_age < genc_yas:
                genc_yas = user_age
                name = user['Name']
                gender = user['Gender']
        
        print(f"{name} isimli kişinin yaşı {genc_yas} ve cinsiyeti {gender}")

function2()



def function3():
    with open("CSV/people.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        users = list(csv_reader)

        yasli_1 = float("-inf")
        yasli_2 = float("-inf")
        yasli_3 = float("-inf")

        name_1 = None
        name_2 = None
        name_3 = None

        for user in users:
            user_age = int(user['Age'])

            if user_age > yasli_1:
                yasli_3 = yasli_2
                name_3 = name_2
                yasli_2 = yasli_1
                name_2 = name_1
                yasli_1 = user_age
                name_1 = user['Name']

            elif user_age > yasli_2:
                yasli_3 = yasli_2
                name_3 = name_2
                yasli_2 = user_age
                name_2 = user['Name']

            elif user_age > yasli_3:
                yasli_3 = user_age
                name_3 = user['Name']

        sonuc = (yasli_1 + yasli_2 + yasli_3) / 3
        print(f"En yaşlı kişi: {name_1}, yaş: {yasli_1}")
        print(f"İkinci en yaşlı kişi: {name_2}, yaş: {yasli_2}")
        print(f"Üçüncü en yaşlı kişi: {name_3}, yaş: {yasli_3}")
        print(f"Ortalama yaş: {sonuc}")

function3()




def function4():
    with open("CSV/people.csv", "r")  as file:
        csv_reader = csv.DictReader(file)

        old = float("-inf")
        young = float("inf")

        old_name = None
        young_name = None

        for user in csv_reader:
            user_age = int(user['Age'])

            if user_age > old:
                old = user_age
                old_name = user['Name']

            if user_age < young:
                young = user_age
                young_name = user['Name']

        sonuc = old - young

        print(f"{old_name} kişi en yaşlıdır ve yaş {old}")
        print(f"{young_name} kişi en gençtir ve yaş {young}")
        print(f"En genç ve en yaşlı arasındaki yaş farkı: {sonuc}")

function4()






def add_user(id,name,gender,age,country,occupation):
    with open("CSV/people.csv", "a") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow([id,name,gender,age,country,occupation])


a=input("id?")
b=input("name?")
c=input("gender?")
d=input("age?")
e=input("country?")
f=input("occupation?")

add_user(id=a,name=b, gender=c,age=d,country=e,occupation=f)

        
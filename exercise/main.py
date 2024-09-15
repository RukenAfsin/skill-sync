# # students=["John", "Mark", "Venessa", "Mariam"]

# # students_no=["John", "Venessa"]


# # [student.lower()  if student not in students_no   else student.upper()   for student in students ]


# numbers= range(10)
# new_dict={}

# for n in numbers:
#     if n%2==0:


# import seaborn as sns
# df = sns.load_dataset("car_crashes")
# df.columns

# df.columns=[(col.upper()) for col in df.columns]
# word='FLAG'
# nword='NO_FLAG'

# new_columns = [f"{word} {col}" if 'INS' in col else f"{nword} {col}" for col in df.columns]

# print(new_columns)



# ['total', 'speeding', 'alcohol', 'not distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']



# text="The goal is to turn data into information, and information into insight."

# new_text=text.upper()

# new_text = new_text.replace(",", " ").replace(".", " ")
# print(new_text)



# lst=["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]



# # lst.pop(8)

# lst.append("R")
# print(lst)


# dict={'Christian': ["America", 18],
#       'Daisy': ["England", 12],
#       'Antonio': ["Spain", 22], 
#       'Dante':["Italy", 25]}


# dict["Ahmet"]=['Turkey', 24]

# dict.pop["Antonio"]

# print(dict)


# def func(x):
#     tek=[]
#     cift=[]

#     for sayi in x:
#      if sayi%2==0:
#         cift.append(sayi)
#      else:
#         tek.append(sayi)
#     return tek,cift



# l=[1,2,3,4,5,6,7,8,9]

# print(func(l))



# kume1=set(["data", "python"])
# kume2=set(["data", "function", "qcut", "lambda", "python", "miul" ])

# # print(kume1.issubset(kume2))

# if kume1.issubset(kume2):
#     print(kume2-kume1)

# else:
#     print("alt küme değil")



import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())


A=[]

for col in df.columns:
    A.append(col.upper())






















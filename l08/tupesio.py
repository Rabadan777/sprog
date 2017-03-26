# name = "123456"
# print(name[2:4])
# text = """много слов
# много слов
# много слов"""
# print(text)
# print(text.upper())
# print(text.replace("МНОГО","мало"))

# list - списки

pupils = ["магомед","арсен","гаджикурбан",94]
print(pupils)
print(pupils[1])
print(pupils[1:3])
pupils.append("хадижат") # добавить
print(pupils)
pupils.insert(1,"рабадан")
print(pupils)
some_peoples = ["абакар","карим"]
pupils.extend(some_peoples)
print(pupils)
pupils[0] = "супер магомед" # заменить
print(pupils)
del pupils[3]
print(pupils)
pupils.remove(94)
print(pupils)
pupils.remove("карим")
print(pupils)
print(pupils.pop(4))
print(pupils)
pupils.append("арсен")
print(pupils)

#tuple - кортежи
# bad_peoples = ("коля","бахмуд")
bad_peoples = "коля","бахмуд"
print(bad_peoples)
print(bad_peoples)



# set - множество
numbers1 = {4,5,7,9}
print(numbers1)
numbers2 = {6,7,8,4}
print(numbers1 & numbers2) # перечисление
print(numbers1 | numbers2)# обьядинение
print(numbers1 - numbers2) # разность

#преобразование
print(set(pupils) & set(bad_peoples))































































































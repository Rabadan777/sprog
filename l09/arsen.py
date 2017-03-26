ru_eng = {
"и":"and",
"лягушка":"frog",
"зло":"evil",
"лиса":"fox"
}
print(ru_eng)
print(ru_eng["лиса"])
ru_eng["зло"] = "harm" # изменить
print(ru_eng["зло"])
ru_eng["компьютер"] = "computer"
print(ru_eng["компьютер"])
word = input("введите русское слово: ")
translate = input("введите перевод на английский : ")
ru_eng[word] = translate
print(ru_eng)


word = input("введите русское слово :")
if word in ru_eng
    print(ru_eng[word])
else:
	print("не знаю")



































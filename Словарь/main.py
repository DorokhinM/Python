import random

dictionary = {
  "wall": "стена",
  "crap": "какашка",
  "pool": "бассейн",
  "time": "время",
  "fool": "дурак",
  "brain": "мозг",
  "black": "черный",
  "door": "дверь",
  "dead": "мертвый",
  "walk": 'ходить',
  "repeat": "повторять"
}

def add_dict(dictionary):
  addeng = input("Введите слово на английском: ")
  addrus = input("Введите слово на русском: ")
  dictionary.update({addeng: addrus})

def show_dict(dictionary):
  for key in dictionary.keys():
    print(key, '-', dictionary[key])

def ask_trans(dictionary):
  for key in dictionary.keys():
    randomd = random.choice(list(dictionary.keys()))
    usertext = input("Введите перевод слова " + "\"" + randomd + "\"" + ": ")
    if usertext == dictionary[randomd]:
      print("Верно!")
    else:
      print("Не верно!")

while True:
  showorstart = input("Введите \"show\" для вывода с
else:
  break
  













import random

num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))

rand = random.randint(num1, num2)

while True:
  try:
        answer = int(input("Ответ: "))
        if answer == rand:
          print("Молодец, ты отгадал число!")
          input()
          break
        elif answer < rand:
          print("Это число меньше загаданного")
        elif answer > rand:
          print("Это число больше загаданного!")
  except:
    print ("Не пытайся меня обмануть, я знаю, что ты написал букву :)")
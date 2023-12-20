import time

start_time = time.time()

from random import randint

n = randint(1, 30)

while 1:
  k = input("Угадайте целое число от 1 до 30: ")

  if k == "Выход":
    print("В следующий раз повезёт!")
    break

  k = int(k)

  if k == n:
    print("Вы угадали")
    end_time = time.time()
    print(f"приложение работола: {round(end_time - start_time, 2)}")
    break

  print("Ваше число " + ("больше" if k > n else "меньше") + ", чем задумал компьютер")

print("Загаданным числом было: " + str(n))

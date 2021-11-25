from random import randint
from time import time, sleep

class Trening_words():

  point = 0
  num_points = 10
  count_words_true = 0

  def __init__(self, file):
    self.file = file
    self.all_words = None
    self.count_words = 0
    self.random_words = ''

  def All_words(self):
    with open(self.file, mode='r', encoding='utf8') as file:
      self.all_words = file.readlines()

  def Count_words(self):
    self.count_words = len(self.all_words)

  def Random_words(self):
      n = randint(0, len(self.all_words))
      self.random_words = self.all_words[n].lower()

  def Processing_responses(self, option):
    if option == self.random_words.strip():
      self.point += self.num_points
      self.count_words_true += 1

    else:
      while option != self.random_words.strip():
        self.num_points -= 1
        option = input('Попробуйте еще раз: ')
      self.point += self.num_points
      self.num_points = 10
      self.count_words_true += 1


print('+' + '-' * 70 + '+')
text = 'Тренажер скоростного написания слов'
text2 = 'Цель: за определенное время напечатать как можно больше слов'
text3 = 'Правила: За каждое правильно написанное слово Вы получаете 10 очков,'
text4 = 'если слово введено неправильно, то Вы вводите его до тех пор, пока'
text5 = 'не напишите его правильно, при этом после каждой попытки у вас'
text6 = 'будет отниматься один балл'
print(f'|{text:^70}|')
print('+' + '-' * 70 + '+')
print(f'|{text2:^70}|')
print('+' + '-' * 70 + '+')
print(f'|{text3:^70}|')
print(f'|{text4:^70}|')
print(f'|{text5:^70}|')
print(f'|{text6:^70}|')
print('+' + '-' * 70 + '+')
print()
time_num = int(input('Введите время игры в секундах: '))
start_time = time()
run = True
x = Trening_words('Random_words.txt')
x.All_words()
x.Count_words()
for i in range(1, 4):
  print('До начала игры: ', i)
  sleep(1)
while run:
  x.Random_words()
  print(x.random_words, end='')
  test = input('Печатайте: ')
  x.Processing_responses(test)
  print()
  if time() - start_time >= time_num:
    print('Время вышло!')
    print(f'Колличество очков: {x.point}')
    print(f'Колличество правильных слов: {x.count_words_true}')
    run = False



































# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.).
# Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.
# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.
# Всего будет 3 класса: UrTube, Video, User.
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.
# Подробное ТЗ:
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
# adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#  Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем.
# Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
# Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
# Метод log_out для сброса текущего пользователя на None.
# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует.
# В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
# Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится,
# если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт,
# чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение:
# "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import hashlib
import time


class User:
 def __init__(self, nickname, password, age):
  self.nickname = nickname
  self.password = self.hash_password(password)  # Хеширование пароля
  self.age = age

 # Функция хеширования пароля.
 def hash_password(self, password):
  """Хеширование пароля с использованием алгоритма SHA-256."""
  return hashlib.sha256(password.encode()).hexdigest()

 def __eq__(self, other):
  """Переопределяем метод сравнения, чтобы проверять пользователя по имени пользователя."""
  return self.nickname == other.nickname

 def __str__(self):
  return f"{self.nickname}"


class Video:

 def __init__(self, title, duration, adult_mode=False):
  self.title = title
  self.duration = duration
  self.time_now = 0  # Текущее время просмотра видео
  self.adult_mode = adult_mode

 def __eq__(self, other):
  """Переопределяем метод сравнения, чтобы проверять видео по заголовку."""
  return self.title.lower() == other.title.lower()

 def __str__(self):
  return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:

 def __init__(self):
  self.users = []
  self.videos = []
  self.current_user = None

 def log_in(self, nickname, password):
  """Проверяет наличие пользователя с указанным логином и паролем."""
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  for user in self.users:
   if user.nickname == nickname and user.password == hashed_password:
    self.current_user = user
    print(f"Пользователь {nickname} вошёл в систему.")
    return True
  print("Ошибка входа: неверный логин или пароль.")
  return False

 def register(self, nickname, password, age):
  """Регистрирует нового пользователя и автоматически выполняет вход."""
  new_user = User(nickname, password, age)
  if new_user in self.users:

   print(f"Пользователь {nickname} уже существует.")
  else:
   self.users.append(new_user)
   self.current_user = new_user

 def log_out(self):
  """Выходит из текущего пользователя."""
  if self.current_user:
   print(f"Пользователь {self.current_user.nickname} вышел из системы.")
   self.current_user = None
  else:
   print("В системе нет активного пользователя.")

 def add(self, *videos):
  """Добавляет новые видео в список, если видео с таким названием ещё нет."""
  for video in videos:
   if video not in self.videos:
    self.videos.append(video)

 def get_videos(self, search_term):
  """Возвращает список видео, содержащих поисковое слово (регистр не учитывается)."""
  search_term_lower = search_term.lower()
  return [video.title for video in self.videos if search_term_lower in video.title.lower()]

 def watch_video(self, title):
  """Воспроизводит видео, если пользователь имеет право на просмотр."""
  if not self.current_user:
   print("Войдите в аккаунт, чтобы смотреть видео")
   return

  for video in self.videos:
   if video.title == title:
    if video.adult_mode and self.current_user.age < 18:
     print("Вам нет 18 лет, пожалуйста покиньте страницу")
     return

    for second in range(video.time_now + 1, video.duration + 1):
     print(second, end=' ', flush=True)
     time.sleep(1)
    print("Конец видео")
    video.time_now = 0
    return


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')

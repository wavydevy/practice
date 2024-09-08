import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

text = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!\n
%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.\n
Как будет проходить ваше обучение на %website%? \n
→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.\n
Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

website = 'https://dvmn.org/referrals/hcOYG4OgDu0hHQf978Uv74CI9YZqS6D16E49Z0EJ/'
friend_name = 'Андрей'
my_name = 'Егор'
tittle = 'Приглашение!'
email_from = os.getenv('SENDER')
email_to = os.getenv('RECIPIENT')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

text = text.replace('%website%', website, 4)
text = text.replace('%friend_name%', friend_name, 1)
text = text.replace('%my_name%', my_name, 1)

letter = """\
From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8"; \n\n""".format(email_from, email_to, tittle) + text
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, letter)
server.quit()
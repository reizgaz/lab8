
Инструкция:

1. Необходимо скачать и установить последнюю версию python 3

https://www.python.org

2. Для работы сервера нужно установить следующие библиотеки, используя pip:

pip install flask

pip install flask_wtf

pip install wtforms

3. Клонировать/скачать репозиторий factor, используя ssh/http/zip:

ssh: git@github.com:aksenof/factor.git

http: https://github.com/aksenof/factor.git

zip: https://github.com//aksenof/factor/archive/master.zip

4. Запустить сервер из коммандной строки:

python 'путь к проекту'/app.py

5. Открыть в браузере (желательно google chrome или opera) страницу:

127.0.0.1:5000 или 127.0.0.1:5000/index

ввести число в поле ввода и нажать кнопку ОК

6. Откроется страница 127.0.0.1:5000/result/<введённое число>

где будет факториал введенного числа

_____

Или

Использовать докер: https://hub.docker.com/repository/docker/aksenof/factor

docker pull aksenof/factor


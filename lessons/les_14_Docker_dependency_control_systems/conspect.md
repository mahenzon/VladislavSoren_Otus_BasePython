# Dependency Control

Существуют системы контроля зависимостей, которые круче `pip`.
Они являются надстройками над pip о с дополнительными плюшками.

`Pipenv`

Установка глобального pipenv на `ubuntu`
```shell
sudo pip install pipenv
```

Устанавливаем все зависимости из Pipfile.lock (замороженные версии всего проекта):
```shell
pipenv install
```
Ищем fastapi в установленных пакетах:
```shell
pip list | grep fastapi
```
Показать все зависимости в консоли:
```shell
pipenv graph
```

Когда я выполняю `pipenv shell` создаётся новый терминал (соответственно и задача),
при этом новый терминал НИЧЕМ не отличается от старого, ОДНАКО всё что я начинаю
устанавливать через `pipenv install` начинает устанавливаться в /home/soren/.local/share/virtualenvs,
а не в venv текущего проекта.
Поэтому все зависимости можно ставить просто через `pipenv install`. 
Т.к. pipenv установлен глобально, то его не обязательно инстолить в каждый проект.

Если же всё таки ткнул `pipenv shell`, то убей терминал введя `exit`, либо `kill -9 PID`.
И всё снова будет ложиться куда надо.

Если будет проблемы с установкой глобального pipenv в контейнерах, то просто можно
устанавливать через `pip install pipenv` непосредственно в venv проекта.

`[dev-packages]` в `Pipfile` - это пакеты, которые нужны только для разработки, но не
в продакшене, например `pytest`, такие пакеты добавляйте командой:
```shell
pipenv install pytest -d
```


> В файле Pipfile.lock лежат хэши версий, что гарантирует установку верного пакета
> Его обязательно публиковать в репозитории! (это те версии, которые мы хотим хранить)


***

`Poetry` - другая система контроля зависимостей, более мудрёная, когда понадобится,
тогда и глубже исследую
Но он вроде как более модный и им часто пользуются


## Containerization vs Virtualization:
Создаётся контейнер на основе образа ubuntu и в интерактивном режиме запускается bash:
```shell
docker run -it ubuntu bash
```
> Обязательно перед установкой каких либо пакетов сделать `apt update` и `apt  upgrade`

В докерфайле в первую очередь нужно устанавливать все зависимости.

 
Создаём образ по Dockerfile в текущей директории
```shell
docker build -t app .
```

Запускаем приложение
```shell
docker run -p 9999:8000 --name dev_app_5 -it app
```



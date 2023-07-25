# Автоматизация тестов функциональной части проекта HERITAGE

---
## Описание

Проект посвящен тестированию регистрации, авторизации и добавления рецептов. Разделен на 3 основных каталога.
В locators хранятся локаторы для страниц, которые стоит протестировать, в pages хранятся методы, с помощью которых
проводим тестирование и tests, в котором хранятся настройки перед тестированием, вызовы тестов и операции с результатми тестирования.


Данные для теста берутся из каталога **input_data**. Произведены только **ПОЗИТИВНЫЕ** сценарии. Количество тестов: 3.

Список используемых технологий:
- Python 3.11
- pytest 7.4.0
- chromdriver 114

---
## Запуск

Для запуска необходимо: 
- Клонировать проект с GitHub
- В терминале ввести команду: pytest

При возникновении ошибок следует изменить значение **username** в файле **input_data.py** (например на  'selenium_test100').

___

## Будущее проекта

Будущие изменения прямо завсят от добавления нового функционала в HERITAGE.
# Where to Go

**Where to Go** — это веб-приложение на Django для отображения интересных мест на интерактивной карте.  
Вы можете добавлять точки на карте, снабжая их описаниями и фотографиями, чтобы делиться красивыми и увлекательными локациями.  
![map_sample](https://github.com/user-attachments/assets/0f91de00-9f7d-4741-9fac-af351c7f4ae6)


## Описание проекта

Проект представляет собой интерактивную карту, на которой отмечены разнообразные места. Каждое место содержит:
- **Название**  
- **Краткое описание**  
- **Подробное описание**  
- **Координаты** (широта и долгота)  
- **Фотогалерею**

Демо версия сайта доступна по [адресу](http://89.110.122.91)

Приложение предоставляет удобный интерфейс для просмотра мест и административную панель для управления контентом.

---

## Используемые технологии

- **Python 3.11**
- **Django 4.2**
- **HTML/JavaScript**
- **Pillow** для работы с изображениями  
- **django-admin-sortable2** для сортировки фотографий  
- **django-tinymce** для форматирования текста  

---

## Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/aqwarius2003/where_to_go.git
   ```

2. **Создайте и активируйте виртуальное окружение:**
   - Для Linux/Mac:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Для Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Создайте файл `.env` в корневой директории проекта и добавьте следующие параметры:**
   ```
   SECRET_KEY=ваш_секретный_ключ
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```
   
   - `SECRET_KEY`: Это секретный ключ, используемый Django для обеспечения безопасности. Он необходим для шифрования данных и защиты от подделки запросов. Важно, чтобы этот ключ оставался конфиденциальным и не был доступен посторонним лицам.

   - `DEBUG`: Булевская переменная, которая определяет, включен ли режим отладки. Если установлено значение `True`, Django будет выводить подробные сообщения об ошибках, что полезно для разработки. В рабочем окружении рекомендуется устанавливать `False` для повышения безопасности.

   - `ALLOWED_HOSTS`: Список хостов, которые могут обращаться к вашему приложению. Это строка, содержащая имена хостов, разделенные запятыми. Например, `localhost,127.0.0.1`. В рабочем окружении сюда следует добавлять доменные имена вашего сайта.

   - `DB_ENGINE`: Указывает на используемый движок базы данных. В данном случае используется `django.db.backends.sqlite3`, что означает, что приложение будет использовать SQLite в качестве базы данных.

   - `DB_NAME`: Имя файла базы данных. Для SQLite это имя файла, в котором будет храниться база данных. В данном случае это `db.sqlite3`.
   

   Убедитесь, что все переменные правильно настроены в вашем `.env` файле перед запуском приложения.


5. **Выполните миграции:**
   ```bash
   python manage.py migrate
   ```

6. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```

Теперь приложение доступно по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Административная панель

Для управления местами и фотографиями используется административная панель Django.  

1. **Создайте суперпользователя:**
   ```bash
   python manage.py createsuperuser
   ```

2. **Перейдите по адресу:**
   [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  

В админ-панели вы можете:
- Добавлять новые места  
- Загружать и сортировать фотографии  
- Редактировать описания с помощью визуального редактора TinyMCE  

---

## Структура проекта

- `places/models.py` — модели данных для мест и фотографий  
- `places/admin.py` — настройки административной панели  
- `places/views.py` — представления для отображения карты и данных  
- `where_to_go/settings.py` — основные настройки проекта  

---

## Добавление локаций из JSON-файлов
Команда load_place позволяет загружать данные о локациях из JSON-файлов в базу данных. 

Пример содержимого JSON-файла:
   ```json
   {
       "title": "Генератор Маркса или «Катушка Тесла»",
       "imgs": [
           "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/d3b5cc74cc94c802b51c85542b2f9ad5.jpg",
           "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b742b82f77028d6a8c9be681cab25a3d.jpg",
           "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/57f990fd24a55324fc1fc541cac41b99.jpg",
           "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/2d5be0d4e83fdde3e8c98f18e0d2e365.jpg",
           "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/d4a8ab43eff1f7e83491610682d13984.jpg",
           "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7945e1e565530ab6943c40d64f21cfb7.jpg"
       ],
       "description_short": "Место, в котором рождаются искусственные молнии и облака.",
       "description_long": "<p>Внешний вид этого монстроподобного, внушительного комплекса заставляет сердца посетителей биться чаще, а некоторое сходство с катушкой Тесла (на самом деле это генератор Аркадьева-Маркса) влечёт сюда всех любителей научпопа, индастриала и других интересующихся. Для того, чтобы попасть на территорию действующего испытательного стенда ВНИЦ ВЭИ, коим и является это окутанное мифами место, рекомендуется договориться с охраной. Несанкционированное попадание в пределы испытаний может повлечь самые серьёзные последствия!</p>",
       "coordinates": {
           "lng": "36.88324860715219",
           "lat": "55.92555463090268"
       }
   }
   ```

Вы можете использовать следующие типы ссылок:

Одиночная ссылка на JSON-файл: Укажите URL, который ведет непосредственно на JSON-файл. Ссылка не обязательно должна быть в формате RAW, так как скрипт автоматически преобразует её в нужный формат.
   ```bash
   python manage.py load_place https://github.com/your-repo/your-file.json
   ```

Несколько ссылок через пробел: Укажите несколько URL, разделенных пробелами. Это позволяет загружать данные из нескольких JSON-файлов за один запуск команды.
   ```bash
   python manage.py load_place https://github.com/your-repo/file1.json https://github.com/your-repo/file2.json
   ```

Ссылка на GitHub-страницу с JSON-файлами: Укажите URL на страницу GitHub, где опубликованы ссылки на JSON-файлы. Скрипт автоматически извлечет и обработает все ссылки на JSON-файлы, найденные на этой странице.
   ```bash
  python manage.py load_place https://github.com/devmanorg/where-to-go-places/tree/master/places
   ```

Примечания
- Скрипт автоматически преобразует ссылки из формата GitHub в формат RAW, если это необходимо.
- Если локация с таким же названием уже существует в базе данных, она не будет добавлена повторно.
- Фотографии, связанные с локацией, также загружаются и сохраняются в базе данных, если они ещё не существуют.

## Лицензия

Проект распространяется под лицензией [**MIT**](https://github.com/Skripko-A/enjoymap/blob/master/LICENSE). Вы можете свободно использовать и изменять код в соответствии с условиями лицензии.

---

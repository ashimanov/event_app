## запуск приложения

```
venv\scripts\flask --app event_app_files\server.py run
```


## cURL тестирование

### добавление нового события
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-03-28|title|text"
```

### получение всего списка событий
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### получение данных о событии по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```

### обновление информации о событии по идентификатору / ID == 1 /  новый текст == "new text"
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-03-28|title|new text"
```

### удаление события по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-03-28|title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/
1|2024-03-28|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2024-03-28|title|text

**## ввод даты в неправильном формате**
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-03|title|text"
api failed to CREATE  with: Invalid isoformat string: '2024-03'

**## ввод данных без даты события**
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "title|text"
api failed to CREATE  with: invalid RAW event data title|text

**## попытка создать дополнительное событие на уже существующую дату**
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-03-28|title|some new text"
api failed to CREATE  with: failed CREATE operation with: failed CREATE operation with: event date 2024-03-28  FOUND in storage

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|title|new text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "title|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: text lenght > MAX: 200

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 30

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/note/
-- пусто --
```

# TaskFlow API

REST API для управления проектами и задачами с аутентификацией пользователей.

---

## 🚀 Стек технологий

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Docker
* JWT (аутентификация)

---

## 📌 Функциональность

* Регистрация и авторизация пользователей
* Работа с проектами (CRUD)
* Работа с задачами (CRUD)
* Связь: User → Project → Task
* Проверка прав доступа (пользователь видит только свои данные)

---

## 🧱 Архитектура проекта

```
app/
├── core/        # настройки и безопасность (JWT, config)
├── db/          # подключение к базе данных
├── deps/        # зависимости FastAPI (auth, db)
├── models/      # модели SQLAlchemy (таблицы)
├── schemas/     # Pydantic-схемы (валидация и ответы API)
├── routers/     # API endpoints
└── main.py      # точка входа
```

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий

```
git clone https://github.com/MahmudDrt/taskflow-api.git
cd taskflow-api
```

### 2. Создать .env

```
cp .env.example .env
```

Сгенерировать SECRET_KEY:

```
python -c "import secrets; print(secrets.token_urlsafe(64))"
```

Вставить в `.env`.

---

### 3. Запуск через Docker

```
docker compose up --build
```

---

### 4. Применить миграции (если нужно)

```
docker compose exec backend alembic upgrade head
```

---

## 📖 Документация API

После запуска доступно:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Аутентификация

Используется JWT.

1. Получить токен:

```
POST /auth/login
```

2. Вставить в Swagger:

```
Authorize → Bearer <token>
```

---

## 📊 Пример структуры данных

* User
* Project (принадлежит пользователю)
* Task (принадлежит проекту)

```
User → Project → Task
```

---

## 🛠 Todo / Планы развития

* [ ] Добавить роли пользователей (admin/user)
* [ ] Реализовать пагинацию
* [ ] Добавить фильтрацию задач
* [ ] Перевести статус задач в Enum на уровне БД
* [ ] Написать тесты (pytest)
* [ ] Добавить CI/CD
* [ ] Логирование и мониторинг
* [ ] Ограничение частоты запросов (rate limiting)

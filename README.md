# TaskFlow API

TaskFlow API — REST API сервис для управления проектами и задачами.

Проект реализован как backend-приложение на FastAPI с JWT-аутентификацией, PostgreSQL, Alembic и Docker.

---

## Стек технологий

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- JWT
- Pydantic
- Pytest

---

## Функциональность

- Регистрация и авторизация пользователей
- JWT-аутентификация
- Получение текущего пользователя
- CRUD для проектов
- CRUD для задач
- Частичное обновление задач через PATCH
- Фильтрация задач по статусу
- Фильтрация задач по проекту
- Пагинация списка задач
- Проверка прав доступа
- Миграции базы данных через Alembic
- Минимальный тест регистрации пользователя

---

## Архитектура проекта

```text
app/
├── core/        # настройки и безопасность
├── db/          # подключение к базе данных
├── deps/        # зависимости FastAPI
├── models/      # SQLAlchemy-модели
├── schemas/     # Pydantic-схемы
├── routers/     # API endpoints
└── main.py      # точка входа

tests/
└── test_auth.py
```

---

## Связи данных

```text
User → Project → Task
```

Один пользователь может иметь несколько проектов.  
Один проект может иметь несколько задач.  
Пользователь может работать только со своими проектами и задачами.

---

## Запуск проекта

### 1. Клонировать репозиторий

```bash
git clone https://github.com/MahmudDrt/taskflow-api.git
cd taskflow-api
```

### 2. Создать `.env`

```bash
cp .env.example .env
```

Пример `.env`:

```env
DATABASE_URL=postgresql://postgres:1234@db:5432/taskflow
SECRET_KEY=your_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256
```

Сгенерировать `SECRET_KEY`:

```bash
python -c "import secrets; print(secrets.token_urlsafe(64))"
```

### 3. Запустить через Docker

```bash
docker compose up --build
```

После запуска API будет доступен:

```text
http://127.0.0.1:8000
```

Swagger-документация:

```text
http://127.0.0.1:8000/docs
```

Миграции Alembic применяются автоматически при запуске контейнера.

---

## Аутентификация

### Регистрация

```http
POST /auth/register
```

Пример запроса:

```json
{
  "email": "user@example.com",
  "username": "user",
  "password": "123456"
}
```

Пример ответа:

```json
{
  "message": "user created"
}
```

### Логин

```http
POST /auth/login
```

Пример запроса:

```json
{
  "email": "user@example.com",
  "password": "123456"
}
```

Пример ответа:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

После получения токена его нужно вставить в Swagger:

```text
Authorize → Bearer <token>
```

---

## Основные endpoints

### Users

```http
GET /users/me
```

### Projects

```http
POST /projects
GET /projects
GET /projects/{project_id}
PUT /projects/{project_id}
DELETE /projects/{project_id}
```

### Tasks

```http
POST /tasks
GET /tasks
GET /tasks/{task_id}
PUT /tasks/{task_id}
PATCH /tasks/{task_id}
DELETE /tasks/{task_id}
```

---

## Пример создания задачи

```http
POST /tasks
```

```json
{
  "title": "Implement authentication",
  "description": "Add JWT authentication",
  "status": "pending",
  "deadline": "2026-05-10T12:00:00",
  "project_id": 1
}
```

Доступные статусы задачи:

```text
pending
in_progress
completed
```

---

## Фильтрация и пагинация задач

Получить задачи с пагинацией:

```http
GET /tasks?limit=10&offset=0
```

Фильтр по статусу:

```http
GET /tasks?status=pending
```

Фильтр по проекту:

```http
GET /tasks?project_id=1
```

Комбинированный запрос:

```http
GET /tasks?project_id=1&status=pending&limit=10&offset=0
```

---

## Частичное обновление задачи

```http
PATCH /tasks/{task_id}
```

Пример запроса:

```json
{
  "status": "completed"
}
```

PATCH обновляет только переданные поля и не затирает остальные данные задачи.

---

## Тесты

Запуск тестов:

```bash
pytest -v
```

Пример результата:

```text
tests/test_auth.py::test_register_user_success PASSED
```

---

## Что показывает проект

- Умение разрабатывать REST API
- Работу с PostgreSQL через SQLAlchemy
- Использование JWT-аутентификации
- Проверку прав доступа к данным
- Работу с миграциями Alembic
- Контейнеризацию через Docker
- Базовое тестирование API

---

## Планы развития

- [ ] Добавить больше тестов для проектов и задач
- [ ] Добавить CI/CD
- [ ] Добавить логирование
- [ ] Добавить роли пользователей
- [ ] Добавить rate limiting

# Бэкенд-сервис для обработки банковских вебхуков

Сервис для приема и обработки платежных вебхуков от банка с начислением баланса организаций по ИНН.

## 📌 Функционал

- Прием вебхуков от банка в формате JSON
- Обработка платежей с защитой от дублирования
- Начисление средств на баланс организаций
- Ведение истории изменений баланса
- Проверка текущего баланса по ИНН

## 🛠 Технологии

- Python 3.9
- Django 4.2
- Django REST Framework
- MySQL

## 🚀 Установка

1. Клонировать репозиторий:
```bash
git clone https://github.com/ryazd/bank-webhooks-service.git
cd bank-webhooks-service
```

2. Клонировать репозиторий:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

3. Установить зависимости:
```bash
pip install -r requirements.txt
```

4. Применить миграции:
```bash
python manage.py migrate
```

5. Создать суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустить сервер:
```bash
python manage.py runserver
```

## 🌐 API Endpoints
### Прием вебхука

POST /api/webhook/bank/

```json
{
  "operation_id": "uuid",
  "amount": 10000,
  "payer_inn": "1234567890",
  "document_number": "PAY-123",
  "document_date": "2024-01-01T12:00:00Z"
}
```

### Получение баланса
GET /api/organizations/<inn>/balance/
```json
{
  "inn": "1234567890",
  "balance": 10000
}
```

## 🧑‍💻 Администрирование
Доступно по адресу /admin/ после создания суперпользователя.

Возможности:

- Просмотр и редактирование организаций

- Просмотр истории платежей

- Анализ изменений баланса

- Фильтрация и поиск записей

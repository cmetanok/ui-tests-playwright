# UI Tests на Playwright + Pytest

Автотесты для интернет-магазина [saucedemo.com](https://www.saucedemo.com)
на Python + Playwright + Pytest с использованием паттерна Page Object Model.

## Что тестируется

- **Логин**: успешный вход, заблокированный пользователь, неверный пароль,
  пустые поля.
- **Каталог товаров**: отображение списка, сортировка по цене (low → high),
  добавление товаров в корзину, счётчик корзины.
- **Корзина**: отображение добавленного товара, удаление, переход к checkout.

## Стек

- Python 3.10+
- Pytest 8.x
- Playwright
- pytest-playwright
- Page Object Model

## Структура

```
ui-tests-playwright/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

## Как установить

```bash
# 1. Клонировать
git clone https://github.com/cmetanok/ui-tests-playwright.git
cd ui-tests-playwright

# 2. Создать виртуальное окружение
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Установить браузеры для Playwright
playwright install
```

## Как запустить

```bash
# Все тесты (с видимым браузером — уже в pytest.ini)
pytest

# Тихий режим (без окна браузера)
pytest --headless

# Один файл
pytest tests/test_login.py

# Один тест
pytest tests/test_cart.py::TestCart::test_checkout_button
```

## Что показывает проект

- Владение Playwright и pytest-playwright.
- Применение паттерна **Page Object Model** — код тестов не содержит
  CSS-селекторов, всё инкапсулировано в page-классах.
- Работа с локаторами через `data-test` атрибуты (устойчивые к изменениям).
- Позитивные и негативные сценарии авторизации.
- Проверка сортировки, работы корзины, навигации.
- Настройка фикстур в `conftest.py`.


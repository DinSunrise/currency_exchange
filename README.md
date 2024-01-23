**1. Склонировать репозиторий и перейти в директорию:**
		
	git clone https://github.com/DinSunrise/currency_exchange.git
	cd currency_exchange

**2. Создать виртуальное окружение:**

	python -m venv venv
	source venv/bin/activate 
 	#Windows: `venv\Scripts\activate`

**3. Установить зависимости:**

	pip install -r requirements.txt

**4. Мигрировать бд:**

	python manage.py migrate

**5. Запустить сервер:**

	python manage.py runserver

**6. Проверить курс доллара к рублю на: **

	http://127.0.0.1:8000/get-current-usd/

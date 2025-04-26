# Базовый образ с Python
FROM python:3.12-slim

# Установка зависимостей для Chrome и Firefox
RUN apt-get update && apt-get install -y \
    chromium chromium-driver \
    firefox-esr \
    wget unzip \
    libnss3 \
    libasound2 \
    libxss1 \
    libdbus-glib-1-2 \
    libgtk-3-0 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Установка geckodriver для Firefox (актуальная версия 0.34.0)
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/ \
    && chmod +x /usr/local/bin/geckodriver \
    && rm /tmp/geckodriver.tar.gz

# Установка chromedriver через apt (уже вклбчен в chromium-driver)
# Проверяем наличие chromedriver
RUN which chromedriver || ln -s /usr/lib/chromium/chromedriver /usr/bin/chromedriver

# Настройка переменных окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SELENIUM_HEADLESS=true \
    CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER_BIN=/usr/bin/chromedriver \
    FIREFOX_BIN=/usr/bin/firefox-esr \
    GECKODRIVER_PATH=/usr/local/bin/geckodriver

# Копирование зависимостей Python
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование тестов
COPY . .

# Запуск тестов через pytest
ENTRYPOINT ["pytest"]
CMD ["tests/"]
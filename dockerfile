# Базовый образ с Python
FROM python:3.12-slim

# Отключение интерактивного режима debconf
ENV DEBIAN_FRONTEND=noninteractive

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    xvfb \
    xauth \
    chromium \
    chromium-driver \
    firefox-esr \
    wget \
    unzip \
    libnss3 \
    libasound2 \
    libxss1 \
    libdbus-glib-1-2 \
    libgtk-3-0 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Установка geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz  -O /tmp/geckodriver.tar.gz && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz

# Установка chromedriver
RUN ln -sf /usr/lib/chromium/chromedriver /usr/bin/chromedriver

# Переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SELENOID_HOST=selenoid \
    CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER_BIN=/usr/bin/chromedriver \
    FIREFOX_BIN=/usr/bin/firefox-esr \
    GECKODRIVER_PATH=/usr/local/bin/geckodriver

# Виртуальное окружение (рекомендуется)
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Копирование зависимостей Python
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование тестов
COPY tests/ /app/tests/

# Копирование скрипта ожидания
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Запуск тестов
ENTRYPOINT ["pytest"]
CMD ["tests/", "--browser", "chrome", "--executor", "selenoid", "--url", "http://opencart:8080"]
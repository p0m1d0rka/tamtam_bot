FROM python:3.8.2
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD gunicorn -w 3 -b 0.0.0.0:9999 app.start:init_app --worker-class aiohttp.GunicornWebWorker
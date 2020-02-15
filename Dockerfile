FROM python:3.8.1-buster

WORKDIR app

RUN pip3 install python-telegram-bot

COPY . .

CMD python3 ibeme_bot.py


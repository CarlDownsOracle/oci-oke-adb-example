FROM enghouse-oke-base:latest

RUN mkdir /app
WORKDIR /app
ADD apps /app/
RUN python3 -m pip install -r /app/requirements.txt

ENV FLASK_APP=/app/todo/todo.py
ENV LANG=en_US.utf-8

RUN mkdir /wallet
ENV TNS_ADMIN=/wallet

EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--no-reload"]

FROM python:3.8

ADD index.py .

# CMD ["python","./index.py"]
ENTRYPOINT python index.py
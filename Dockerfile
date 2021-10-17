FROM python:3.8
WORKDIR /app
copy . /app

ENV VIRTUAL_ENV=/app/pyenv


ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip3 install virtualenv
CMD virtualenv $VIRTUAL_ENV
CMD /app/pyenv/bin/uvicorn main:app --reaload

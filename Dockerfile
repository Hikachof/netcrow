FROM python:3.9.9

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Serverエラーにならずにスクレイピングできるようになる
RUN apt-get update
RUN apt-get install -y libnss3
RUN apt-get install -y libgconf-2-4
RUN apt-get install -y libfontconfig1

WORKDIR /app

COPY ./app /app
COPY ./drivers /drivers

CMD ["python", "main.py"]
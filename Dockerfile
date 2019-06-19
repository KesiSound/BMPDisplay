FROM arm32v7/python:3-slim-stretch
RUN apt-get update -y
RUN apt-get install -y build-essential zlib1g zlib1g-dev libjpeg-dev
RUN pip install Pillow
RUN pip install Adafruit_SSD1306
RUN pip3 install adafruit-circuitpython-bmp280
ADD BMPDisp.py /
CMD [ "python", "./BMPDisp.py"]

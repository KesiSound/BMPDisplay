FROM arm32v7/python:3-stretch
ADD BMPDisp.py /
RUN pip install -U setuptools
RUN apt-get update -y
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install Adafruit_SSD1306
RUN pip3 install adafruit-circuitpython-bmp280
RUN pip install Pillow
CMD [ "python", "./BMPDisp.py"]
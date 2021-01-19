FROM python:3

# set a directory for the app
WORKDIR /usr/src/factor

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install flask flask_wtf wtforms

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./server.py"]
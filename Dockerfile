#official python base image 
FROM python:3.8-slim-buster

#use this path as the default location for all subsequent commands
WORKDIR /app

#copy requirements.txt file into our image
COPY requirements.txt requirements.txt

#execute the command pip3 install and the modules will install into the image.
RUN pip3 install -r requirements.txt

#takes all the files located in the current directory and copies them into the image
COPY . .

#command we want to run when our image is executed inside a container
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]


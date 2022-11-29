#Selecting latest python runtime base image from docker hub
#Will download image to local computer or get from local file
FROM python:latest
#Change directory to /App on the docker container file system
WORKDIR /app
#Copy content of the publish folder to the working dir of docker container
#COPY pyt.py .
COPY . .

RUN pip install -r requirements.txt

#Entrypoint will be executed when the docker container runs
#python command is used
#HelloWorld.py is argument for python command

ENTRYPOINT ["python", "pyt.py"]

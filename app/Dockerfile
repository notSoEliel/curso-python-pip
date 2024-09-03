FROM python:3.10.12 
#This is the base image for our application (Python in this case)

WORKDIR /app 
#This sets the working directory to /app inside the container
COPY requirements.txt /app/requirements.txt
#This copies the requirements.txt file from your local machine to the /app directory in the container

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#This runs the pip install command to install all the dependencies listed in the requirements.txt file
#-r means it will read the requirements.txt file and install all the packages listed there
#--no-cache-dir means it won't use any cached data during installation
#--upgrade means it will upgrade any existing package to its latest version

COPY . /app

#This is where your application code starts
CMD bash -c "while true; do sleep 1; done"
#This command runs a shell script that keeps the container running indefinitely. It's useful for applications that don't have their own built-in server to keep running.
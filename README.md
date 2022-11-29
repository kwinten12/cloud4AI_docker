# cloud4AI_docker

## docker-compose:

  With this we build both docker files, assign them to a container, specify the needed volumes and for the website container we specify the port to run on.

## model:
  
  In this folder the files to create and train the model are stored.
  After that the model is stored on the volume created in the docker-compose file.
 
## website:
  
  Here we store the files that make the webserver run.
  When the form has its data and the user submits the data, the stored model will be loaded, the data will be read and funally the model will predict an ouptut.
  Once we have an output it will be given back to the HTML page that will print the result.

## usage
Go to the directory in wich the docker-compose file is stored with a cli using cd "<directory>".
Then, use the command "docker-compose up" to run the docker files.
Go to localhost:8080 to see the webserver running.

Now you can give values as input to predict if a person will have diabetes.
Some values are given to test if it works correctly (6,148,72,35,50), this should give an output of 1 (a.k.a. true)

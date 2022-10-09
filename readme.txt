#WORKDIR

Put the file inside your dir, can be ~/Documents or ~/Download or whatever you want.
I am using ~/Documents dir here for the example.


#BUILD THE DOCKER IMAGE
Go inside the file, 

cd ~/Documents/json_convert/

Run below command in your terminal,

docker build -t csv_to_json .

#NOTE: above path can be configurable based on your path dir setting


#RUN THE IMAGE

docker run -v ~/Documents/json_convert/src/:/app/ csv_to_json

#NOTE: above path can be configurable based on your path dir setting

OUTPUT FILE IS LOCATED INSIDE ./src/output
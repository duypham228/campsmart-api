
from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template('index.html')

@app.route("/<location>")
def weather(location):
	#Parameters for the API to find the location ID
    
    #Request the API to get the location id

    #Get the id from the response
 
    #Request the API to get the weather based on location id
    
    #converting to JSON
    
    #Get the consolidated weather from the JSON file
    
    #Get the list of weather info for today weather
    
    #Get today temperature from the list
    
	return render_template('weather.html', location=location, temp=today_temp)



if __name__=="__main__":
	app.run(host='0.0.0.0', port=8080)

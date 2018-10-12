from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify 
import requests
import json
import re


app=Flask(__name__)
sslify=SSLify(app)

	


	URL = "https://api.telegram.org/bot671540030:AAErA9Bye6Ua-xb9gVJBiGOEhLUXjb9qYqU/"




	def write_json(date,filename="answer.json"):
		with open(filename,"w") as f:
			json.dump(date,f,indent=2,ensure__ascii=False)



	def send_message(chat_id,text="Привіт що вас цікавить "):
		url=URL + "sendMessage"
		answer={"chat_id":chat_id, "text":text}
		r=requests.post(url,json=answer)
		return r.json()





	def parse_text(text):
		patern=r"/\w+"
		contamination=re.search(patern,text).group()
		return contamination[1:]



	def get_price(contamination):
		#######################url = "{}".format(contamination) поле для get запросов АПІ
		r=requests.get(url).json()
		price=r[-1]["price_usd"]
    	return price  


		@app.route("/671540030:AAErA9Bye6Ua-xb9gVJBiGOEhLUXjb9qYqU", metods=["POST","GET"])
		def index():
			if request.metod == "POST":
				r=request.get_json()
				chat_id=r["message"]["chat"]["id"]
				message=r["message"]["text"]


				patern = r"/\w+"


				if re.search(patern,message):
					price=get_price(parse_text(message)) 
					send_message(chat_id, text=price)
				#write_json(r)
				return jsonify(r)
			return "<h1>Bot Welcomes you</h1>"

			#https://api.telegram.org/bot671540030:AAErA9Bye6Ua-xb9gVJBiGOEhLUXjb9qYqU/METHOD_NAME/setWebhook
			
				
	

if __name__==("__main__"):
	app.run()



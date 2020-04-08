import uuid
import numpy as np
import pickle
from flask import Flask, render_template, request,jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer



app = Flask(__name__)
model_path="modelmnb_final.pkl"#Sved model pickle path.
model = None
max_length = None
unique_intent = None

with open(model_path,"rb") as saved_processing:
    model,unique_intent = pickle.load(saved_processing)
    saved_processing.close()
    
count_vect = pickle.load(open('count_vect_final', 'rb')) 

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    currentIntent=predict(userText,unique_intent,model)
    if(currentIntent=='Greeting'):
    	msg="Hi Good Morning! How may I assist you? "
    elif(currentIntent=='Dentistry'):
    	msg="It sounds like you need help with Dentistry,.<a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10076' target='_blank' style='color:white'> Click Here</a> to find more details "
    elif(currentIntent=='Family_Practice'):
    	msg="It sounds like you need help with Family Practice,The following link will help you.<a href=' https://www.centraleasthealthline.ca/listServices.aspx?id=10655' target='_blank' style='color:white'> Click Here</a> to find more details"
    elif(currentIntent=='Urgent_Care'):
    	msg="It sounds like you need help with Urgent Care,The following link will help you. <a href='https://www.centraleasthealthline.ca/listServices.aspx?id=11234' target='_blank' style='color:white'> Click Here</a> to find more details"
    elif(currentIntent=='Home_care_services'):
    	msg="It sounds like you need help with Home care services,The following link will help you. <a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10074' target='_blank' style='color:white'> Click Here</a> to find more details "
    elif(currentIntent=='Optometry'):
    	msg="It sounds like you need help with Optometry,The following link will help you.<a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10288' target='_blank' style='color:white'> Click Here</a> to find more details "
    elif(currentIntent=='Rehab_Medicine'):
    	msg="It sounds like you need help with Rehabilitation Medicine ,The following link will help you. <a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10827' target='_blank' style='color:white'> Click Here</a> to find more details "
    elif(currentIntent=='Speech_and_Language_pathology'):
    	msg="It sounds like you need help with Speech and Language Pathology,The following link will help you.<a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10288' target='_blank' style='color:white'> Click Here</a> to find more details "
    elif(currentIntent=='Chiropractic'):
    	msg="It sounds like you need help with Chiropractic,The following link will help you. <a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10288' target='_blank' style='color:white'> Click Here</a> to find more details "
    elif(currentIntent=='Pharmacy'):
    	msg="It sounds like you need help with Pharmacy,The following link will help you. <a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10345' target='_blank' style='color:white'> Click Here</a> to find more details "
    elif(currentIntent=='Medical_Product_Search'):
    	msg="It sounds like you need help with Medical_Product_Search,The following link will help you. <a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10081' target='_blank' style='color:white'> Click Here</a> to find more details "
    elif(currentIntent=='ER_Hospital'):
    	msg="It sounds like you need help with Emergency Care/Hospitals,The following link will help you. <a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10078' target='_blank' style='color:white'> Click Here</a> to find more details"
    elif(currentIntent=='Medical_Supplier'):
    	msg="It sounds like you need help with Medical Supplier,The following link will help you. <a href='https://www.centraleasthealthline.ca/listServices.aspx?id=10078' target='_blank' style='color:white'> Click Here</a> to find more details "
    elif(currentIntent=='Good_Bye'):
    	msg="You are welcome.Have a good one. :)"
    else:
    	msg="Sorry I cannot understand you,Please type a valid query.If you need more help please visit our website <a href='https://www.thehealthline.ca/ ' target='_blank' style='color:white'> Click Here</a> to find more details"

    return str(msg)


def predict(msg,classes,model):
	
	originalintent=model.predict(count_vect.transform([msg]))
	return originalintent[0]  

if __name__ == "__main__":
    app.run()

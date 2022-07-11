#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib
from flask import Flask 
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from flask import render_template, request 
import numpy as np


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        num_adults = request.form.get("adults")
        num_children= request.form.get("children")
        SGD_amount = request.form.get("price")
        stay_duration = request.form.get("duration")
        book_duration = request.form.get("book")
        
        
        num_adults=int(num_adults)
        num_children = int(num_children)
        SGD_amount = float(SGD_amount)
        stay_duration = int(stay_duration)
        book_duration = int(book_duration)
        
        first_time = request.form['first_time']
        if (first_time=='Yes'):
            first_time=1
        else:
            first_time=0
        
        branch = request.form.get('branch')
        if(branch=='Orchard'):
            branch_Orchard=1
            branch_Changi=0
        else:
            branch_Changi=1
            branch_Orchard=0
            
        country = request.form.get("country")
        if(country=='Australia'):
            country_Australia=1
            country_China=0
            country_India=0
            country_Indonesia=0
            country_Japan=0
            country_Malaysia=0
            country_Singapore=0
        elif(country=='China'):
            country_Australia=0
            country_China=1
            country_India=0
            country_Indonesia=0
            country_Japan=0
            country_Malaysia=0
            country_Singapore=0
        elif(country=='India'):
            country_Australia=0
            country_China=0
            country_India=1
            country_Indonesia=0
            country_Japan=0
            country_Malaysia=0
            country_Singapore=0
        elif(country=='Indonesia'):
            country_Australia=0
            country_China=0
            country_India=0
            country_Indonesia=1
            country_Japan=0
            country_Malaysia=0
            country_Singapore=0
        elif(country=='Japan'):
            country_Australia=0
            country_China=0
            country_India=0
            country_Indonesia=0
            country_Japan=1
            country_Malaysia=0
            country_Singapore=0   
        elif(country=='Malaysia'):
            country_Australia=0
            country_China=0
            country_India=0
            country_Indonesia=0
            country_Japan=0
            country_Malaysia=1
            country_Singapore=0 
        else:
            country_Australia=0
            country_China=0
            country_India=0
            country_Indonesia=0
            country_Japan=0
            country_Malaysia=0
            country_Singapore=1
        
        room = request.form.get('room')
        if(room=='King'):
            room_King=1
            room_President_Suite=0
            room_Queen=0
            room_Single=0
        elif(room=='President_Suite'):
            room_King=0
            room_President_Suite=1
            room_Queen=0
            room_Single=0
        elif(room=='Queen'):
            room_King=0
            room_President_Suite=0
            room_Queen=1
            room_Single=0
        else:
            room_King=0
            room_President_Suite=0
            room_Queen=0
            room_Single=1
        
        platform = request.form.get('platform')
        if(platform=='Agent'):
            platform_Agent=1
            platform_Email=0
            platform_Phone=0            
            platform_Website=0
        elif(platform=='Email'):
            platform_Agent=0
            platform_Email=1
            platform_Phone=0            
            platform_Website=0
        elif(platform=='Phone'):
            platform_Agent=0
            platform_Email=0
            platform_Phone=1            
            platform_Website=0
        else:
            platform_Agent=0
            platform_Email=0
            platform_Phone=0            
            platform_Website=1
            
        
        
        print(first_time, num_adults, num_children, SGD_amount, branch_Changi, branch_Orchard)
        
        modelDT = joblib.load("decisiontree")
        predDT = modelDT.predict([[first_time, num_adults, num_children, SGD_amount, 
                                   branch_Changi, branch_Orchard, country_Australia,country_China,country_India,
                                   country_Indonesia,country_Japan,country_Malaysia,country_Singapore,
                                   room_King, room_President_Suite, room_Queen, room_Single,
                                   platform_Agent, platform_Email, platform_Phone, platform_Website,
                                   book_duration, stay_duration]])
        
        
        modelXGB = joblib.load("xgboost")
        predXGB = modelXGB.predict(np.array([[first_time, num_adults, num_children, SGD_amount, 
                                              branch_Changi, branch_Orchard, country_Australia,country_China,country_India,
                                              country_Indonesia,country_Japan,country_Malaysia,country_Singapore,
                                              room_King, room_President_Suite, room_Queen, room_Single,
                                              platform_Agent, platform_Email, platform_Phone, platform_Website,
                                              book_duration, stay_duration]]))

        modellgbm = joblib.load("lgbm")
        modellgbm = modellgbm.predict(np.array([[first_time, num_adults, num_children, SGD_amount, 
                                              branch_Changi, branch_Orchard, country_Australia,country_China,country_India,
                                              country_Indonesia,country_Japan,country_Malaysia,country_Singapore,
                                              room_King, room_President_Suite, room_Queen, room_Single,
                                              platform_Agent, platform_Email, platform_Phone, platform_Website,
                                              book_duration, stay_duration]]))
        
        
        s3 = "The no-show prediction based on Decision Tree Model is " + str(predDT) + ". The potential loss amount is SGD$" + str(SGD_amount)
        s2 = "The no-show prediction based based on XGBoost Model is " + str(predXGB) + ". The potential loss amount is SGD$" + str(SGD_amount)
        s1 = "The no-show prediction based based on LightGBM Model is " + str(modellgbm) + ". The potential loss amount is SGD$" + str(SGD_amount)


        
        return(render_template("index.html", Result1=s1, Result2=s2, Result3=s3))
    else:
        return(render_template("index.html", Result1=" ", Result2=" ", Result3=" "))


# In[4]:


if __name__ == "__main__":
    app.run()


# In[ ]:





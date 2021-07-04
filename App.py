#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import datetime
import keras
import pandas as pd
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta


# In[3]:


month=[]
day=[]
week=[]
hour=[]
minute=[]
st.title('EV Charging station usage')
terminal = st.selectbox("Please select one of the terminals: ",
                     ['S7-T1', 'S2-T1', 'S19-T1', 'S56-T3', 'S85-T3','S16-T3', 'S16-T1',
                     'S94-T3', 'S28-T1', 'S62-T3', 'S14-T3', 'S8-T1', 'S8-T3', 'S34-T3',
                     'S6-T2', 'S29-T3', 'S64-T1', 'S11-T1', 'S76-T3', 'S59-T1'])
 
# print the selected hobby
st.write("You Selected : ", terminal)

d = st.date_input("Please Select the date", datetime.date(2019, 11, 1), min_value=datetime.date(2019, 11, 1), 
                  max_value=datetime.date(2021, 2, 1)) 
st.write('Your selected date is:', d)

t = st.time_input('Please select the time', datetime.time(8, 45))
st.write('Your selected time is:', t)
month.append(d.month)
day.append(d.day)
week.append(d.weekday())
hour.append(t.hour)
minute.append(t.minute)

# Create a button, that when clicked, shows a text
if(st.button("Please Submit the data")):
    start = timer()
    if terminal in ['S7-T1', 'S19-T1', 'S85-T3', 'S28-T1', 'S62-T3']:
        
        st.text("This terminal is: DOWN")
        end = timer()
        st.write("Time taken in seconds:", timedelta(seconds=end-start))
    else:

        X_test=pd.DataFrame(list(zip( month, week, day, hour, minute)),
             columns =['Month_name', 'Week_number', 'Date', 'Hour', 'Minute'])
        
        #st.write("This terminal is: ", X_test)
        reconstructed_model = keras.models.load_model(terminal)
        y_pred=reconstructed_model.predict(X_test)
        val_predict=np.argmax(y_pred, axis=1) 
        #st.write("This terminal is: ", y_pred)
        if val_predict==0:
            text='Available'
        elif val_predict==1:
            text='Charging'
        elif val_predict==2:
            text='Passive'
        elif val_predict==3:
            text='Offline'
        else:
            text='Down'
        st.write("This terminal is: ", text)
        end = timer()
        st.write("Time taken in seconds:" ,timedelta(seconds=end-start))


# In[ ]:





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:20:36 2024

@author: mmoreira
"""



### Correction du TD avec la librairie streamlit


import streamlit as st
import requests
from io import BytesIO
from PIL import Image, ImageDraw

import config
adresse = f'https://api.nasa.gov/planetary/apod?api_key={config.NASA_API_KEY}'



def getimage(adresse):
    
    adresse=adresse+'&date='+datechoisie
    response = requests.get(adresse)
    data=response.json()
    url=data['url']
    legende=data['explanation']
    res = requests.get(url)
    image=res.content
    image = Image.open(BytesIO(image))
    return image,legende
     
st.title("The astronomy picture of the Day provided by NASA")
datechoisie = st.date_input("Date ?")
datechoisie=str(datechoisie)
st.write("date choisie:", datechoisie)
image,legende=getimage(adresse)
st.image(image)
st.caption(legende)


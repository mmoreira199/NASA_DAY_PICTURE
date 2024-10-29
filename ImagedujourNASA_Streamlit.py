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


def getimage():
    adresse='https://api.nasa.gov/planetary/apod?api_key=vBsbRn3IvW8j1Mnn3n4Aj3ReLJs9b1AKh37rQa1N'
    adresse=adresse+'&date='+datechoisie
    response = requests.get(adresse)
    data=response.json()
    url=data['url']
    legende=data['explanation']
    res = requests.get(url)
    image=res.content
    image = Image.open(BytesIO(image))
    return image,legende
     

datechoisie = st.date_input("Date ?")
datechoisie=str(datechoisie)
st.write("date choisie:", datechoisie)
image,legende=getimage()
st.image(image)
st.caption(legende)


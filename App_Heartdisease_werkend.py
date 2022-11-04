from turtle import onclick

import keras.models
import streamlit as st
import pandas as pd
import numpy as np



# Start pagina
def start():

    # Functionaliteit
    def switch():
        st.session_state["page"] = "questionair"

    # UI
    from PIL import Image
    image = Image.open('CVD_NSHomepageWidget.jpg')

    st.image(image, caption=None, width=None, use_column_width='auto', clamp=False, channels="RGB", output_format="auto")

    st.title("Heart Disease")
    st.header("Heeft u een hartziekte?")
    st.markdown("Volgens de CDC is hartziekte een van de belangrijkste doodsoorzaken voor mensen van de meeste rassen in de VS (Afro-Amerikanen, Amerikaanse Indianen en Alaska Natives, en blanken). Ongeveer de helft van alle Amerikanen (47%) heeft ten minste 1 van de 3 belangrijkste risicofactoren voor hartaandoeningen: hoge bloeddruk, hoog cholesterolgehalte en roken. Andere belangrijke indicatoren zijn diabetesstatus, zwaarlijvigheid (hoge BMI), te weinig lichaamsbeweging of te veel alcohol drinken. Het opsporen en voorkomen van de factoren die de grootste impact hebben op hart- en vaatziekten is erg belangrijk in de gezondheidszorg. Computationele ontwikkelingen maken op hun beurt de toepassing van machine learning-methoden mogelijk om patronen uit de gegevens te detecteren die de toestand van een patiënt kunnen voorspellen. ")

    st.header("Hoe doen we dat?")
    st.markdown("Om een diagnose te kunnen stellen dient u een aantal vragen te beantwoorden van onze vragenlijst. Deze kunt u via de **Start** knop bereiken. "
                "Nadat u dit gedaan heeft worden u antwoorden vergeleken met de historische data van andere mensen met een hartziekte om een voorspelling te geven. ")
    st.caption("**Alle data die u invult wordt niet opgeslagen en is op geen enkele manier naar u terug te leiden**")

    button1 = st.button("Start", on_click=switch)

# Vragenlijst pagina
def questionair():

    # Functionaliteit
    def switch():
        st.session_state["page"] = "results"

    # UI
    st.title("Vragenlijst")

    # BMI Calculator
    # gewicht / lengte ^2
    gewicht = st.slider("Hoeveel kg weegt u?", 1,150, step=1)
    lengte = st.slider("Hoe lang bent u in meter?", 0.8, 2.5)
    st.session_state["data"]["BMI"] = [int(gewicht/(lengte*lengte))/94.85]
    st.write("U heeft een BMI van: ", st.session_state["data"]["BMI"][0]*94.85)



    #Gender
    sex = st.radio("Bent u man of vrouw?", ["Man", "Vrouw"])
    st.session_state["data"]["Male"] = [int(sex == "Man")]
    st.session_state["data"]["Female"] = [int(sex == "Vrouw")]

    #Leeftijd
    Age = st.slider('Hoe oud bent u?', 18, 110)
    st.write("Ik ben", Age, 'jaar oud.')
    if Age >= 18 and Age <= 24:
        st.session_state["data"]["AgeCategory"] = [0]

    if Age >= 25 and Age <= 29:
        st.session_state["data"]["AgeCategory"] = [1/12]

    if Age >= 30 and Age <= 34:
        st.session_state["data"]["AgeCategory"] = [2/12]

    if Age >= 35 and Age <= 39:
        st.session_state["data"]["AgeCategory"] = [3/12]

    if Age >= 40 and Age <= 44:
        st.session_state["data"]["AgeCategory"] = [4/12]

    if Age >= 45 and Age <= 49:
        st.session_state["data"]["AgeCategory"] = [5/12]

    if Age >= 50 and Age <= 54:
        st.session_state["data"]["AgeCategory"] = [6/12]

    if Age >= 55 and Age <= 59:
        st.session_state["data"]["AgeCategory"] = [7/12]

    if Age >= 60 and Age <= 64:
        st.session_state["data"]["AgeCategory"] = [8/12]

    if Age >= 65 and Age <= 69:
        st.session_state["data"]["AgeCategory"] = [9/12]

    if Age >= 70 and Age <= 74:
        st.session_state["data"]["AgeCategory"] = [10/12]

    if Age >= 75 and Age <= 79:
        st.session_state["data"]["AgeCategory"] = [11/12]

    if Age >= 80:
        st.session_state["data"]["AgeCategory"] = [12/12]

    #Roken
    Smoking = st.radio("Heeft u in uw leven meer dan 100 sigaretten gerookt?", ["Ja", "Nee"])
    st.session_state["data"]["Smoking"] = [int(Smoking == "Ja")]

    #Diabtic
    Diabetic = st.radio("Heeft u diabetis?", ["Ja", "Nee"])
    st.session_state["data"]["Diabetic"] = [int(Diabetic == "Ja")]

    # physical activity
    PhysicalActivity = st.radio("Heeft u sportief?", ["Ja", "Nee"])
    st.session_state["data"]["PhysicalActivity"] = [int(PhysicalActivity == "Ja")]

    # Asthma
    Asthma = st.radio("Heeft u asthma?", ["Ja", "Nee"])
    st.session_state["data"]["Asthma"] = [int(Asthma == "Ja")]

    # kidney disease
    KidneyDisease = st.radio("Heeft u een nier ziekte?", ["Ja", "Nee"])
    st.session_state["data"]["KidneyDisease"] = [int(KidneyDisease == "Ja")]

    #SkinCancer
    SkinCancer = st.radio("Heeft u huidkanker?", ["Ja", "Nee"])
    st.session_state["data"]["SkinCancer"] = [int(SkinCancer == "Ja")]

    #Alcohol
    AlcoholDrinking = st.radio("Drinkt u veel alcohol? (Mannen >= 14 drankjes per week en vrouwen >= 7 drankjes per week)", ["Ja", "Nee"])
    st.session_state["data"]["AlcoholDrinking"] = [int(AlcoholDrinking == "Ja")]

    #Beroerte
    Stroke = st.radio("Heeft u ooit een beroerte gehad?", ["Ja", "Nee"])
    st.session_state["data"]["Stroke"] = [int(Stroke == "Ja")]

    #Psychische gezondheid
    p_gezondheid = st.session_state["data"]["PhysicalHealth"] = [st.slider("in de afgelopen 30 dagen, hoeveel heeft u zich psychisch 'slecht' gevoeld? (0 = Weinig, 30 = Veel)",
                                                        0, 30)/30]
    st.write("Ik heb me de afgelopen 30 dagen,", p_gezondheid[0]*30, 'dagen slecht gevoeld.')

    # Mentale gezondheid
    m_gezondheid = st.session_state["data"]["MentalHealth"] = [st.slider(
        "in de afgelopen 30 dagen, hoeveel heeft u zich mentaal 'slecht' gevoeld? (0 = Weinig, 30 = Veel)",
        0, 30)/30]
    st.write("Ik heb me de afgelopen 30 dagen,", m_gezondheid[0]*30, 'dagen slecht gevoeld.')

    # Moeite met lopen
    DiffWalking = st.radio("Heeft u moeite met lopen en of traplopen?", ["Ja", "Nee"])
    st.session_state["data"]["DiffWalking"] = [int(DiffWalking == "Ja")]

    #GenHealth
    GenHealth = st.slider('Hoe voelt u zich?(0 is slecht en 4 is excellent)', 0, 4)

    if GenHealth == 0:
        generalhealth = "slecht"
    elif GenHealth == 1:
        generalhealth = "gemiddeld"
    elif GenHealth == 2:
        generalhealth = "goed"
    elif GenHealth == 3:
        generalhealth = "zeer goed"
    elif GenHealth == 4:
        generalhealth = "perfect"
    else:
        generalhealth = ""

    st.write("Ik voel me ", generalhealth)
    st.session_state["data"]["GenHealth"] = [int(GenHealth)/4]

    # Sleeptime
    Sleeptime = st.slider('Hoeveel uur slaapt u', 0, 12)
    st.write("Ik slaap gemiddeld : ", Sleeptime)
    st.session_state["data"]["SleepTime"] = [int(Sleeptime)/24]

    #st.write(st.session_state["data"])

    button2 = st.button("Kans op hartziekte", on_click=switch)


# Resultaat pagina

def results():
    st.title("Resultaten")

    #Functionaliteit
    def switch():
        st.session_state["page"]= "questionair"

    def result():
        model = keras.models.load_model("./model")
        data = st.session_state["data"]
        result = model.predict(pd.DataFrame(data))
        return result

    st.write(f"{(int(result()[0][0] * 100))}%")
    st.progress(int(result() * 100))
    button3 = st.button("opnieuw", on_click=switch)

#UI
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, red , green);
        }
    </style>""",
    unsafe_allow_html=True,
    )


pages = {
    "start" : start,
    "questionair" : questionair,
    "results" : results
}

if "page" not in st.session_state:
    st.session_state["page"] = "start"
    st.session_state["data"] = {}

pages[st.session_state["page"]]()
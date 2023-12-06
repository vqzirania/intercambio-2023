import streamlit as st
# from streamlit.logger import get_logger
import json

# '''
# To fix constant rebooting
# write pairs inro a json,
# then read out of it.
# '''

# LOGGER = get_logger(__name__)
st.title(":santa::gift: Intercambio de Regalos 2023")
st.markdown(
    """
    Vamos a hacer el sorteo para el intercambio de regalos de este año atraves de este link. \n
    Las mamas de niños pequeños, pueden ingresar el nombre de su hijo(a) abajo, para ver el nombre de la persona que le toca. 
    """
    )

st.warning(
    """
    **ATTENCION:** Anota el nombre que te toco. Se borrara el nombre de el registro despues de poner tu nombre. \n
    Si hay un fallo en el programa, contacten a Irania :smile: 
    """
    )


# PARTICIPANTS

fams = [
        ["IRANIA", "JHOVANNA", "DOMINGO", "GUADALUPE"],
        ["MARIA", "CHRISTIAN"],
        ["OSCAR", "JASMIN", "AXEL", "ANTHONY"],
        ["MARICELA", "PATO", "LENNY","VANESSA","ISABELLA"],
        ["ALEJANDRA","JUAN","JOHANNA","JARE", "JAYLIN"],
        ["OLIVIA","FREDDY","FRIDA","KENDRA"],
        ["MAMA CHUCHA","PAPA GERARDO"]
        
        ]

names = sum(fams, []) # makes one list from lists of lists
st.write("Las personas participando son:", names)


# CREATING PAIRINGS
# in secret santa.py file


# ENTERING NAME + DISPLAYING PAIR
person = st.text_input("**Ingresa tu nombre aqui:**").upper()

# Opening the json file
with open("pairs.json", "r") as pairings:
    ss_result = json.load(pairings)

# Trying to get the pair
try:  
    if st.button("Listo"):
        # Since the variable "result" is a dictionary,
        # pop, gives the value of the key and removes it from the dictionary
        result = ss_result.pop(person)
        st.success("Listo " + person + ", la persona a quien te toco es: " + result)
        st.balloons()

except KeyError:
    st.error("Esta persona no esta en la lista de participantes, o ya ha visto la persona que le toca.")

# REMOVING NAMES FROM THE LIST

# print(ss_result[person])
# del ss_result[person]
# popoutnames = []
# popoutnames.append(person)
# st.write("Las personas que ya han visto la persona que le toca son:", popoutnames)

# # print(ss_result)




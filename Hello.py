import streamlit as st
# from streamlit.logger import get_logger
import json

# '''
# To fix constant rebooting
# write pairs inro a json,
# then read out of it.
# '''

# LOGGER = get_logger(__name__)

#  TAB DISPLAY
st.set_page_config(
    page_title="Navidad 2023",
    page_icon="🎄",
)

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

    ** NO PONGAN EL NOMBRE DE OTRA PERSONA! ** - Si no, la persona no va poder ver quien le toco.
      \n Credo por Irania :smile: 
      """
    )


## PARTICIPANTS
# PASTE INTO SECRET SANTA
fams = [
        ["IRANIA", "JHOVANNA", "DOMINGO", "GUADALUPE"],
        ["MARIA", "CHRISTIAN"],
        ["OSCAR", "JASMIN", "AXEL", "ANTHONY"],
        ["MARICELA", "PATO", "LENNY","VANESSA","ISABELLA"],
        ["ALEJANDRA VAZQUEZ","JUAN","JOHANNA","YARE", "JAYLIN"],
        ["PEPE", "JESSICA", "MATEO","JIROSHI","MAX"],
        ["OLIVIA","FREDDY","FRIDA","KENDRA"],
        ["ALEJANDRA MENDEZ","TITO","DAVID"],
        ["MAMA CHUCHA","PAPA GERARDO"],
        ["TONIO"]
        
        ]

# Making a nice list of names
names = sum(fams, []) # makes one list from lists of lists

names_displayed = ["IRANIA", "JHOVANNA", "DOMINGO", "GUADALUPE","MARIA", "CHRISTIAN","OSCAR", "JASMIN", "AXEL (8 años)", "ANTHONY (5 años)","MARICELA", "PATO", "LENNY (6 años)","VANESSA (3 años)","ISABELLA (BABY)","ALEJANDRA VAZQUEZ","JUAN","JOHANNA (16 años)","YARE (6 años)", "JAYLIN (5 años)","OLIVIA","FREDDY","FRIDA (4 años)","KENDRA (9 años)","MAMA CHUCHA","PAPA GERARDO","TONIO", "PEPE", "JESSICA", "MATEO (16 años)","JIROSHI (12 años)","MAX (6 años)","ALEJANDRA MENDEZ","TITO","DAVID (5 años)"]
st.write("Las personas participando son:", names_displayed)


## CREATING PAIRINGS
# RUN in secret santa.py file


# ENTERING NAME + DISPLAYING PAIR
person = st.text_input("**Ingresa tu nombre aqui:**").upper()

# Opening the json files
with open("pairs.json", "r") as pairings:
    ss_result = json.load(pairings)

with open("viewers.json", "r") as viewed:
    # Splitlines creates a list after reading a file
    popoutnames_list = viewed.read().splitlines()

# Trying to get the pair
try:  
    if st.button("Listo"):
        # Check if its their FIRST TIME they are on original list
        if person in ss_result:
            # Since the variable "result" is a dictionary,
            # pop, gives the value of the key and removes it from the dictionary
            result = ss_result.pop(person)
            st.success("Listo " + person + ", la persona a quien te toco es: " + result)
            st.balloons()

            # SAVING TO THE LIST OF PEOPLE WHO ALREADY VIEWED - PARTICIPATED - by appending
            with open("viewers.json", "a") as viewed:
                viewed.write(person + "\n")

        # Check if wrong spelling
        elif person not in names:
            st.error("Esta persona no esta en la lista de participantes. Usa la lista de participantes como guia y corrige tu otographia.")
        
        # They already viewed
        else:
            st.error("Ya has visto la persona que te toca.")

# If they arent on the original list using their correct name
except KeyError:
    st.error("Ocurrio un error. Contacta Irania")


# WHO HAS VIEWED
if popoutnames_list ==[]:
    st.info("Se la primer persona en participar! :tada:")
else:
    st.write("Las personas que ya han visto la persona que le toca son:", popoutnames_list)





# SAVING THE ERASED NAMES OF PEOPLE TO JSON
# This is to avoid others from looking up who others got
with open("pairs.json", "w") as pairings:
    json.dump(ss_result,pairings)


# GETTING SIZES AND INFO
# st.write("##### Dale un poco de informacion a la persona que te dara un regalo. :hugging_face:")

# person = st.text_input('Confirma tu nombre, escrito como esta en la lista de participantes:')
# shirt_size = st.text_input('Cual es tu talla de camisa?')
# pants_size = st.text_input('Cual es tu talla de pantalon?')
# shoe_size = st.text_input('Cual es tu talla de zapato? (talla US)')

# with open("sizes.json", "w") as
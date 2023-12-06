import streamlit as st
from streamlit.logger import get_logger
import copy
import random

LOGGER = get_logger(__name__)
st.title("Intercambio de Regalos 2023")
st.subheader("Vamos a hacer el sorteo para el intercambio de regalos de este año atraves de este link. \n Las mamas de niños chiquitos, pueden ver el nombre de la persona que va a recibir regalo de su hijo(a), ingresando el nombre de su hijo(a) abajo.")

st.warning("**ATTENCION:** Anota el nombre que te toco. Se borrara el nombre de el registro despues de poner tu nombre.")


# PARTICIPANTS
# fam1 = ["Irania", "Jhovanna", "Domingo", "Guadalupe"]
# fam2 = ["Maria", "Christian"]
# fam3 = ["Oscar", "Jazmin", "Axel", "Anthony"]

fams = [
        ["IRANIA", "JHOVANNA", "DOMINGO", "GUADALUPE"],
        ["MARIA", "CHRISTIAN"],
        ["OSCAR", "JASMIN", "AXEL", "ANTHONY"]
        
        ]

names = sum(fams, []) # makes one list from lists of lists
st.write("Las personas participando son:", names)


# CREATING PAIRINGS
def secret_santa(names):
    my_list = fams
    choose = copy.copy(names) 
    
    # my_list = names
    # choose = copy.copy(my_list) # copy.deepcopy() for classes
    
    result = {}
    for fam in my_list:
        # print("this is fam", fam)
        names = copy.copy(my_list)
        
        # print('this is the original names:', names)
        names.pop(names.index(fam)) # Removes a person from choosing themself # With Fam, removes the whole fam from being selected by one another
        names = sum(names,[]) # Removing lists from lists
        # print('names after pop:', names)
        for person in fam:
            # print(person)
            chosen = random.choice(list(set(choose)&set(names)))
            # print(list(set(choose)&set(names)))
            result[person] = chosen
            choose.pop(choose.index(chosen))
    return result

ss_result = secret_santa(names)
# print('results:', ss_result)


# ENTERING NAME + DISPLAYING PAIR
person = st.text_input("**Ingresa tu nombre aqui:**").upper()
if st.button("Listo"):
    result = ss_result.pop(person)
    st.success("Listo " + person + ", la persona a quien te toco es: " + result)


#popoutnames = 
#st.write("las personas que ya han visto la persona que le toca son:", popoutnames)






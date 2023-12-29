#¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ #
#           Library            #
#_____ _____ _____ _____ _____ #

# General Libraries
import ssl
from model_pipeline import generate_text_from

# Streamlit requierements
from collections import namedtuple
import altair as alt
import streamlit as st
from streamlit import components


#¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨#
# #¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ #  #
# #      Fonctions Streamlit     #  #
# #_____ _____ _____ _____ _____ #  #
#_____ _____ _____ _____ _____ _____#

#¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ #
#          Customize.          #
#_____ _____ _____ _____ _____ #

ssl._create_default_https_context = ssl._create_unverified_context

model_name = 'Open llama'
mail = 'gauthier.r@devlaunchers.com'
link = 'https://www.linkedin.com/in/gauthier-rammault/'

page_title = f"Play with {model_name}."
page_comment = f''':blue[Beta]: If you have any questions, send me an [e-mail]({mail}) or text me on [LinkedIn]({link}).'''

default_title_input = "Your question here:"
default_text_input = "Explain to me the difference between nuclear fission and fusion."
button_title = f"Ask to {model_name}"


#¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ #
#        Streamlit page        #
#_____ _____ _____ _____ _____ #

def main():
    # Streamlit page configuration
    st.set_page_config(page_title=f'{model_name} model', page_icon="🔮", layout="wide")

    # Main content
    st.title(page_title, anchor=None)

    # User input
    input_text = st.text_input(default_title_input, default_text_input)

    # Button click event
    if st.button(button_title):
        result = generate_text_from(input_text)
        st.text("Answer: {}".format(result))

    # Page comment
    st.caption(page_comment)

if __name__ == '__main__':
    main()
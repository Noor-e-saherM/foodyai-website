import streamlit as st
from  PIL import Image
import pandas as pd
#from pandas.io.formats.style import styler

#Brand logo images
image1 = Image.open("data/Logo.PNG")
image2 = Image.open("data/Logo2.PNG")


#Two columns with different width
col1, col2 = st.columns( [0.8, 0.2])

with col1:               #To display brand logo
    st.image(image1,  width=500)

with col2:
    pass


# To display the header text using css style
st.markdown(""" <style> .font {
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;}
    </style> """, unsafe_allow_html=True)

st.markdown('<p class="font">Upload a picture of your meal and get a nutrition fact .....</p>', unsafe_allow_html=True)

#Using the file uploader to upload an image and specifying the types that can be uploaded.
uploaded_file = st.file_uploader("Select an image:", type=['jpg','png','jpeg'])

#If an image is uploaded, it will do the following steps.
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    #Since images cannot be centered with streamlit; Create three columns with differnt widths to center the image.
    col1, col2, col3 = st.columns([3.5,8,1])

    with col1:
        st.write("")

    with col2:
        st.image(image, width=300)

    with col3:
        st.write("")

    #The following displays the nutrition information.
    st.markdown(""" <style> .fontt {
    font-size:23px ; font-family: 'Cooper Black'; text-align: center; color: #FF9633;}
    </style> """, unsafe_allow_html=True)

    st.markdown('<p class="fontt">Your Nutrition Data </p>', unsafe_allow_html=True)

    st.markdown(""" <style> .fontt1 {
    font-size:23px ; font-family: 'Cooper Black'; text-align: center; }
    </style> """, unsafe_allow_html=True)

    st.markdown('<p class="fontt1">Category of the food: Cheese </p>', unsafe_allow_html=True)

    @st.cache
    def get_dataframe_data():

        return pd.DataFrame(
        {
            "name": ["Cheese"],
            "serving size": ["camembert"],
            "calories": ["100 g"],
            "total fat": ["300"],
            "saturated fat": ["24 g"],
            "cholestrol": ["15 g"],
            "sodium": ["59.00 mg"],
            "choline": ['69.3 mg'],
            "folate": ['22.00 mg'],
            "protein": ["0.26 g"]
        }
    )

    df = get_dataframe_data()

    #Pandas styler to hide the index of the dataframe.
    styler = df.style.hide_index()

    st.write(styler.to_html(), unsafe_allow_html=True)

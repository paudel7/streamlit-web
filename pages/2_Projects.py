import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title ("Projects")
st.subheader(":blue[Earthquake Data Explorer] :sunglasses:")
st.text('Get ready for exploration of Earthquake Data')
#new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
#st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')

#st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Use Navigation for Exploring Data')
    else:
        st.header('To begin upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

    # def charting():
    #     st.header('Charting')
    #     chart_data = pd.DataFrame(
    #     #np.random.randn(20, 3),
    #     columns=(x=df['Date'], y=df['Magnitude'])
    #     st.bar_chart(columns)

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot():
    st.header('Plot of Data')

    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data')
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Charting', 'Data Header', 'Scatter Plot'])

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Scatter Plot':
    displayplot()
elif options == 'Charting':
    charting()


def displayplot():
    st.header('Plot of Data')

    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)

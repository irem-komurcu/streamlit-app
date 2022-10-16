import numpy as np
import pandas as pd
import streamlit as st
import plotly.figure_factory as ff


data = pd.read_csv("twitter.csv", sep=",")

with st.sidebar:
    st.write("Do you like this app?")
    cbox = st.checkbox('yes')


def tabs(default_tabs = [], default_active_tab=0):
    if not default_tabs:
        return None

    active_tab = st.radio("", default_tabs, index=default_active_tab, key='tabs')
    child = default_tabs.index(active_tab)+1

    st.markdown("""  
        <style type="text/css">
        div[role=radiogroup] > label > div:first-of-type, .stRadio > label {
        display: none;               
        }
        div[role=radiogroup] {
            flex-direction: unset
        }
        div[role=radiogroup] label {             
            border: 1px solid #999;
            background: #EEE;
            padding: 4px 12px;
            border-radius: 4px 4px 0 0;
            position: relative;
            top: 1px;
            }
        div[role=radiogroup] label:nth-child(""" + str(child) + """) {    
            background: #FFF !important;
            border-bottom: 1px solid transparent;
        }            
        </style>
    """, unsafe_allow_html=True)        

    return active_tab

active_tab = tabs(["Light Side", "Dark Side"])


if st.sidebar.button('Get Results'): 
    if cbox:
        if (active_tab == "Light Side"):
            st.write(data)
            st.dataframe(data["Tweet Impressions"]) 
            st.table(data)
        else: 
            layout = st.columns([1, 2])
            with layout[0]: 
                st.write("Column A")

            with layout[-1]: 
                st.write("Column B")


st.line_chart(data['Tweets'])
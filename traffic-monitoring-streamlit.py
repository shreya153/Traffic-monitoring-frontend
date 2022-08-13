import streamlit as st
import pandas as pd

Title= st.title("TRAFFIC MONITORING SYSTEM")
Sidebar = st.sidebar.title("Menu")
Menu = st.sidebar.selectbox("Choose one",("Live Stream","Database","Analysis"))

if Menu == "Live Stream":
    #---Live streeam code
    st.title("Live Streaming")
    st.title("Add your live streaming code in first if condition")

elif Menu == "Database":
    #---Database manipulation
    st.title("Log")
    st.title("Add and manipulate the database in Database elif condition")
else:
    #---Database analysis
    st.title("Analysis")
    st.markdown("---")
    Numberofin = st.title("In Vehicle")
    nin = st.title("--")
    Numberofout = st.title("Out Vehicle")
    nout = st.title("--")
    st.bar_chart((1,2,3,4,2,3,1,5,1))
import streamlit as st
import register
import login

user_color      = '#0000987'
title_webapp    = "Visitor Monitoring Webapp"

html_temp = f"""
            <div style="background-color:{user_color};padding:12px">
            <h1 style="color:white;text-align:center;">{title_webapp}
            </h1>            
            </div>
            """
st.markdown(html_temp, unsafe_allow_html=True)

registerTab, loginTab = st.tabs(["Register", "Login"])



with registerTab:
    register.register()
with loginTab:
    login.login()
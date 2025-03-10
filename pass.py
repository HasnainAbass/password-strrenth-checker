import streamlit as st
import pandas as pd 
import re

st.set_page_config(page_title="Password Strenth Checker", page_icon=":lock:" , layout="centered", initial_sidebar_state="expanded")
st.title( "🔐 Password Strenth Checker")
st.markdown("""
## wellcom to the Ultimate Password Strenth Checker 👋!
use the simple tool to check of your password and get suggestions on how to make it stronger.
            we will give helpful tips to create a **Strong Password** 🔏""") 

password = st.text_input("Please Enter your Password Here" , type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    if re.search("[A-Z]", password) and re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain both upper and lower case characters")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one digit")
    if re.search(r"[@#$%&*:\.]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one special character")
    if score == 4:
        feedback.append("🟢 Your Password is strong 👍 ")
    elif score == 3:
        feedback.append("🟡 Your Password is medium strength it could be stronger ")
    else:
        feedback.append("🔴 Your Password is weak Please make it stronger")
    if feedback:
        st.markdown("## improvements sagustions")
        for tip in feedback:
            st.write(tip)
else:
    st.write("Please enter a password to check its strength")
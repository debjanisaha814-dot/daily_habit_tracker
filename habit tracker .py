import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash")
st.title("Your Daily Habit Tracker")

name = st.text_input("Enter your name:")

# 1️⃣ Water Question
if st.checkbox("Did you drink at least 8 glasses of water today?"):
    choice = st.radio("Pick one:", ["Yes", "No"])

    if choice == "Yes":
        st.success("8 glasses of water keep your body hydrated, boost energy, support digestion, and improve skin health.")
    else:
        st.error("Try to drink more water!")

# 2️⃣ Study Question
if st.checkbox("Did you use any of your free time today to study or learn for one hour?"):
    choice = st.radio("Pick one:", ["Yes", "No"])

    if choice == "Yes":
        st.success("Awesome! Studying improves your knowledge and focus.")
    else:
        st.error("It’s okay — you can start something new tomorrow!")

# 3️⃣ Exercise Question
if st.checkbox("Did you exercise or walk for at least 20 minutes?"):
    choice = st.radio("Pick one:", ["Yes", "No"])

    if choice == "Yes":
        st.success("Exercise improves heart health, boosts energy, reduces stress, and strengthens muscles and mood.")
    else:
        st.error("Not exercising can lead to low energy and health risks.")

# 4️⃣ Healthy Meal Question
if st.checkbox("Did you eat healthy meals today?"):
    choice = st.radio("Pick one:", ["Yes", "No", "Somewhat"])

    if choice == "Yes":
        st.success("Great! Eating healthy keeps your body strong.")
    elif choice == "No":
        st.error("Try to reduce junk food tomorrow!")
    elif choice == "Somewhat":
        st.warning("Not bad! A little improvement will help a lot.")

# 5️⃣ Sleep Question
if st.checkbox("Did you sleep for at least 7 hours last night?"):
    choice = st.radio("Pick one:", ["Yes", "No"])

    if choice == "Yes":
        st.success("Sleeping 7 hours improves mood, boosts energy, and supports recovery.")
    else:
        st.error("Lack of sleep causes tiredness, poor focus, and more stress.")

# 6️⃣ Productivity Question
if st.checkbox("Did you do anything productive today, like work or studying?"):
    choice = st.radio("Pick one:", ["Yes", "No"])

    if choice == "Yes":
        st.success("Great! Staying productive builds discipline.")
    else:
        st.error("Try to do something productive tomorrow!")

# 7️⃣ Study Time Question
study_time = st.number_input("How many hours did you study today?", min_value=0.0)
st.write(f"You studied for: {study_time} hours")

# 8️⃣ Mobile Usage Question
if st.checkbox("Did you limit mobile/social media usage today?"):
    choice = st.radio("Pick one:", ["Yes", "No"])

    if choice == "Yes":
        st.success("Great job keeping screen time low!")
    else:
        st.error("Try to reduce phone use tomorrow.")

# 9️⃣ Happiness Question
if st.checkbox("Did you do something today that made you happy or relaxed?"):
    choice = st.radio("Pick one:", ["Yes", "No"])

    if choice == "Yes":
        activity = st.text_input("What made you happy today?")
        if activity:
            st.success(f"That's wonderful! Today you enjoyed: {activity}")
    else:
        st.warning("Try to do at least one thing that makes you happy tomorrow!")

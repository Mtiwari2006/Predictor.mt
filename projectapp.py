import streamlit as st
import google.generativeai as ai

st.title("😊📖Mtiwari ji Chatbot😊📖")

if st.checkbox("Do you want to Ask any question from AI"):

    my_key = "AIzaSyDP7YqjNzwWr5rm7ZJUGnQo_jvv5y6GoVY"
    ai.configure(api_key=my_key)
    model = ai.GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat()

    msg = st.text_area("Ask your question:-")

    if st.button("Send to AI"):
        user_msg = msg.strip().lower()
        developer_keywords = [
    "who built", "who made", "who created", "developer", "creator", "maker", 
    "banaya kisne", "kisne banaya", "who programmed", "created by", "developed you",
    "developer name", "mtiwari ne tumhe banaya", "who coded you",
    "tumhe kisne banaya", "tumhara developer kaun hai", 
    "mtiwari ne hi banaya", "kya mtiwari ne banaya", "kisi aur ne banaya",
    "did mtiwari build you", "mtiwari created you", "are you built by mtiwari",
    "tumhe mtiwari ne banaya ya kisi aur ne"
]  
        purpose_keywords = [
            "kis liye", "kis kaam ke liye", "kaam kya", "what is your purpose", 
            "why were you made", "why did mtiwari create", "what do you do", 
            "tumhara kaam kya", "why mtiwari made you", "mtiwari ne kis work ke liye tumhe banaya"
        ]

        if any(k in user_msg for k in purpose_keywords):
            answer = "Mtiwari ji ne mujhe banaya hai taki main logo ki help kar Saku."
        elif any(k in user_msg for k in developer_keywords):
            answer = "Mujhe Mtiwari ji ne banaya hai 😊🙏"
        else:
            result = chat.send_message(msg)
            answer = result.text

        st.markdown("**Mtiwari AI Response:**")
        st.write(answer)

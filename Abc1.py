
import google.generativeai as ai
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
#to run program:- C:\Users\acer\AppData\Local\Programs\Python\Python313\Scripts\streamlit.exe run "c:/Users/acer/Desktop/python codes/AIml/Abc1.py"
# Load dataset
df = pd.read_excel(r"C:\Users\acer\Desktop\python codes\AIml\Sand..xlsx")

# Prepare features and target
X = df[['Sleep Hours', 'Caffeine Cups', 'ScreenTime', 'Stress Level']]
y = df['Productivity']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Streamlit App UI
st.title("😴 Sleep Tracker AI - Productivity Predictor")

st.markdown("Enter your daily details to predict how productive you'll feel tomorrow:")

sleep = st.slider("🛌 Sleep Hours", 0.0, 12.0, 7.0, 0.5)
caffeine = st.slider("☕ Caffeine (cups)", 0, 10, 2)
screen = st.slider("📱 Screen Time Before Bed (hrs)", 0.0, 6.0, 2.0, 0.5)
stress = st.slider("😫 Stress Level (1 = Calm, 10 = High)", 1, 10, 4)

if st.button("Predict Productivity"):
    input_df = pd.DataFrame([[sleep, caffeine, screen, stress]], 
                            columns=['Sleep Hours', 'Caffeine Cups', 'ScreenTime', 'Stress Level'])
    prediction = model.predict(input_df)[0]
    st.success(f"🧠 Predicted Productivity Score: **{prediction:.2f}/100**")

    if prediction < 50:
        st.warning("⚠️ Low productivity. Try getting more rest or reducing stress.")
    elif prediction > 80:
        st.balloons()
        st.info("🎉 Excellent! You're on track for a super productive day!")

st.markdown("---")
st.caption("Always be happy and healthy.\n Mithilesh ❤️ Tiwari")


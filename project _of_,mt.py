import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import streamlit as st
import sklearn.linear_model as LogisticRegression
import warnings

url = "heart.csv"
df = pd.read_csv(url)
X=df.drop('target',axis=1)
Y=df['target']
Z=df['age']
warnings.filterwarnings("ignore", category=UserWarning)
model=LogisticRegression.LogisticRegression()
model.fit(X,Y)
print( "\n(1)- Age\n",
       "(2)- Sex\n",
       "(3)- Chest Pain Type\n",
       "(4)- Resting Blood Pressure\n",
       "(5)- Serum Cholesterol\n",
       "(6)- Fasting Blood Sugar\n",
       "(7)- Resting Electrocardiographic Results\n",
       "(8)- Maximum Heart Rate Achieved\n",
       "(9)- Exercise Induced Angina\n",
       "(10)-ST Depression (Oldpeak)\n",
       "(11)-Slope of the ST Segment\n",
       "(12)-Number of Major Vessels Colored by Fluoroscopy\n",
       "(13)-Thalassemia\n",
       "(14)-Heart Disease Presence\n")
print("\t\nNOTICE:--Please see the capital and small word to give yes no answer\n")
def ai():
    import google.generativeai as ai
    my_key="AIzaSyDP7YqjNzwWr5rm7ZJUGnQo_jvv5y6GoVY"
    ai.configure(api_key=my_key)
    modal=ai.GenerativeModel("gemini-2.0-flash")
    chat=modal.start_chat()
    print('Write bye to exit the AI')
    while True:
        msg=input("Ask your question:-")
        if (msg=="bye"):
            print("Chatbot:Good Bye")
            print('❤️Thanks You Can Call Me latter For Help🙏👍')
            break
        result=chat.send_message(msg)
        print("Chatbot:",result.text)
def pre():
    a=int(input("\nEnter the age(29-77) of the Patient in years:-"))
    s=int(input("\nEnter the sex of the Patient(1 = Male, 0 = Female):-"))
    cp=int(input("\nEnter the Patient Chest Pain Type('0 = Typical angina ,1 = Atypical angina,2 = Non-anginal pain, 3 = Asymptomatic):-"))
    tre=float(input("\nEnter the Resting Blood Pressure (94-200)(in mm Hg) at admission of Patient:-"))
    chol=int(input("\nEnter Serum Cholesterol (in mg/dl(e.g., 126 - 564)) of Patient:-"))
    fbs=int(input("\nEnter the Fasting Blood Sugar(1 = Yes (blood sugar > 120),0 = No (blood sugar ≤ 120)of Patient:-"))
    res=int(input("\nEnter the Resting Electrocardiographic Results(0 =Normal,1 =ST-T wave abnormality,2 =Left ventricular hypertrophy) of Patient:-"))
    tha=int(input("\nEnter the Max heart rate achieved during test of Patient(e.g., 150, 187):-"))
    ex=int(input("\nEnter Chest pain during exercise(1 = Yes, 0 = No)of patient:-"))
    old=float(input("\nEnter ST depression induced by exercise relative to rest of patient(0.0 - 6.2):-"))
    slope=int(input("\nEnter the Slope of peak exercise ST segment(0 = Upsloping,1 = Flat,2 = Downsloping)of patient:-"))
    ca=int(input("\nEnter the Number of major vessels colored by fluoroscopy (Integer:0 to 3 (can go up to 4 in some versions)) of Patient:-"))
    thal=int(input("\nEnter the Blood disorder — thalassemia test result(1 = Normal,2 = Fixed defect,3 = Reversible defect) of Patient:-"))
    All=[a,s,cp,tre,chol,fbs,res,tha,ex,old,slope,ca,thal,]
    warnings.filterwarnings("ignore", category=UserWarning)
    Pre=model.predict([All])
    print("\nPredicted Result for your given data is :-",'😢😢 Heart Disease Possible😢😢'if Pre[0] else ' ❤️ 😊😊 No Heart Disease.Your Heart is in Good Condition😊😊❤️')
    if Pre[0]:
        print("\nDo you want to know how to reduce the possibility of your disease.You can ask from AI.")
        nm=input("\nDo you want to ask write yes or no here:-")
        if nm=='yes':
            ai()
           
   
print("\n🙏 Have you above mentioned information is available or not if not available then don't waste your time here because without information you can not predict you Disease 🙏")

nme=input("\nIf available write Yes(If want any information about any word write AI to help) else Write No :-")
if nme=='Yes':
    pre()
    while True:
        argu=input("\nDo you have any another data of other patient of which you want to know about possibility of heart disease(Write yes or no):-")
        if argu=="yes":
            pre()
        else:
            print("\n 😊 Thanks to use me  😊")
            break
elif nme=='AI':
    ai()
    m=input("Are you want to predict your disease ?:- ")
    if m=="yes":
        pre()
j=input("Do you want to see the Heart Disease Posibility Graph:Yes OR No:-")
if j=='Yes':
    plt.figure(figsize=(10,10))
    plt.title("Heart ❤️ Disease Posibility Graph")
    plt.plot(Z,Y,color='green',label='Real Data')
    plt.xlabel("Age")
    plt.ylabel("Posibility of Heart Disease")
    plt.grid(True)
    plt.legend()
    plt.show()
m=input('Have You Any Doubt You Can Ask From AI Only Write AI Here:-')
if m=='AI':
    ai()
else:
    print('❤️ Thanks You Can Call Me latter For Help 🙏 👍')

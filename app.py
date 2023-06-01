import streamlit as st
import pickle
import pandas as pd


st.sidebar.image("iplimages.png")
st.sidebar.image("image9.png")
st.sidebar.image("image4.jpg")
st.sidebar.image("image5.png")
st.sidebar.image("image112.jpg")
st.sidebar.image("image10.jpg")
st.sidebar.image("image13.jpg")
st.sidebar.image("image15.jpg")


st.sidebar.header("IPL Prediction")
st.sidebar.write("The IPL, a professional Twenty20 cricket league in India, attracts viewers due to its star power, entertainment value, fast-paced format, regional pride, international fanbase, competitive balance, festive atmosphere, and digital engagement. The presence of renowned players, engaging elements like cheerleaders and music, high-scoring matches, regional rivalries, global following, competitive nature, festive timing, and widespread coverage on television and digital platforms make the IPL a highly appealing tournament for viewers.")
st.sidebar.image("image4.jpg")
st.sidebar.image("image11.jpg")
st.sidebar.image("image21.jpg")
st.sidebar.image("image17.jpg")



teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals',

        ]

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title("Khelo Dimag Se App")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city', sorted(cities))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/(balls_left)

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city': [selected_city],'runs_left': [runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    # st.table(input_df)
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    st.header(batting_team + " - " + str(round(win*100)) + "%")
    st.header(bowling_team + " - " + str(round(loss*100)) + "%")
    # st.text(result)




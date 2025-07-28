import streamlit as st
import pandas as pd
import pickle

# Load trained model pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('🏏 IPL Match Winner Predictor (Pre-match)')

# Team selection
teams = sorted([
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
])

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

venues = [
    'Rajiv Gandhi International Stadium, Uppal',
    'M Chinnaswamy Stadium',
    'MA Chidambaram Stadium, Chepauk',
    'Wankhede Stadium',
    'Eden Gardens',
    'Feroz Shah Kotla',
    'Sawai Mansingh Stadium',
    'Punjab Cricket Association Stadium, Mohali'
]

# Input form
col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox('Team 1', teams)
with col2:
    team2 = st.selectbox('Team 2', [t for t in teams if t != team1])

city = st.selectbox('Match City', sorted(cities))
venue = st.selectbox('Venue', sorted(venues))
toss_winner = st.selectbox('Toss Winner', [team1, team2])
toss_decision = st.selectbox('Toss Decision', ['bat', 'field'])

if st.button("Predict Winner"):
    input_df = pd.DataFrame({
        'team1': [team1],
        'team2': [team2],
        'venue': [venue],
        'city': [city],
        'toss_winner': [toss_winner],
        'toss_decision': [toss_decision]
    })

    prediction = pipe.predict(input_df)
    st.success(f"🏆 Predicted Winner: **{prediction[0]}**")

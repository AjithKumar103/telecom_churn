import streamlit as st
import joblib as jb
import numpy as np

st.title('Telecom Churn Rate Predictor')
st.image(
    """https://img.freepik.com/free-vector/mobile-telecommunicatidigital-tower-background_1017-23175.jpg?size=626&ext=jpg&ga=GA1.1.896618002.1681572493&semt=sph""")
st.header('Enter the details of the Telecom Subscriber:')

sex = st.selectbox('Gender:', ['Male', 'Female'])

partner = st.selectbox('Marital status:', ['Yes', 'No'])

dependent = st.selectbox('Are you have dependencies:', ['Yes', 'No'])

senior_citizen = st.selectbox('Are you Senior Citizen', ['Yes', 'No'])

tenure = st.number_input('Tenure of the subscriber:', min_value=1, max_value=72, value=6)

phone_service = st.selectbox('Are you have Phone Service', ['Yes', 'No'])

multiple_lines = st.selectbox('Are you have multiple lines for phone', ['No phone service', 'No', 'Yes'])

internet_service = st.selectbox('What type of internet service', ['DSL', 'Fiber optic', 'No'])

online_security = st.selectbox('Are you have online security', ['No', 'Yes', 'No internet service'])

online_backup = st.selectbox('Are you have online backup', ['No', 'Yes', 'No internet service'])

device_protection = st.selectbox('Are you have device protection', ['No', 'Yes', 'No internet service'])

tech_support = st.selectbox('Are you have tech support', ['No', 'Yes', 'No internet service'])

stream_tv = st.selectbox('Are you have streaming TV', ['No', 'Yes', 'No internet service'])

stream_movies = st.selectbox('Are you have streaming movies', ['No', 'Yes', 'No internet service'])

contract = st.selectbox('Contract type of the subscription', ['Month-to-month', 'One year', 'Two year'])

paperless_billing = st.selectbox('Do you have paperless billing', ['Yes', 'No'])

payment_method = st.selectbox('Payment method', ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'])

monthly_charges = st.number_input('Monthly charges', min_value=18.0, max_value=118.0, value=70.0)

total_charges = st.number_input('Total charges:', min_value=18.0, max_value=9000.0, value=350.0)

he_she = sex

if sex == 'Male':
    sex = 1
else:
    sex = 0

yes_no = {"partner": partner, "dependent": dependent, "senior_citizen": senior_citizen, "phone_service": phone_service,
          "paperless_billing": paperless_billing}
for i in yes_no.keys():
    if yes_no[i] == 'Yes':
        yes_no[i] = 1.0
    else:
        yes_no[i] = 0.0

if multiple_lines == 'No phone service':
    multiple_lines = 1.0
elif multiple_lines == 'Yes':
    multiple_lines = 2.0
else:
    multiple_lines = 0.0

if internet_service == 'No':
    internet_service = 2.0
elif internet_service == 'DSL':
    internet_service = 0.0
else:
    internet_service = 1.0

if payment_method == 'Electronic check':
    payment_method = 2.0
elif payment_method == 'Mailed check':
    payment_method = 3.0
elif payment_method == 'Bank transfer':
    payment_method = 0.0
else:
    payment_method = 1.0

if contract == 'Month-to-month':
    contract = 0.0
elif contract == 'One year':
    contract = 1.0
else:
    contract = 2.0

yes_no_noservice = {"online_security": online_security, "online_backup": online_backup,
                    "device_protection": device_protection, "tech_support": tech_support, "stream_tv": stream_tv,
                    "stream_movies": stream_movies}

for j in yes_no_noservice.keys():
    if yes_no_noservice[j] == 'No':
        yes_no_noservice[j] = 0.0
    elif yes_no_noservice[j] == 'Yes':
        yes_no_noservice[j] = 2.0
    else:
        yes_no_noservice[j] = 1.0


features = [sex, yes_no["partner"], yes_no["dependent"], yes_no["phone_service"],
            multiple_lines, internet_service, yes_no_noservice["online_security"], yes_no_noservice["online_backup"],
            yes_no_noservice["device_protection"], yes_no_noservice["tech_support"], yes_no_noservice["stream_tv"],
            yes_no_noservice["stream_movies"], contract, yes_no["paperless_billing"], payment_method,
            yes_no["senior_citizen"], tenure, monthly_charges, total_charges]

final_features = np.array([features])

loaded_model = jb.load("Boost_Final_Model.pkl")

if he_she == 'Male':
    a = 'He'
else:
    a = 'She'

if st.button('Predict'):
    prediction = loaded_model.predict(final_features)
    st.balloons()
    st.success(f'Would {a} Churn: {prediction[0]}')

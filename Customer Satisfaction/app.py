from flask import Flask, render_template, request
import pandas as pd
import pickle

app=Flask(__name__)
data=pd.read_excel('C:\VSCODE\ML TRAINING PROJECT\Invistico_Airline.xlsx')
pklfile=pickle.load(open('C:\VSCODE\ML TRAINING PROJECT\mainy.pkl','rb'))
@app.route('/')

def index():
    return render_template('index.html')
# Age	Type of Travel	Class	Flight Distance	Seat comfort	Departure/Arrival time convenient	Food and drink	Gate location	Inflight wifi service	Inflight entertainment	Online support	Ease of Online booking	On-board service	Leg room service	Baggage handling	Checkin service	Cleanliness	Online boarding	Departure Delay in Minutes	Arrival Delay in Minutes

@app.route('/predict',methods=['POST'])
def predict():
    Gender=request.form.get('gender')
    Customer_Type=request.form.get('customer-type')
    Age=request.form.get('age')
    Type_of_travel=request.form.get('type-of-travel')
    Class=request.form.get('class')
    Flight_Distance=request.form.get('flight-distance')
    Seat_comfort=request.form.get('seat-comfort')
    Departure_Arrival_Time_Convenient=request.form.get('datc')
    Food_Drink=request.form.get('food-drink')
    Gate_Location=request.form.get('gate-location')
    Inflight_Wifi_services=request.form.get('Iwifi')
    Inflight_entertainment=request.form.get('inflight-ent')
    Online_support=request.form.get('online-support')
    Ease_of_online_booking=request.form.get('eoob')
    On_board_services=request.form.get('onboard-services')
    Leg_room_services=request.form.get('lrs')
    Baggage_handling=request.form.get('bh')
    Checkin_services=request.form.get('cis')
    Cleanliness=request.form.get('clean')
    Online_boarding=request.form.get('online-boarding')
    Departure_delaying=request.form.get('DD-in-min')
    Arrival_delaying=request.form.get('AA-in-min')

    if(Gender=='Male'):
        Gender=0
    else :
        Gender=1

    if(Customer_Type=='Loyal Customer'):
        Customer_Type=0
    else :
        Customer_Type=1

    if(Type_of_travel=='Personal Travel'):
        Type_of_travel=0
    else :
        Type_of_travel=1

    if(Class=='Eco'):
        Class=1
    elif(Class=='Business'):
        Class=0
    else :
        Class=2

    input=pd.DataFrame([[Gender,Customer_Type,Age,Type_of_travel,Class,Flight_Distance,Seat_comfort,Departure_Arrival_Time_Convenient,Food_Drink,Gate_Location,Inflight_Wifi_services,Inflight_entertainment,Online_support,Ease_of_online_booking,On_board_services,Leg_room_services,Baggage_handling,Checkin_services,Cleanliness,Online_boarding,Departure_delaying,Arrival_delaying]],columns=['Gender','Customer Type','Age','Type of Travel','Class','Flight Distance','Seat comfort','Departure/Arrival time convenient','Food and Drink','Gate Location','Inflight wifi service','Inflight entertainment','Online support','Ease of Online booking','On-board service','Leg room service','Baggage handling','Checkin service','Cleanliness','Online boarding','Departure Delay in minutes','Arrival Delay in minutes'])
    prediction=pklfile.predict(input)
    print(prediction)
    if(prediction==1):
        return "SATISFIED"
    else :
        return "DISSATISFIED"

if __name__=="__main__":
    app.run(debug=True, port=5001)
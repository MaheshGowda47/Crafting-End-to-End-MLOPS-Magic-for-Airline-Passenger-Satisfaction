"""
This is a boilerplate pipeline 'processed_data'
generated using Kedro 0.19.1
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def preprocessed_data(data) -> pd.DataFrame:
    # Columns to drop 
    col_to_drop = ["ID", "Gate Location"] 
    data = data.drop(columns=col_to_drop, axis=1)

    # Interaction Features_1 [all through online service]
    data["flight_service_1"] = ((data["Ease of Online Booking"] + data["Check-in Service"] + data["Online Boarding"]) / 3).round().astype(int)
    col_drop1 = ["Ease of Online Booking", "Check-in Service", "Online Boarding"]
    data = data.drop(columns=col_drop1, axis=1)

    # Interaction Features_2 [service in airline infrastructure]
    data["flight_service_2"] = ((data["On-board Service"] + data["Seat Comfort"] + data["Food and Drink"] + data["Cleanliness"] + data["Leg Room Service"]) / 5).round().astype(int)
    col_drop2 = ["On-board Service", "Seat Comfort", "Food and Drink", "Cleanliness", "Leg Room Service"]
    data = data.drop(columns=col_drop2, axis=1)

    # Interaction Features_3 [manual service of airlines]
    data["flight_service_3"] = ((data["In-flight Service"] + data["In-flight Wifi Service"] + data["In-flight Entertainment"] + data["Baggage Handling"]) / 4).round().astype(int)
    col_drop3 = ["In-flight Service", "In-flight Wifi Service", "In-flight Entertainment", "Baggage Handling"]
    data = data.drop(columns=col_drop3, axis=1)

    # Calculate percentiles for Flight Distance
    q1, q2, q3 = np.percentile(data["Flight Distance"], [25, 50, 75])

    # Replace values based on Flight Distance percentiles
    data.loc[data['Flight Distance'] <= q1, 'Flight Distance'] = 0
    data.loc[(data['Flight Distance'] > q1) & (data['Flight Distance'] <= q2), 'Flight Distance'] = 1
    data.loc[(data['Flight Distance'] > q2) & (data['Flight Distance'] <= q3), 'Flight Distance'] = 2
    data.loc[data['Flight Distance'] > q3, 'Flight Distance'] = 3  
    data['Flight Distance'] = data['Flight Distance'].astype(int)

    # Handling 'Arrival Delay' missing values represented as string 'nan'
    data["Arrival Delay"] = data["Arrival Delay"].astype(str)
    data["Arrival Delay"] = data["Arrival Delay"].apply(lambda x: 0 if x=="nan" else x)
    data["Arrival Delay"] = data["Arrival Delay"].astype(float)

    # Arrival and Departure Binning for Arrival Delay
    q1, q2, q3 = np.percentile(data["Arrival Delay"], [25, 50, 75])
    data.loc[data["Arrival Delay"] <= q1, "Arrival Delay"] = 0
    data.loc[(data['Arrival Delay'] > q1) & (data['Arrival Delay'] <= q2), 'Arrival Delay'] = 1
    data.loc[(data['Arrival Delay'] > q2) & (data['Arrival Delay'] <= q3), 'Arrival Delay'] = 2
    data.loc[data['Arrival Delay'] > q3, 'Arrival Delay'] = 3  
    data['Arrival Delay'] = data['Arrival Delay'].astype(int)

    # Departure Binning for Departure Delay
    q1, q2, q3 = np.percentile(data["Departure Delay"], [25, 50, 75])
    data.loc[data["Departure Delay"] <= q1, "Departure Delay"] = 0
    data.loc[(data['Departure Delay'] > q1) & (data['Departure Delay'] <= q2), 'Departure Delay'] = 1
    data.loc[(data['Departure Delay'] > q2) & (data['Departure Delay'] <= q3), 'Departure Delay'] = 2
    data.loc[data['Departure Delay'] > q3, 'Departure Delay'] = 3  
    data['Departure Delay'] = data['Departure Delay'].astype(int)

    # Label encoding to object columns
    encoder = LabelEncoder()
    col_to_encode = ["Gender", "Customer Type", "Type of Travel", "Class", "Satisfaction"]
    data[col_to_encode] = data[col_to_encode].apply(encoder.fit_transform)
    
    # Reordering columns, moving 'Satisfaction' to the end
    satisfaction_column = data.pop('Satisfaction')
    data['Satisfaction'] = satisfaction_column


    #nameing
    pre_data = data
    pre_data.to_csv(r"data/02_processed/processed_data.csv")
    # print(pre_data.head(5))
    # print(pre_data.shape)

    return pre_data





import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_synthetic_data():
    np.random.seed(42)
    districts = ['Dhaka', 'Chittagong', 'Rajshahi', 'Khulna', 'Barisal']
    upazilas = [f'Upazila_{i}' for i in range(1, 11)]
    diseases = ['Malaria', 'Dengue', 'Diarrhoea']

    records = []
    start_date = datetime(2015, 1, 1)
    dates = [start_date + timedelta(weeks=i) for i in range(520)]  # 10 years weekly

    for date in dates:
        for district in districts:
            for upazila in upazilas:
                lat = round(23 + random.uniform(-1, 1), 4)
                lon = round(90 + random.uniform(-1, 1), 4)
                temp = round(25 + 5 * np.sin((date.timetuple().tm_yday / 365.0) * 2 * np.pi) + np.random.normal(), 2)
                rain = round(abs(np.random.normal(100, 50)), 2)
                humidity = round(random.uniform(60, 90), 2)
                ndvi = round(random.uniform(0.2, 0.9), 2)
                soil_moisture = round(random.uniform(0.1, 0.5), 2)

                malaria_api = np.random.poisson(5)
                malaria_tpr = np.random.uniform(0, 0.2)
                dengue = np.random.poisson(3)
                diarrhoea = np.random.poisson(7)
                admissions = np.random.poisson(4)

                records.append([
                    date, district, upazila, lat, lon, temp, rain, humidity,
                    ndvi, soil_moisture, malaria_api, malaria_tpr, dengue,
                    diarrhoea, admissions
                ])

    columns = ['date', 'district', 'upazila', 'lat', 'lon', 'temperature', 'rainfall',
               'humidity', 'ndvi', 'soil_moisture', 'malaria_api', 'malaria_tpr',
               'dengue_incidence', 'diarrhoea_incidence', 'hospital_admissions']
    df = pd.DataFrame(records, columns=columns)
    df.to_csv('data/synthetic_data.csv', index=False)
    return df
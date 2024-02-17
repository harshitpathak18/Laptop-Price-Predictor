import pandas as pd
import pickle


df = pd.read_csv(r"C:\Users\DELL\Desktop\Machine_learning\Laptop_Price_Prediction\Predict_laptop_price\Assets\cleaned_laptop_price.csv")
pipe = pickle.load(open(r"C:\Users\DELL\Desktop\Machine_learning\Laptop_Price_Prediction\Predict_laptop_price\Assets\laptop_price_pipeline.pkl", 'rb'))

company = df['Company'].unique()
type_name = df['TypeName'].unique()
ram = [2,4,6,8,12,16,24,32,64]
gpu = df['GPU Brand'].unique()
cpu = df['CPU Brand'].unique()
ssd = [0,8,128,256,512,1024]
hdd = [0,128,256,512,1024,2048]

def Data():
    return sorted(company), type_name, sorted(ram), sorted(gpu), sorted(cpu), sorted(ssd), sorted(hdd), df['Weight'].min(), df['Weight'].max()


def predict_price(company, type, ram, weight, touchscreen, ips, screen_size, resolution, cpu, hdd, ssd, gpu):
    # Convert touchscreen and IPS to binary
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Calculate PPI
    X_res = int(str(resolution).split('x')[0])
    Y_res = int(str(resolution).split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size

    # Create DataFrame
    data = pd.DataFrame([[company, type, ram, weight, gpu, ppi, touchscreen, ips, cpu, ssd, hdd]],
                        columns=['Company', 'TypeName', 'Ram', 'Weight', 'GPU Brand', 'ppi', 'TouchScreen', 'IPS', 'CPU Brand', 'SSD','HDD'])

    # Predict price
    predicted_price = pipe.predict(data)[0]
    return int(predicted_price)
from src.data_handling.input_data import read_file


DATAPATH = 'data/raw/diabetes.csv'
COLUMNS = [
    'Age',
    # 'BMI',
    'BloodPressure',
    # 'DiabetesPedigreeFunction',
    'Glucose',
    # 'Insulin',
    'Outcome',
    # 'Pregnancies',
    # 'SkinThickness'
]
TARGET = ""

if __name__ == "__main__":

    import yaml

    df = read_file(DATAPATH, columns=COLUMNS)

    print(df.head())
    print(df.iloc[0])
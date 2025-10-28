import pandas as pd

def run_etl(input_file, output_file):
    df = pd.read_csv(input_file)
    df['total'] = df['quantity'] * df['price']
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    run_etl("input_data.csv","output_data.csv")

import pandas as pd
from etl_pipeline import run_etl

def test_run_etl():
    
    input_data = pd.DataFrame({
        'product' : ['Test'],
        'quantity' : [2],
        'price' : [3.0]
    })
    input_data.to_csv("test_input.csv", index=False)
    run_etl("test_input.csv","test_output.csv")
    result = pd.read_csv("test_output.csv")
    assert result['total'][0] == 6.0

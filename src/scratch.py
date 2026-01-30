import polars as pl
import csv

def read_csv_file(file_path: str) -> list[dict]:
    i = 0
    with open(file_path, mode='r', newline='', encoding='utf-8') as reader:
        for row in reader:
            i += 1
            print(i)
            data = next(reader)
            print(data)
    return data

def main():
    file_path = '/Users/mike/Documents/Mike/Finance/Banking/Barclays/Data/tax years/2023-24/2023-24 tax year 90186236.csv'  # Replace with your CSV file path
    # file_path = '/Users/mike/Documents/Mike/Finance/Banking/Barclays/Data/tax years/2023-24/data.csv'  # Replace with your CSV file path
    data = read_csv_file(file_path)
    df = pl.read_csv(file_path)
    print(df)

if __name__ == "__main__":
    main()
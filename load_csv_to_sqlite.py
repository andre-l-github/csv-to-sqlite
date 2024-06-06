import os
import sqlite3
import pandas as pd

def load_csv_to_sqlite(input_directory, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    for subfolder in os.listdir(input_directory):
        subfolder_path = os.path.join(input_directory, subfolder)
        if os.path.isdir(subfolder_path):
            output_db_path = os.path.join(output_directory, f"{subfolder}.sqlite")

            # Connect to the SQLite database
            conn = sqlite3.connect(output_db_path)
            cursor = conn.cursor()

            # Iterate over all CSV files in the subdirectory
            for filename in os.listdir(subfolder_path):
                if filename.endswith(".csv"):
                    file_path = os.path.join(subfolder_path, filename)
                    table_name = os.path.splitext(filename)[0]

                    try:
                        # Read the CSV file into a DataFrame
                        df = pd.read_csv(file_path, sep=';')

                        # Write the DataFrame to the SQLite database
                        df.to_sql(table_name, conn, if_exists='replace', index=False)

                        print(f"Loaded {filename} into table {table_name} in {output_db_path}")
                    except Exception as e:
                        print(f"Failed to load {filename}: {e}")

            # Close the database connection
            conn.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python load_csv_to_sqlite.py <input_directory> <output_directory>")
        sys.exit(1)
    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    load_csv_to_sqlite(input_directory, output_directory)

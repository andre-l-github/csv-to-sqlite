# CSV to SQLite

This project provides a solution for loading CSV files from a directory into an SQLite database using Docker. Each subdirectory within the specified input directory is treated as a separate SQLite database, with the CSV files within each subdirectory being loaded as tables.

## Prerequisites

Install docker on your system.

## Directory Structure

Ensure your project directory has the following structure:

```
project_directory/
│
├── csv/ # This directory contains subdirectories with your CSV files
│ ├── subfolder1/
│ │ ├── file1.csv
│ │ ├── file2.csv
│ │ └── ...
│ └── subfolder2/
│ ├── file1.csv
│ ├── file2.csv
│ └── ...
│
├── exports/ # This directory will contain the SQLite databases
│ ├── subfolder1.sqlite
│ ├── subfolder2.sqlite
├── load_csv_to_sqlite.py
├── Dockerfile
└── convert.sh
```

## Prepare Your CSV Files

Place your CSV files into subdirectories within the ./csv directory. Each subdirectory will correspond to a separate SQLite database.

## Instructions

Make the shell script executable (if not already done):

```
chmod +x convert.sh
```

Run the shell script to build the Docker image and process the CSV files:

```
./convert.sh
```

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).

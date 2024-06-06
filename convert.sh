#!/bin/bash

# Define input and output directories
INPUT_DIR=$(realpath ./csv)
OUTPUT_DIR=$(realpath ./exports)

# Create the output directory if it does not exist
mkdir -p "$OUTPUT_DIR"

# Build the Docker image
docker build -t csv_to_sqlite .

# Run the Docker container
docker run --rm -v "$INPUT_DIR":/input -v "$OUTPUT_DIR":/output csv_to_sqlite /input /output

echo "Databases written to $OUTPUT_DIR"

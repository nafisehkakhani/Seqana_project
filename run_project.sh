#!/bin/bash

# Check if the file path argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: ./run_project.sh <path_to_excel_file>"
    exit 1
fi

# Activate the conda environment
echo "Activating conda environment..."
source ~/miniconda3/etc/profile.d/conda.sh  # Adjust this if conda is installed in a different location
conda activate seqana_test_env

# Run the main Python script with the provided file path
echo "Running main.py..."
python main.py "$1"

echo "Process completed!"

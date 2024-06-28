# How to Properly Load the Data

## Step 0: Download train.bin from Prompt

Run the decrypt.py script, which will give us the two .csv we work with in this project.

## Step 1: Obtain ads.csv & feeds.csv

Create a directory called 'decrypted_file' and a directory within it called 'train'.

Save the two csv files in that directory

## Step 2: Run the MergeDataframe.ipynb Notebook

Before running the last cell (to_csv) ensure that you create a directory called 'merged_file'

These steps will ensure that their won't be any issues with pathing if any of the other Jupyter Notebooks are ran (the Synthetic Data Generation/Predictive Modelling one)
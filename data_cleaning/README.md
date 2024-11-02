# Movie Genre Cleaning Script

This project provides a Python script that cleans a dataset of movies by extracting genre information from a CSV file. The cleaned data is then saved into a new CSV file.

## Prerequisites

- Python 3.x
- pandas library
- json library (comes with Python standard library)

## Input

- The script expects an input file named `movies.csv`. This file should contain a column named `genres`, which contains JSON formatted strings representing the genres of each movie.

## Output

- The script generates a new file named `movies_cleaned.csv`, which contains two columns:
  - `Id`: The unique identifier for each genre.
  - `Name`: The name of each genre.


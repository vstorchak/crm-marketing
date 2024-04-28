# resampling-tool is an interaction analysis tool
This Python script provides a user-friendly method to leverage existing user interactions, such as emails opens / clicks or video views (any kind of interaction actually).
It generates extended pseudo-samples of interactions, which can be used for in-depth statistical analysis.

## Features

- Parse interaction data from a specified file.
- Split the data into a specified number of blocks and chunks for analysis.
- Resample the chunks to create extended pseudo-samples.
- Calculate interaction metrics like open rate and conduct statistical analysis on the results.

## How to Use

1. Run the script and provide the name of the file containing the interaction data when prompted.
2. Input the number of blocks the IDs belong to, the number of chunks to split each block into, and the number of resamples for each chunk.
3. View the calculated average open rate for each block along with the confidence interval.

## Usage

python interaction_analysis.py


When prompted, enter the name of the file containing the interaction data, the number of blocks, the number of chunks, and the number of resamples.

## Example

Suppose you have interaction data in a file named "interactions.csv", and you want to split the IDs into 5 blocks, each with 4 chunks, and perform 100 resamples for each chunk. You would run the script, input "interactions.csv" when prompted, and then enter 5, 4, and 100 for the respective parameters.

## Dependencies

- Python 3.x
- NumPy

## Future development vision

One of currently missing use case that has some demand behind is the intersection of existing data about interactions to generate various comparison results as outputs. That's where the next focus area for this developer's products will be.

## Note

This script assumes that the interaction data is structured with specific columns for user IDs, interactions, etc. Make sure your input file conforms to the expected format for the script to work correctly.

Feel free to use this tool to gain insights from your interactions data and conduct statistical analysis effectively. If you have any questions or feedback, please don't hesitate to reach out. Happy analyzing!

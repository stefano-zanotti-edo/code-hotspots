# Description: Extract complexity from SonarQube and save it to a CSV file
# This script calls the SonarQube API to get the complexity of the components of a given project.
# The complexity is saved in a CSV file with the following columns:
# - language
# - filename
# - blank
# - comment
# - code
# The script receives the component as an argument.

import requests
import csv
import argparse

# Arg parsing
parser = argparse.ArgumentParser(description='Extract complexity from SonarQube and save it to a CSV file')
parser.add_argument('sonar_url', type=str, help='The SonarQube server URL')
parser.add_argument('component', type=str, help='The component to be analyzed')
parser.add_argument('output_file', type=str, help='CSV output file')
args = parser.parse_args()

url = f"{args.sonar_url}/api/measures/component_tree"
params = {
    "additionalFields": "metrics",
    "p": 1,
    "ps": 500,
    "asc": "false",
    "metricSort": "complexity",
    "s": "metric",
    "component": args.component,
    "metricKeys": "complexity",
    "strategy": "leaves"
}

# Open the output CSV file for writing
with open(args.output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["language", "filename", "blank", "comment", "code"])
    
    while True:
        # Make the API call
        response = requests.get(url, params=params)
        data = response.json()

        # Extract components from the response
        components = data.get("components", [])

        # If the components array is empty, break the loop
        if not components:
            break

        # Write component data to the CSV file
        for component in components:
            language = "Java"
            filename = "./" + component.get("path", "")
            blank = 0
            comment = 0

            # Check if the measures array is empty
            measures = component.get("measures", [])
            if measures and filename.endswith(".java"):
                code = measures[0].get("value", 0)
                writer.writerow([language, filename, blank, comment, code])

        # Increment the page number for the next API call
        params["p"] += 1

print(f"Data saved to {args.output_file}")
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# todo change from json to env file for numbers and path
# todo change from print to loguru

# Load  queries from  JSON file
with open("queries.json", "r") as f:
    queries = json.load(f)

# Specify  path to your Edge WebDriver
service = Service(
    executable_path=r"path"
)

# Initialize Edge WebDriver with options
options = Options()
options.add_argument("--headless")
driver = webdriver.Edge(service=service, options=options)

# Dictionary to store results
results = {}

try:
    # Open website
    driver.get("https://powerfailure.tshwane.gov.za/Tshwanesms/NewCall")

    # Open text file to write  responses
    with open("responses.txt", "w") as txt_file:
        for query in queries:
            # Fill out  form for each query
            driver.find_element(By.ID, "MainContent_TextNumber").clear()
            driver.find_element(By.ID, "MainContent_TextNumber").send_keys(
                query["account_number"]
            )
            driver.find_element(
                By.ID, "MainContent_TextCellNo"
            ).clear()  # Cell number remains blank
            driver.find_element(By.ID, "MainContent_TextComment").clear()
            driver.find_element(By.ID, "MainContent_TextComment").send_keys(
                "Power out in Lasseandra"
            )

            # Submit form
            driver.find_element(By.ID, "MainContent_cmdSend").click()

            # Wait for a response to be displayed
            time.sleep(3)

            # Extract response message
            response = driver.find_element(By.ID, "MainContent_LblMsg").text

            # Save response in results dictionary
            results[query["house_number"]] = {
                "account_number": query["account_number"],
                "response": response,
            }

            # Write the house number and response to a text file
            txt_file.write(
                f"House Number: {query['house_number']} - Response: {response}\n"
            )

            print(f"House Number: {query['house_number']} - Response: {response}")

finally:
    # Close WebDriver session
    driver.quit()

    # Save results to a JSON file
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Results have been saved to 'results.json' and 'responses.txt'.")

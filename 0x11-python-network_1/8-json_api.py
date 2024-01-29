#!/usr/bin/python3
"""json"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # If no argument is given, set q=""
        letter = ""
    elif len(sys.argv) == 2:
        # Extract the letter from the command line argument
        letter = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            print("No result")
    except ValueError:
        # Display an error if the JSON is invalid
        print("Not a valid JSON")

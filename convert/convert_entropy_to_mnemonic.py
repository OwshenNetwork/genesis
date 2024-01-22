import argparse
import json
from mnemonic import Mnemonic

def entropy_to_mnemonic(entropy):
    mnemonic = Mnemonic("english")
    mnemonic_phrase = mnemonic.to_mnemonic(bytes(entropy))
    return mnemonic_phrase

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Convert entropy to mnemonic phrase")

    # Add the --entropy-json argument
    parser.add_argument("--entropy-json", required=True, help="Path to the JSON file containing entropy")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Read JSON data from file
    try:
        with open(args.entropy_json, "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{args.entropy_json}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{args.entropy_json}'.")
        return

    # Extract entropy from the JSON
    entropy = json_data["entropy"]["value"]

    # Convert the array of integers to a bytes object
    entropy_bytes = bytes(entropy)

    # Convert entropy to mnemonic
    mnemonic_phrase = entropy_to_mnemonic(entropy_bytes)

    # Print the mnemonic phrase
    print("Mnemonic Phrase:", mnemonic_phrase)

if __name__ == "__main__":
    main()

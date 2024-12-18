import requests
import time
import argparse

# Function to read the token from the specified file
def get_token(token_file):
    with open(token_file, 'r') as f:
        return f.read().strip()

# Argument parser for optional command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--token', required=True, help='Path to the token file')
parser.add_argument('--guild', required=False, help='Guild ID if applicable')
args = parser.parse_args()

# Get the token and channel ID
TOKEN = get_token(args.token)
CHANNEL_ID = input("Enter Channel ID: ")
GUILD_ID = input("Enter Guild ID:")

# List of valid regions
regions = [
    'brazil', 'hongkong', 'india', 'japan', 'russia', 
    'singapore', 'southafrica', 'sydney', 'us-central', 
    'us-east', 'us-south', 'us-west'
]

# Setup headers for the API request
headers = {
    'Authorization': TOKEN,
    'Content-Type': 'application/json'
}

def change_region(new_region):
    # Determine the correct URL based on whether GUILD_ID is provided
    if GUILD_ID:
        url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}"
        data = {
            "rtc_region": new_region
        }
    else:
        url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/call"
        data = {
            "region": new_region
        }

    # Send the PATCH request to change the voice region
    response = requests.patch(url, headers=headers, json=data)

    # Handle the response
    if response.status_code == 200 or response.status_code == 204:
        print(f"Successfully changed region to {new_region}.")
    elif response.status_code == 429:
        print(f'Rate limited while changing region to {new_region}. Waiting 10 seconds...')
        time.sleep(10)
    else:
        print(f"Failed to change region. Status Code: {response.status_code} - {response.text}")

# Loop through regions and change the region
while True:
    for region in regions:
        change_region(region)
        time.sleep(3)  # Wait a little before changing to the next region

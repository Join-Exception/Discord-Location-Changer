# Discord Voice Region Changer

This Python program automates changing the voice region for a Discord channel or call. It's designed for testing and experimenting with Discord API functionality and requires a valid bot token and channel ID.

## Features

- **Cycles through a predefined list of voice regions**.
- **Supports both guild (server) and call regions**.
- **Automatically handles rate-limiting with retry logic**.

## Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Discord Bot Token**: Obtain a valid bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
3. **Channel ID**: Identify the channel ID where the voice region changes should be applied.
4. **Dependencies**: Install required Python packages using:
   ```bash
   pip install requests argparse
   ```

## Usage

### Command-Line Arguments

- `--token`: Path to a file containing the bot token (required).
- `--guild`: Guild (server) ID if applicable (optional).

### Running the Program

1. Save your bot token in a text file (e.g., `token.txt`).
2. Execute the program with the following command:
   ```bash
   python main.py --token token.txt
   ```
3. Enter the channel ID and guild ID (if applicable) when prompted.

## How It Works

1. The program reads the bot token from the specified file.
2. It prompts the user for a channel ID and an optional guild ID.
3. It cycles through a predefined list of valid voice regions:
   - `brazil`
   - `hongkong`
   - `india`
   - `japan`
   - `russia`
   - `singapore`
   - `southafrica`
   - `sydney`
   - `us-central`
   - `us-east`
   - `us-south`
   - `us-west`
4. Sends a PATCH request to the Discord API to update the voice region.
5. Logs the success or failure of each change.
6. Handles rate-limiting by waiting and retrying when necessary.

## Example Output

```
Enter Channel ID: 123456789012345678
Enter Guild ID: 987654321098765432
Successfully changed region to brazil.
Successfully changed region to hongkong.
Rate limited while changing region to india. Waiting 10 seconds...
Successfully changed region to india.
...
```

## Configuration

- **Token File**: Save your bot token in a plain text file. Ensure the file path is correct when using the `--token` argument.
- **Regions**: Modify the `regions` list in the script to include or exclude specific regions.

## Security

- **Token Safety**: Do not share your bot token. Treat it like a password.
- **Discord API Guidelines**: Ensure your usage complies with the [Discord Terms of Service](https://discord.com/terms).

## Disclaimer

This program is for educational and testing purposes only. Misuse of this tool can lead to account bans or other penalties from Discord. Use responsibly and ensure proper authorization before interacting with any Discord server or channel.


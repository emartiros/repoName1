from sys import argv
from slack import WebClient
from slack.errors import SlackApiError
from os import getenv

if __name__ == '__main__':
    os = argv[1]
    file_path = argv[2]
    client = WebClient(token=getenv('SLACK_TOKEN'))
    channel_id = getenv('SLACK_CHANNEL')
    message = "New " + os + " build"

    try:
        response = client.files_upload(
            channels=channel_id,
            initial_comment=message,
            file=file_path
        )
        print("Message sent successfully:", response["ts"])
    except SlackApiError as e:
        print("Error sending message:", e.response['error'])
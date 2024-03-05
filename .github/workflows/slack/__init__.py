from sys import argv
from slack import WebClient
from slack.errors import SlackApiError
from os import getenv

if __name__ == '__main__':
    try:
        os = argv[1]
        file_path = argv[2]
        client = WebClient(token=getenv('SLACK_TOKEN'))
        channel_id = '#' + getenv('SLACK_CHANNEL')
        message = "New " + os + " build"
        response = client.chat_postMessage(
            channel=channel_id,
            text=message
        )
        response = client.files_upload(
            channels=channel_id,
            initial_comment=message,
            file=file_path
        )
        print("Message sent successfully:", response["ts"])
    except Exception as e:
        print("Error sending message:", e.response['error'])
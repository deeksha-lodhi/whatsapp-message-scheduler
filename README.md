# WhatsApp Message Scheduler

This project enables users to schedule WhatsApp messages, including messages to groups, using the PyWhatKit library.

## Features

- Schedule text messages to individuals or groups at specific times.
- Simple and user-friendly interface.

## Usage

1. Install PyWhatKit:

    ```pip install pywhatkit```

2. Import PyWhatKit:

    import pywhatkit

3. Schedule a message:

- For a number:

    ```pywhatkit.sendwhatmsg('+1234567890', 'Hello!', 18, 30)```

    Replace +1234567890 with the recipient's phone number or group_id and adjust the message content and time accordingly.

- For a group

    ```pywhatkit.sendwhatmsg_to_group(group_id, message, hour, minute)```
    
    To Know the Group Id: Get into the Group Info "Click on Invite via link" Add the suffix part of the link.

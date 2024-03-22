# WhatsApp Message Scheduler

This project enables users to schedule WhatsApp messages, including messages to groups, using the PyWhatKit library and Streamlit for building the user interface.

## Features

- Schedule messages to individuals or groups at specific times.
- Support for text-based messages.
- Interactive user interface built with Streamlit.
- Simple and user-friendly experience.

## Usage

1. Install PyWhatKit and Streamlit:

    ```pip install pywhatkit streamlit```


2. Import PyWhatKit and Streamlit in your Python code:
    
    ```
    import pywhatkit as pk
    import streamlit as st
    ```

3. Use the Streamlit interface to schedule a message:
    
    ```
    pk.sendwhatmsg(number, message, hour, minute)
    pk.sendwhatmsg_to_group(group_id, message, hour, minute)
    ```
    - Make sure you add the country code before sending a message to a number.
    - To Know the Group ID: Get into the Group Info "Click on Invite via link" Add the suffix part of the link.
  
4. Running the app:
    - Open the terminal
    - Enter the command: ```streamlit run main.py```
    - A browser window will open displaying the web app
    - Make sure you have WhatsApp web logged in before sending the message.

## Example Usage

```
import pywhatkit as pk
import streamlit as st

# Get user inputs using Streamlit
group_id = st.text_input("Enter group ID (optional):")
message = st.text_input("Enter your message:")
hour = st.number_input("Enter hour (24-hour format):", min_value=0, max_value=23)
minute = st.number_input("Enter minute:", min_value=0, max_value=59)

# Send a message to a group
pk.sendwhatmsg_to_group(group_id, message, hour, minute)
```


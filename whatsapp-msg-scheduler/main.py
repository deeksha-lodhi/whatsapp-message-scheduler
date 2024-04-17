import streamlit as st
import pywhatkit as pk
import time

st.title("WhatsApp Message Scheduler")

# Get user inputs
message = st.text_input("Enter your message:")
number = st.text_input("Enter recipient's phone number (with country code):")
group_id = st.text_input("Enter group ID (optional):")
hour = int(st.number_input("Enter hour (24-hour format):", min_value=0, max_value=23))
minute = int(st.number_input("Enter minute:", min_value=0, max_value=59))

# Function to send message
def send_message():
    try:
        if group_id:
            st.write("Sending message to group...")
            pk.sendwhatmsg_to_group(group_id, message, hour, minute)
            st.success("Message sent to group successfully!")
        else:
            st.write("Sending message to number...")
            pk.sendwhatmsg(number, message, hour, minute)
            st.success("Message sent successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Button to send message
if st.button("Send Message"):
    st.write("Attempting to send message...")
    time.sleep(5)  # Delay to ensure proper browser focus
    send_message()

# Security Disclaimer (Optional)
st.info("Sending WhatsApp messages directly from a web app might have security risks. Consider alternative solutions for production use.")

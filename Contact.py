import streamlit as st

# Define the contacts page
def contacts():
    st.title("Contacts Page")
    st.write("Welcome to the Contacts Page! Here, you can find some contact information.")

    # Sample contact information
    contact_data = [
        {"Name": "John Doe", "Email": "johndoe@example.com", "Phone": "+1 (123) 456-7890"},
        {"Name": "Jane Smith", "Email": "janesmith@example.com", "Phone": "+1 (234) 567-8901"},
        {"Name": "Bob Johnson", "Email": "bobjohnson@example.com", "Phone": "+1 (345) 678-9012"},
    ]

    # Display contact information
    for contact in contact_data:
        st.subheader(contact["Name"])
        st.write(f"Email: {contact['Email']}")
        st.write(f"Phone: {contact['Phone']}")
        st.write("-" * 40)  # Add a separator line

# Call the contacts function to display the contact page
contacts()

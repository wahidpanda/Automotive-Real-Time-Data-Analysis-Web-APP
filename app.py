import streamlit as st
import time
from auth import authenticate

# Set page title and icon
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# Create a container to style the login form
st.markdown(
    """
    <style>
    .login-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f0f0f0;
    }
    .login-box {
        display: flex;
        justify-content: space-between;
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .bold-text {
        font-weight: bold;
        font-size: 20px;
    }
    .icon {
        font-size: 36px;
    }
    .button-container {
        display: flex;
        justify-content: space-between;
    }
    .button {
        margin-top: 10px;
    }
    .digital-clock {
        font-size: 36px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define the login page
def login():
    st.markdown("<h1>Welcome to Sales Dashboard</h1>", unsafe_allow_html=True)
    # st.markdown("<h2 class='bold-text'>Google Calendar:</h2>", unsafe_allow_html=True)
    # Embed Google Calendar on the right side of the page
    st.markdown(
        """
    <iframe src="https://calendar.google.com/calendar/embed?height=300&wkst=1&bgcolor=%23ffffff&ctz=America%2FNew_York&src=your_email%40domain.com&color=%23853104&showTz=0&showCalendars=0"
        width="300" height="300" frameborder="0" scrolling="no" style="float: right;"></iframe>
    """,
        unsafe_allow_html=True,
    )

    # Display a big, bold clock
    st.markdown("<h1 class='digital-clock' id='clock'></h1>", unsafe_allow_html=True)
    

    # Rectangular login box
    with st.container():
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>"
            f"{time.strftime('%H:%M:%S')}⏳</h1>",
            unsafe_allow_html=True)
        

        # Username and password inputs
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Log In"):
            if authenticate(username, password):
                st.success("Logged in successfully!")
                st.session_state.logged_in = True
                st.button("Go to Projects Page")
            else:
                st.error("Authentication failed. Please try again.")

        st.markdown("<div class='button-container'>", unsafe_allow_html=True)

        # Button for reset password
        if st.button("Reset Password", key="reset_password"):
            st.info("Reset Key sent to your E-MAIL")

        # Button for creating a new account
        if st.button("Create New Account", key="create_account"):
            st.info("Loading...")

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# Define the contacts page
def contacts():
    st.title("Contacts Page")
    # Add your contacts page code here

# Define the 📚Projects page
def projects_page():
    st.title("📚Projects")
    # Add your 📚Projects page code here

# Multi-page navigation
pages = {
    "🏠Homepage": login,
    "📚Projects": projects_page,
    "💬Contact": contacts,
}

# Sidebar for navigation
selected_page = st.sidebar.radio("Navigation", list(pages.keys()))

# Display the selected page, and restrict access to the Projects page
if selected_page == "📚Projects" and not st.session_state.get("logged_in"):
    st.warning("Please log in to access this page.")
else:
    if selected_page == "🏠Homepage":
        st.markdown(
            """
            <div class="digital-clock" id="clock"></div>
            <script>
            function updateClock() {
                const now = new Date();
                const hours = now.getHours().toString().padStart(2, '0');
                const minutes = now.getMinutes().toString().padStart(2, '0');
                const seconds = now.getSeconds().toString().padStart(2, '0');
                document.getElementById('clock').textContent = `${hours}:${minutes}:${seconds}`;
            }
            setInterval(updateClock, 1000);
            </script>
            """,
            unsafe_allow_html=True,
        )

    pages[selected_page]()

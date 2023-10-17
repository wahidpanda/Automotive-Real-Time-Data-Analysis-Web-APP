import streamlit as st
import time
from auth import authenticate
import random
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    st.markdown("<h1>📌Welcome to Sales Dashboard📌</h1>", unsafe_allow_html=True)
    # st.markdown("<h2 class='bold-text'>Google Calendar:</h2>", unsafe_allow_html=True)
    # Embed Google Calendar on the right side of the page
    st.markdown(
        """
    <iframe src="https://calendar.google.com/calendar/embed?height=300&wkst=1&bgcolor=%E6B894&ctz=Asia%2FDhaka&src=your_email%40domain.com&color=%23853104&showTz=0&showCalendars=0"
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
    st.title("Contacts Information 📞")
    # Add your contacts page code here
    st.title("Contacts Page")
    st.write("Welcome to the Contacts Page! Here, you can find some contact information.")

    # Sample contact information
    contact_data = [
        {"Name": "John Doe 👨", "Email": "johndoe@example.com", "Phone": "+1 (123) 456-7890"},
        {"Name": "Jane Smith 👧", "Email": "janesmith@example.com", "Phone": "+1 (234) 567-8901"},
        {"Name": "Bob Johnson 👦🏼", "Email": "bobjohnson@example.com", "Phone": "+1 (345) 678-9012"},
    ]

    # Display contact information
    for contact in contact_data:
        st.subheader(contact["Name"])
        st.write(f"Email: {contact['Email']}")
        st.write(f"Phone: {contact['Phone']}")
        st.write("-" * 40)  # Add a separator line

# # Call the contacts function to display the contact page
# contacts()

# Define the 📚Projects page
def projects_page():
    st.title("📚Projects")
    # Add your 📚Projects page code here
    
# st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

    st.title("Analyzer Dashboard 📊")
    st.markdown("_Prototype v1.0_")
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>"
                f"{time.strftime('%H:%M:%S')}</h1>",
                unsafe_allow_html=True)

    with st.sidebar:
        st.header("Configuration")
        uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is None:
        st.info(" Upload your DATA", icon="ℹ️")
        st.stop()

    #######################################
    # DATA LOADING
    #######################################


    @st.cache_data
    def load_data(path: str):
        df = pd.read_excel(path)
        return df


    df = load_data(uploaded_file)
    all_months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    with st.expander("Data Preview"):
        st.dataframe(
            df,
            column_config={"Year": st.column_config.NumberColumn(format="%d")},
        )

    #######################################
    # VISUALIZATION METHODS
    #######################################


    def plot_metric(label, value, prefix="", suffix="", show_graph=False, color_graph=""):
        fig = go.Figure()

        fig.add_trace(
            go.Indicator(
                value=value,
                gauge={"axis": {"visible": False}},
                number={
                    "prefix": prefix,
                    "suffix": suffix,
                    "font.size": 28,
                },
                title={
                    "text": label,
                    "font": {"size": 24},
                },
            )
        )

        if show_graph:
            fig.add_trace(
                go.Scatter(
                    y=random.sample(range(0, 101), 30),
                    hoverinfo="skip",
                    fill="tozeroy",
                    fillcolor=color_graph,
                    line={
                        "color": color_graph,
                    },
                )
            )

        fig.update_xaxes(visible=False, fixedrange=True)
        fig.update_yaxes(visible=False, fixedrange=True)
        fig.update_layout(
            # paper_bgcolor="lightgrey",
            margin=dict(t=30, b=0),
            showlegend=False,
            plot_bgcolor="white",
            height=100,
        )

        st.plotly_chart(fig, use_container_width=True)


    def plot_gauge(
        indicator_number, indicator_color, indicator_suffix, indicator_title, max_bound
    ):
        fig = go.Figure(
            go.Indicator(
                value=indicator_number,
                mode="gauge+number",
                domain={"x": [0, 1], "y": [0, 1]},
                number={
                    "suffix": indicator_suffix,
                    "font.size": 26,
                },
                gauge={
                    "axis": {"range": [0, max_bound], "tickwidth": 1},
                    "bar": {"color": indicator_color},
                },
                title={
                    "text": indicator_title,
                    "font": {"size": 28},
                },
            )
        )
        fig.update_layout(
            # paper_bgcolor="lightgrey",
            height=200,
            margin=dict(l=10, r=10, t=50, b=10, pad=8),
        )
        st.plotly_chart(fig, use_container_width=True)


    def plot_top_right():
        sales_data = duckdb.sql(
            f"""
            WITH sales_data AS (
                UNPIVOT ( 
                    SELECT 
                        Scenario,
                        business_unit,
                        {','.join(all_months)} 
                        FROM df 
                        WHERE Year='2023' 
                        AND Account='Sales' 
                    ) 
                ON {','.join(all_months)}
                INTO
                    NAME month
                    VALUE sales
            ),

            aggregated_sales AS (
                SELECT
                    Scenario,
                    business_unit,
                    SUM(sales) AS sales
                FROM sales_data
                GROUP BY Scenario, business_unit
            )
            
            SELECT * FROM aggregated_sales
            """
        ).df()

        fig = px.bar(
            sales_data,
            x="business_unit",
            y="sales",
            color="Scenario",
            barmode="group",
            text_auto=".2s",
            title="Sales for Year 2023",
            height=400,
        )
        fig.update_traces(
            textfont_size=12, textangle=0, textposition="outside", cliponaxis=False
        )
        st.plotly_chart(fig, use_container_width=True)


    def plot_bottom_left():
        sales_data = duckdb.sql(
            f"""
            WITH sales_data AS (
                SELECT 
                Scenario,{','.join(all_months)} 
                FROM df 
                WHERE Year='2023' 
                AND Account='Sales'
                AND business_unit='Software'
            )

            UNPIVOT sales_data 
            ON {','.join(all_months)}
            INTO
                NAME month
                VALUE sales
        """
        ).df()

        fig = px.line(
            sales_data,
            x="month",
            y="sales",
            color="Scenario",
            markers=True,
            text="sales",
            title="Monthly Budget vs Forecast 2023",
        )
        fig.update_traces(textposition="top center")
        st.plotly_chart(fig, use_container_width=True)


    def plot_bottom_right():
        sales_data = duckdb.sql(
            f"""
            WITH sales_data AS (
                UNPIVOT ( 
                    SELECT 
                        Account,Year,{','.join([f'ABS({month}) AS {month}' for month in all_months])}
                        FROM df 
                        WHERE Scenario='Actuals'
                        AND Account!='Sales'
                    ) 
                ON {','.join(all_months)}
                INTO
                    NAME year
                    VALUE sales
            ),

            aggregated_sales AS (
                SELECT
                    Account,
                    Year,
                    SUM(sales) AS sales
                FROM sales_data
                GROUP BY Account, Year
            )
            
            SELECT * FROM aggregated_sales
        """
        ).df()

        fig = px.bar(
            sales_data,
            x="Year",
            y="sales",
            color="Account",
            title="Actual Yearly Sales Per Account",
        )
        st.plotly_chart(fig, use_container_width=True)


    #######################################
    # STREAMLIT LAYOUT
    #######################################

    top_left_column, top_right_column = st.columns((2, 1))
    bottom_left_column, bottom_right_column = st.columns(2)

    with top_left_column:
        column_1, column_2, column_3, column_4 = st.columns(4)

        with column_1:
            plot_metric(
                "Total Accounts Receivable",
                6621280,
                prefix="$",
                suffix="",
                show_graph=True,
                color_graph="rgba(0, 104, 201, 0.2)",
            )
            plot_gauge(1.86, "#0068C9", "%", "Current Ratio", 3)

        with column_2:
            plot_metric(
                "Total Accounts Payable",
                1630270,
                prefix="$",
                suffix="",
                show_graph=True,
                color_graph="rgba(255, 43, 43, 0.2)",
            )
            plot_gauge(10, "#FF8700", " days", "In Stock", 31)

        with column_3:
            plot_metric("Equity Ratio", 75.38, prefix="", suffix=" %", show_graph=False)
            plot_gauge(7, "#FF2B2B", " days", "Out Stock", 31)
            
        with column_4:
            plot_metric("Debt Equity", 1.10, prefix="", suffix=" %", show_graph=False)
            plot_gauge(28, "#29B09D", " days", "Delay", 31)

    with top_right_column:
        plot_top_right()

    with bottom_left_column:
        plot_bottom_left()

    with bottom_right_column:
        plot_bottom_right()

 

# Multi-page navigation
pages = {
    "🤓Homepage": login,
    "📚Projects": projects_page,
    "💬Contact": contacts,
}

# Sidebar for navigation
selected_page = st.sidebar.radio("Navigation", list(pages.keys()))

# Display the selected page, and restrict access to the Projects page
if selected_page == "📚Projects" and not st.session_state.get("logged_in"):
    st.warning("Please log in to access this page.")
else:
    if selected_page == "🤓Homepage":
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

import streamlit as st
import pandas as pd

# Apply custom styles for a sea green theme
st.markdown(
    """
    <style>
    /* General styling */
    body {
        background-color: #ffffff;
        color: #333333;
        font-family: "Arial", sans-serif;
    }

    /* Title and header styling */
    .title, .header {
        color: #333333;
        text-align: center;
        font-weight: bold;
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #2e8b57;
        padding: 15px;
        border-radius: 10px;
        color: white;
    }
    .sidebar .sidebar-content h2 {
        color: white;
    }

    /* DataFrame styling */
    .dataframe td, .dataframe th {
        padding: 10px;
        text-align: center;
        border: 1px solid #ddd;
        font-family: Arial, sans-serif;
    }
    .dataframe th {
        background-color: #2e8b57;
        color: #ffffff;
    }
    .dataframe td {
        background-color: #f7fff7;
        color: #333333;
    }

    /* Google Maps links */
    a {
        color: #2e8b57;
        font-weight: bold;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
        color: #3cb371;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app
st.markdown('<h1 class="title"> Potential Sellers Dashboard</h1>', unsafe_allow_html=True)

st.write(
    """
    Welcome to the **Potential Sellers Dashboard**! This interactive app lets you explore properties
    with filters for **state**, **city**, and **property type**. View property details, including assessed 
    value and sale amount, along with clickable Google Maps links for each property.
    """
)

# Dummy Data for Table
data = {
    "Name": ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", "Alice Green", "Robert Brown"],
    "Address": [
        "123 Elm Street, New York, NY",
        "456 Oak Avenue, Los Angeles, CA",
        "789 Pine Road, Chicago, IL",
        "321 Maple Lane, Houston, TX",
        "22 Ocean Drive, New Haven, CT",
        "85 River Street, Stamford, CT"
    ],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "New Haven", "Stamford"],
    "State": ["NY", "CA", "IL", "TX", "CT", "CT"],
    "Property Type": ["Residential", "Commercial", "Industrial", "Residential", "Commercial", "Residential"],
    "Assessed Value ($)": [500000, 1200000, 2500000, 800000, 600000, 450000],
    "Sale Amount ($)": [550000, 1250000, 2600000, 850000, 620000, 470000],
    "Google Maps Link": [
        "https://www.google.com/maps?q=123+Elm+Street,+New+York,+NY",
        "https://www.google.com/maps?q=456+Oak+Avenue,+Los+Angeles,+CA",
        "https://www.google.com/maps?q=789+Pine+Road,+Chicago,+IL",
        "https://www.google.com/maps?q=321+Maple+Lane,+Houston,+TX",
        "https://www.google.com/maps?q=22+Ocean+Drive,+New+Haven,+CT",
        "https://www.google.com/maps?q=85+River+Street,+Stamford,+CT"
    ]
}

# Convert data to a Pandas DataFrame
df = pd.DataFrame(data)

# Sidebar Filters
st.sidebar.markdown('<h2>🔎 Filters</h2>', unsafe_allow_html=True)
states = st.sidebar.multiselect("Select State(s)", options=df["State"].unique(), default=df["State"].unique())
cities = st.sidebar.multiselect("Select City(s)", options=df["City"].unique(), default=df["City"].unique())
property_types = st.sidebar.multiselect("Select Property Type(s)", options=df["Property Type"].unique(), default=df["Property Type"].unique())

# Apply Filters
filtered_df = df[
    (df["State"].isin(states)) &
    (df["City"].isin(cities)) &
    (df["Property Type"].isin(property_types))
]

# Display Filtered Data as a Table
st.markdown('<h2 class="header"> Filtered Results</h2>', unsafe_allow_html=True)
st.write(
    "Here are the filtered results based on your selected criteria. You can view the property details, "
    "including **assessed value**, **sale amount**, and Google Maps links for navigation."
)

st.dataframe(
    filtered_df[["Name", "Address", "City", "State", "Property Type", "Assessed Value ($)", "Sale Amount ($)"]],
    use_container_width=True
)

# Add clickable Google Maps links
st.markdown('<h2 class="header"> Google Maps Links</h2>', unsafe_allow_html=True)
for i, row in filtered_df.iterrows():
    st.markdown(f"🔗 [{row['Address']}]({row['Google Maps Link']})")

st.info("This is a demo UI. Real data will be displayed once connected to the model or API.")  
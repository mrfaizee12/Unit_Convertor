import streamlit as st

# Page Configurations
st.set_page_config(page_title="Smart Unit Converter", page_icon="🔄", layout="centered")

# Theme Toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

# Custom CSS for Dark/Light Mode
if dark_mode:
    st.markdown(
        """
        <style>
            body, .stApp { background-color: #1e1e2f; color: #ffffff; }
            .title { color: #14ffec; }
            .subtitle, .footer { color: #bbb; }
            .stButton>button { background: linear-gradient(to right, #14ffec, #0f3443); color: white; }
            .sidebar-title { color: #14ffec; }
            .stSelectbox label, .stNumberInput label { color: #14ffec; }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
            body, .stApp { background-color: #ffffff; color: #000000; }
            .title { color: #0f3443; }
            .subtitle, .footer { color: #333; }
            .stButton>button { background: linear-gradient(to right, #0f3443, #14ffec); color: black; }
            .sidebar-title { color: #0f3443; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Page Header
st.markdown("<h1 class='title'>Smart Unit Converter 🚀</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Convert Anything Instantly</h2>", unsafe_allow_html=True)
st.write("")

# Sidebar
st.sidebar.markdown("<p class='sidebar-title'>🔍 Choose a Category</p>", unsafe_allow_html=True)

# Conversion Data
conversion_data = {
    "Length": { "Millimeter": 0.001, "Centimeter": 0.01, "Meter": 1, "Kilometer": 1000, "Inch": 0.0254, "Foot": 0.3048, "Yard": 0.9144, "Mile": 1609.34 },
    "Mass": { "Milligram": 0.000001, "Gram": 0.001, "Kilogram": 1, "Ton": 1000, "Ounce": 0.0283495, "Pound": 0.453592 },
    "Temperature": { "Celsius": lambda c: c, "Fahrenheit": lambda f: (f - 32) * 5/9, "Kelvin": lambda k: k - 273.15 },
    "Area": { "Square Meter": 1, "Square Kilometer": 1000000, "Hectare": 10000, "Square Foot": 0.092903, "Acre": 4046.86 },
    "Volume": { "Milliliter": 0.001, "Liter": 1, "Cubic Meter": 1000, "Cubic Inch": 0.0163871, "Cubic Foot": 28.3168, "Gallon": 3.78541 },
    "Time": { "Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400, "Week": 604800 }
}

# Sidebar Category Selection
category = st.sidebar.selectbox("", list(conversion_data.keys()))

# User Inputs
unit_list = list(conversion_data[category].keys())
from_unit = st.selectbox("🎯 Convert From", unit_list)
to_unit = st.selectbox("🎯 Convert To", unit_list)
input_value = st.number_input("📌 Enter Value", value=0.0, step=0.1)

# Convert Button
if st.button("Convert Now 🚀"):
    from_conversion = conversion_data[category][from_unit]
    to_conversion = conversion_data[category][to_unit]

    if callable(from_conversion):
        result = to_conversion(from_conversion(input_value))
    else:
        result = (input_value * from_conversion) / to_conversion

    st.success(f"🎉 {input_value} {from_unit} = {result:.4f} {to_unit}")

# Footer
st.markdown("---")
st.markdown("<p class='footer'>✨ Created by <b style='color:#ff79c6;'>Faizee</b> with ❤️</p>", unsafe_allow_html=True)

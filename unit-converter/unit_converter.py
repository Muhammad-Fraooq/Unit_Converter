import streamlit as st

# Streamlit config
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🚀",
    layout='wide',
)

def unit_convert(value, unit_from, unit_to):
    conversion = {
        # Length
        "meters_kilometers": 0.001,      # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,       # 1 kilometer = 1000 meters
        "meters_centimeters": 100,       # 1 meter = 100 centimeters
        "centimeters_meters": 0.01,      # 1 centimeter = 0.01 meters
        "meters_millimeters": 1000,      # 1 meter = 1000 millimeters
        "millimeters_meters": 0.001,     # 1 millimeter = 0.001 meters
        "meters_miles": 0.000621371,     # 1 meter = 0.000621371 miles
        "miles_meters": 1609.34,         # 1 mile = 1609.34 meters
        "meters_feet": 3.28084,          # 1 meter = 3.28084 feet
        "feet_meters": 0.3048,           # 1 foot = 0.3048 meters
        "meters_inches": 39.3701,        # 1 meter = 39.3701 inches
        "inches_meters": 0.0254,         # 1 inch = 0.0254 meters
        # Weight/Mass
        "grams_kilograms": 0.001,        # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,         # 1 kilogram = 1000 grams
        "grams_milligrams": 1000,        # 1 gram = 1000 milligrams
        "milligrams_grams": 0.001,       # 1 milligram = 0.001 grams
        "kilograms_pounds": 2.20462,     # 1 kilogram = 2.20462 pounds
        "pounds_kilograms": 0.453592,    # 1 pound = 0.453592 kilograms
        "grams_ounces": 0.035274,       # 1 gram = 0.035274 ounces
        "ounces_grams": 28.3495,         # 1 ounce = 28.3495 grams
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversion:
        conversion_factor = conversion[key]
        return (
            conversion_factor(value) if callable(conversion_factor) else value * conversion_factor
        )  
    else:
        return 'Conversion not supported'  # Fixed typo from 'Converstion' to 'Conversion'

# Enhanced Heading and Welcome Section
st.markdown("""
    <h1 style='text-align: center; color: #1E90FF;'>
        🚀 Universal Unit Converter
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; color: #555;'>
        <h3>Welcome to the Ultimate Conversion Tool!</h3>
        <p>Easily convert between length and weight units with precision and speed. 
        Select your units, enter a value, and let us do the math for you!</p>
    </div>
""", unsafe_allow_html=True)

# Main Converter Section
st.markdown("---")  # Horizontal line for separation

col1, col2, col3 = st.columns([2, 2, 2])  # Create a 3-column layout for better spacing

with col1:
    value = st.number_input('Enter the value: ',)

with col2:
    unit_from = st.selectbox("Convert from: ", [
        "meters", "kilometers", "centimeters", "millimeters", "miles", "feet", "inches",
        "grams", "kilograms", "milligrams", "pounds", "ounces"
    ])

with col3:
    unit_to = st.selectbox("Convert to: ", [
        "meters", "kilometers", "centimeters", "millimeters", "miles", "feet", "inches",
        "grams", "kilograms", "milligrams", "pounds", "ounces"
    ])

# Center the Convert button
st.markdown("<div style='text-align: center; '>", unsafe_allow_html=True)
if st.button("Convert", key="convert_btn"):
    result = unit_convert(value, unit_from, unit_to)
    st.success(f"Converted value: {result}")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")  # Horizontal line for separation
st.markdown("""
    <div style='text-align: center; color: #777; font-size: 14px;'>
        <p>Developed with ❤️ by Muhammad Farooq | Powered by Streamlit | © 2025</p>
        <p>Need more units? Contact us at <a href='mailto:muhammad888xyz@gmail.com'>muhammad888xyz@gmail.com</a></p>
    </div>
""", unsafe_allow_html=True)
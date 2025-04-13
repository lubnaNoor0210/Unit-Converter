import streamlit as st

st.title("Unit Converter")
st.markdown("### Common Unit Converter")
st.write("Enter the value to convert!")

category = st.selectbox("Choose A Category", ["Length", "Weight", "Time"])

unit_options = {
    "Length": ["Kilometers to meter", "Meter to Kilometers", "Centimeter to millimeter", "Millimeter to centimeter", "Foot to inch", "Inch to foot"],
    "Weight": ["Kilograms to grams", "Grams to kilograms", "Kilograms to pounds", "Pounds to kilograms"],
    "Time": ["Seconds to minutes", "Minutes to seconds", "Hours to minutes", "Minutes to hours", "Hours to seconds", "Seconds to hours", "Second to millisecond", "Millisecond to second"]
}

unit = st.selectbox("Select Conversion", unit_options[category])
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

def convert_units(category, value, unit):
    if category == "Length":   # conditional statement
        # Dictionary and Arithmetic Operators performs math for each conversion and stores in dictinaory
        conversions = {
            "Kilometers to meter": value * 1000,
            "Meter to Kilometers": value / 1000,
            "Centimeter to millimeter": value * 10,
            "Millimeter to centimeter": value / 10,
            "Foot to inch": value * 12,
            "Inch to foot": value / 12
        }
    elif category == "Weight":
        conversions = {
            "Kilograms to grams": value * 1000,
            "Grams to kilograms": value / 1000,
            "Kilograms to pounds": value * 2.2046244202,
            "Pounds to kilograms": value / 2.2046244202
        }
    elif category == "Time":
        conversions = {
            "Seconds to minutes": value / 60,
            "Minutes to seconds": value * 60,
            "Hours to minutes": value * 60,
            "Minutes to hours": value / 60,
            "Hours to seconds": value * 3600,
            "Seconds to hours": value / 3600,
            "Second to millisecond": value * 1000,
            "Millisecond to second": value / 1000
        }
    return conversions.get(unit, "Invalid conversion") # get() disctinary method Returns the result of the selected conversion or shows "Invalid conversion" if not found.

if st.button("Convert"):
    result = convert_units(category, value, unit) #Function Call & Variable Assignment, stores the result in result varibale
    st.success(f"The result is {result:.2f}") # string formatting

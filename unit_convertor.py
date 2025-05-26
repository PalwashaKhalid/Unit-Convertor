# import
import streamlit as st

# Making a funtion having conversion parameters
def convert_units(value, unit_from, unit_to):

    # Create a dictionary for conversion Parameter:
    conversions= {
        "meters_kilometers" : 0.001,
        "kilometers_meters" : 1000,
        "grams_kilograms" : 0.001,
        "kilograms_grams" : 1000 
    }
    
    # Generate a unique keyfor conversion:
    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion is not Supported"
    
st.title("Unit Convertor")
value = st.number_input("Enter the Value: ")
unit_from = st.selectbox("Convert from: ", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to: ", ["meters", "kilometers", "grams", "kilograms"] )
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")
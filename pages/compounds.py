import streamlit as st
import pandas as pd
import math
def main():
    st.title("Compound Mole Calculater")

    total_elements = st.number_input("Enter the total number of elements: ", 1)
    periodic_data = pd.read_csv("https://gist.githubusercontent.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee/raw/1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic%2520Table%2520of%2520Elements.csv")
    elements = []

    numElement = []

    for i in range(total_elements):
        user_element = st.selectbox(f"Select Element {i + 1}", periodic_data["Element"])
        elements.append(user_element)
        numberOfElementinCompound = st.number_input(f"How many times is {user_element} in the compound", 1, key = f"input_{i}")
        numElement.append(numberOfElementinCompound)
        

    total_molar_mass = 0

    for element, num_element in zip(elements, numElement):
        molar_mass = periodic_data.loc[periodic_data["Element"] == element, "AtomicMass"].iloc[0]
        total_molar_mass += molar_mass * num_element
        
    mass = st.number_input("Enter the mass of the compound (in grams): ")
    numOfMoles = mass/total_molar_mass

    compound_formula = ""

    for element, num_element in zip(elements, numElement):
        symbol = periodic_data.loc[periodic_data["Element"] == element, "Symbol"].iloc[0]
        if num_element == 1: 
            compound_formula += symbol
        else:
            compound_formula += f"{symbol}{str(num_element).translate(str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉'))}"

    if numOfMoles > 0:
        exponent = int(math.log10(numOfMoles))
        st.write(f"There is {numOfMoles:.2f}*10^{exponent} moles of {compound_formula} in {mass:.2f}g")

    elif numOfMoles == 0:
        exponent = 0
        st.write(f"There is {numOfMoles:.2f} moles of {compound_formula} in {mass:.2f}g")

if __name__ == "__main__":
    main()

    


    
    

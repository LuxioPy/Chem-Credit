import streamlit as st 
import pandas as pd
import math 

periodic_data = pd.read_csv("https://gist.githubusercontent.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee/raw/1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic%2520Table%2520of%2520Elements.csv")
def main():
    st.title('Moles Calculator')
    user_element_dropdown = st.selectbox("Choose an Element", periodic_data["Element"])
    if user_element_dropdown:
        mass = st.number_input("Enter the mass of the element (in grams): ")
        if mass == 0:
            st.write("Enter a mass greater than zero :rage:")
        elif mass < 0:
            st.write("Seirously a negative mass??? :confused:")
        elif st.button("Calculate Number of Moles"):
            atomic_mass = periodic_data.loc[periodic_data["Element"] == user_element_dropdown, "AtomicMass"].iloc[0]
            numofMoles = mass/atomic_mass
            st.write(f"There is {numofMoles:.2f}*10^{int(math.log10(numofMoles))} moles of {str(user_element_dropdown)} in {mass:.2f}g")


if __name__ == "__main__":
    main()
import streamlit as st 
import pandas as pd

periodic_data = pd.read_csv("https://gist.githubusercontent.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee/raw/1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic%2520Table%2520of%2520Elements.csv")
def main():
    st.title('Moles Calculator')
    user_element_dropdown = st.selectbox("Choose an Element", periodic_data["Element"])
    if user_element_dropdown:
        mass = st.number_input("Enter the mass of the element (in grams): ")
        if st.button("Calculate Number of Moles"):
            element_data = periodic_data.loc[periodic_table_data["elements"].apply(lambda x: x["name"]) == selected_element].iloc[0]["elements"]


if __name__ == "__main__":
    main()
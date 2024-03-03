# Moles Calculator and Compound Mole Calculator

These Streamlit applications are designed to calculate the number of moles of an element or compound given certain parameters. 

## Moles Calculator

The Moles Calculator allows users to input the mass of an element and then calculates the number of moles of that element based on its atomic mass. The user selects an element from a dropdown menu, inputs the mass in grams, and then clicks a button to calculate the number of moles. The calculated result is displayed on the screen.

## Compound Mole Calculator

The Compound Mole Calculator extends the functionality to calculate the number of moles for compounds. Users input the total number of elements in the compound, select each element along with the number of times it appears in the compound, and then input the mass of the compound in grams. The application then calculates the total molar mass of the compound based on the sum of the molar masses of its constituent elements and computes the number of moles. It displays the result in scientific notation along with the compound's chemical formula.

## Usage

To use these applications, make sure you have the necessary libraries installed (Streamlit, Pandas, Math), and run the respective Python scripts. The applications will launch in your web browser, allowing you to interact with them as described above.

## Data Source

Both applications utilize periodic table data sourced from the following link:
[Periodic Table of Elements CSV](https://gist.githubusercontent.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee/raw/1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic%2520Table%2520of%2520Elements.csv)

## Notes

- Mass inputs must be greater than zero.
- Negative mass inputs are not accepted.
- The calculations assume standard atomic masses for elements and compounds.
- Scientific notation is used to display very large or very small numbers.

These applications are useful for educational purposes or for quick calculations in chemistry-related tasks. Enjoy using them!

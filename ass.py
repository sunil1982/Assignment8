import streamlit as st


st.write('Largest of three numbers ')


def main():

    st.title('Find the Largest Number')
    st.write('Enter three number and then click on the buutton to find the largest')
    

num1 = st.number_input("Enter first number: ")
num2 = st.number_input("Enter second number: ")
num3 = st.number_input("Enter third number: ")
largest_num=0


if st.button("Find the Largest number"):
    if (num1 >= num2) and (num1 >= num3):
       largest_num = num1
    elif (num2 >= num1) and (num2 >= num3):
       largest_num = num2
    else:
       largest_num = num3


st.write("The largest number is :", largest_num)



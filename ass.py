{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install -q streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "\n",
    "st.write('Largest of three numbers ')\n",
    "\n",
    "\n",
    "def main():\n",
    "\n",
    "    st.title('Find the Largest Number')\n",
    "    st.write('Enter three number and then click on the buutton to find the largest')\n",
    "    \n",
    "\n",
    "num1 = float(st.number_input(\"Enter first number: \"))\n",
    "num2 = float(st.number_input(\"Enter second number: \"))\n",
    "num3 = float(st.number_input(\"Enter third number: \"))\n",
    "largest_num=0\n",
    "\n",
    "\n",
    "if st.button(\"Find the Largest number\"):\n",
    "    if (num1 >= num2) and (num1 >= num3):\n",
    "       largest_num = num1\n",
    "    elif (num2 >= num1) and (num2 >= num3):\n",
    "       largest_num = num2\n",
    "    else:\n",
    "       largest_num = num3\n",
    "\n",
    "\n",
    "st.write(\"The largest number is :\", largest_num)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!streamlit run C:\\Users\\DELL\\Desktop\\ass.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

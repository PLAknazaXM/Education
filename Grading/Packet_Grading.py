import streamlit as st
import numpy as np

st.set_page_config(page_title="Packet Grading App",
                   page_icon=":check_mark:", layout="wide")

st.title('Packet Grading Program')
#st.sidebar.success("Select a page above")


st.markdown('''This provides a quick and simple method to grade
packets, providing fractional and percentage grades.''')

Total = st.number_input('Enter the total point value of the packet:', step = 1)

Points_float = (0,0)

Earn = st.text_input('''Enter the number of points lost on each page, separated by commas, spaces, or dashes.
Ex: 1,5,13 OR 1 5 13 OR 1-5-13''')

try:
    Points = Earn.split('-')
    Points_float = [float(x) for x in Points]
except:
    try:
        Points = Earn.split(' ')
        Points_float = [float(x) for x in Points]
    except:
        try:
            Points = Earn.split(',')
            Points_float = [float(x) for x in Points]
        except:
            st.title('Invalid method of entering points earned!')

EC = st.text_input('''Enter the points awarded through extra credit.
Enter 0 if none''')

try:
    EC = float(EC)
except:
    EC = 0

Total_Lost = sum(Points_float)

Total_Earn = Total - Total_Lost + EC

if Total == 0:
    st.write('Configure total points of assignment')
else:
    st.write('''Fractional Grade:''', Total_Earn, '/', Total)
    st.write('Percentage Grade: ', round(Total_Earn/Total*100,2), '%')


st.text('''Version 1.2.1
1.0 Creation of app
1.1 Points entered are now the points that were lost rather than earned.
1.2 Added extra credit option
1.2.1 Adjusted point entry to integer if using the plus/minus buttons''')

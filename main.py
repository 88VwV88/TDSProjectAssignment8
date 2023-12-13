import streamlit as st

st.write('''
# Greatest of three numbers: 
''')

st.write('''### Please enter 3 numbers: ''')

a = st.text_input('a')
b = st.text_input('b')
c = st.text_input('c')
if st.button('Submit'):
    a, b, c = int(a), int(b), int(c)
    st.write(f'''The greatest number is: {max(a, b, c)}''')
else:
    st.write('''*Please enter valid numbers!*''')
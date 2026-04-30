import pandas as pd
import streamlit as st
from db.db import get_conn, init_db

init_db()
st.title('Animal Master')

with st.form('add_animal'):
    st.subheader('Add Animal')
    tag_no = st.text_input('Tag No')
    name = st.text_input('Name')
    breed = st.text_input('Breed', value='HF Cross')
    sex = st.selectbox('Sex', ['F', 'M'])
    dob = st.date_input('Date of Birth')
    lactation_no = st.number_input('Lactation No', min_value=0, value=0)
    purchase_price = st.number_input('Purchase Price', min_value=0.0, value=0.0)
    submitted = st.form_submit_button('Save')

if submitted and tag_no.strip():
    with get_conn() as conn:
        conn.execute(
            '''INSERT INTO animals (tag_no, name, breed, sex, dob, lactation_no, purchase_price)
               VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (tag_no.strip(), name.strip(), breed.strip(), sex, str(dob), lactation_no, purchase_price),
        )
        conn.commit()
    st.success('Animal added successfully')

with get_conn() as conn:
    animals = pd.read_sql_query('SELECT * FROM animals ORDER BY id DESC', conn)

st.dataframe(animals, use_container_width=True)

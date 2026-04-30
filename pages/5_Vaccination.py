import pandas as pd
import streamlit as st
from db.db import get_conn, init_db
init_db(); st.title('Vaccination')
with get_conn() as conn:
    animals = pd.read_sql_query('SELECT id, tag_no FROM animals ORDER BY tag_no', conn)
with st.form('vax'):
    aid = st.selectbox('Animal', animals['id'].tolist(), format_func=lambda x: animals[animals.id==x]['tag_no'].iloc[0])
    vaccine = st.text_input('Vaccine')
    vdate = st.date_input('Vaccination Date')
    next_due = st.date_input('Next Due Date')
    cost = st.number_input('Cost', min_value=0.0, value=0.0)
    ok = st.form_submit_button('Save')
if ok and vaccine:
    with get_conn() as conn:
        conn.execute('INSERT INTO vaccinations (animal_id,vaccine_name,vaccination_date,next_due_date,cost) VALUES (?,?,?,?,?)',(aid,vaccine,str(vdate),str(next_due),cost)); conn.commit()
    st.success('Saved')

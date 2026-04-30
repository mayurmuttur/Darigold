import pandas as pd
import streamlit as st
from db.db import get_conn, init_db

init_db(); st.title('Health Records')
with get_conn() as conn:
    animals = pd.read_sql_query('SELECT id, tag_no FROM animals ORDER BY tag_no', conn)

with st.form('health_form'):
    aid = st.selectbox('Animal', animals['id'].tolist(), format_func=lambda x: animals[animals.id==x]['tag_no'].iloc[0])
    visit_date = st.date_input('Visit Date')
    condition = st.text_input('Condition')
    treatment = st.text_input('Treatment')
    vet_name = st.text_input('Vet Name')
    cost = st.number_input('Cost', min_value=0.0, value=0.0)
    ok = st.form_submit_button('Save')
if ok and condition:
    with get_conn() as conn:
        conn.execute('INSERT INTO health_records (animal_id, visit_date, condition, treatment, vet_name, cost) VALUES (?,?,?,?,?,?)',(aid,str(visit_date),condition,treatment,vet_name,cost)); conn.commit()
    st.success('Saved')
with get_conn() as conn:
    st.dataframe(pd.read_sql_query('SELECT h.visit_date,a.tag_no,h.condition,h.treatment,h.vet_name,h.cost FROM health_records h JOIN animals a ON a.id=h.animal_id ORDER BY h.id DESC',conn), use_container_width=True)

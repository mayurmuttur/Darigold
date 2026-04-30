import pandas as pd
import streamlit as st
from db.db import get_conn, init_db
init_db(); st.title('Breeding')
with get_conn() as conn:
    animals = pd.read_sql_query("SELECT id, tag_no FROM animals WHERE sex='F' ORDER BY tag_no", conn)
with st.form('breed'):
    aid = st.selectbox('Animal', animals['id'].tolist(), format_func=lambda x: animals[animals.id==x]['tag_no'].iloc[0])
    sdate = st.date_input('Service Date')
    sire = st.text_input('Sire Name')
    method = st.selectbox('Method', ['AI', 'Natural'])
    pcheck = st.date_input('Pregnancy Check Date')
    result = st.selectbox('Result', ['Pending', 'Positive', 'Negative'])
    ecd = st.date_input('Expected Calving Date')
    ok = st.form_submit_button('Save')
if ok:
    with get_conn() as conn:
        conn.execute('INSERT INTO breeding_records (animal_id,service_date,sire_name,method,pregnancy_check_date,result,expected_calving_date) VALUES (?,?,?,?,?,?,?)',(aid,str(sdate),sire,method,str(pcheck),result,str(ecd))); conn.commit()
    st.success('Saved')

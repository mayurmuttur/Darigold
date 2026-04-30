import pandas as pd
import streamlit as st
from db.db import get_conn, init_db
init_db(); st.title('Expenses')
with st.form('exp'):
    d = st.date_input('Date')
    cat = st.text_input('Category')
    desc = st.text_input('Description')
    amt = st.number_input('Amount', min_value=0.0, value=0.0)
    ok = st.form_submit_button('Save')
if ok and cat:
    with get_conn() as conn:
        conn.execute('INSERT INTO expenses (expense_date,category,description,amount) VALUES (?,?,?,?)',(str(d),cat,desc,amt)); conn.commit()
    st.success('Saved')
with get_conn() as conn:
    st.dataframe(pd.read_sql_query('SELECT * FROM expenses ORDER BY id DESC', conn), use_container_width=True)

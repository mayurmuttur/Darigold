import pandas as pd
import streamlit as st
from db.db import get_conn, init_db
init_db(); st.title('Feed Logs')
with st.form('feed'):
    d = st.date_input('Date')
    f = st.text_input('Feed Type')
    q = st.number_input('Quantity (kg)', min_value=0.0, value=0.0)
    c = st.number_input('Cost', min_value=0.0, value=0.0)
    ok = st.form_submit_button('Save')
if ok and f:
    with get_conn() as conn:
        conn.execute('INSERT INTO feed_logs (log_date,feed_type,quantity_kg,cost) VALUES (?,?,?,?)',(str(d),f,q,c)); conn.commit()
    st.success('Saved')
with get_conn() as conn:
    st.dataframe(pd.read_sql_query('SELECT * FROM feed_logs ORDER BY id DESC', conn), use_container_width=True)

import pandas as pd
import streamlit as st
from db.db import get_conn, init_db
init_db(); st.title('Reports')
with get_conn() as conn:
    milk_daily = pd.read_sql_query('SELECT entry_date, SUM(liters) total_liters FROM milk_yield GROUP BY entry_date ORDER BY entry_date DESC', conn)
    due_vax = pd.read_sql_query("SELECT a.tag_no, v.vaccine_name, v.next_due_date FROM vaccinations v JOIN animals a ON a.id=v.animal_id WHERE v.next_due_date >= date('now') ORDER BY v.next_due_date", conn)
st.subheader('Daily Milk Report')
st.dataframe(milk_daily, use_container_width=True)
st.subheader('Upcoming Vaccination Due')
st.dataframe(due_vax, use_container_width=True)

import streamlit as st
import pandas as pd
from db.db import get_conn, init_db

init_db()
st.title('Milk Yield Entry')

with get_conn() as conn:
    animals = pd.read_sql_query("SELECT id, tag_no || ' - ' || COALESCE(name, '') AS label FROM animals WHERE sex='F'", conn)

if animals.empty:
    st.warning('No female animals available.')
else:
    with st.form('milk_entry'):
        animal_label = st.selectbox('Animal', animals['label'].tolist())
        entry_date = st.date_input('Entry Date')
        session = st.selectbox('Session', ['Morning', 'Evening'])
        liters = st.number_input('Liters', min_value=0.0, value=0.0, step=0.1)
        submitted = st.form_submit_button('Save Entry')

    if submitted:
        animal_id = int(animals.loc[animals['label'] == animal_label, 'id'].iloc[0])
        with get_conn() as conn:
            conn.execute(
                'INSERT INTO milk_yield (animal_id, entry_date, session, liters) VALUES (?, ?, ?, ?)',
                (animal_id, str(entry_date), session, liters),
            )
            conn.commit()
        st.success('Milk yield recorded.')

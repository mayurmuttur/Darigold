import pandas as pd
import streamlit as st
from db.db import get_conn, init_db

init_db()
st.title('Animal Profile')

with get_conn() as conn:
    animals = pd.read_sql_query('SELECT id, tag_no, name, breed, sex, status FROM animals ORDER BY tag_no', conn)

if animals.empty:
    st.info('No animals found.')
else:
    pick = st.selectbox('Select Animal', (animals['tag_no'] + ' - ' + animals['name'].fillna('')).tolist())
    tag = pick.split(' - ')[0]
    row = animals[animals['tag_no'] == tag].iloc[0]

    c1, c2, c3 = st.columns(3)
    c1.metric('Tag', row['tag_no'])
    c2.metric('Breed', row['breed'])
    c3.metric('Status', row['status'])

    with get_conn() as conn:
        milk = pd.read_sql_query(
            '''SELECT entry_date, session, liters FROM milk_yield
               WHERE animal_id = ? ORDER BY entry_date DESC, id DESC''',
            conn,
            params=(int(row['id']),),
        )
        health = pd.read_sql_query(
            'SELECT visit_date, condition, treatment, cost FROM health_records WHERE animal_id = ? ORDER BY visit_date DESC',
            conn,
            params=(int(row['id']),),
        )

    st.subheader('Milk History')
    st.dataframe(milk, use_container_width=True)
    st.subheader('Health History')
    st.dataframe(health, use_container_width=True)

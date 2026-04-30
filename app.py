import pandas as pd
import streamlit as st

from db.db import get_conn, init_db

st.set_page_config(page_title='Darigold Dashboard', layout='wide')
init_db()

st.title('🐄 Darigold Dashboard')

with get_conn() as conn:
    animal_count = conn.execute('SELECT COUNT(*) FROM animals').fetchone()[0]
    milk_today = conn.execute("SELECT COALESCE(SUM(liters),0) FROM milk_yield WHERE entry_date = date('now')").fetchone()[0]
    sales_today = conn.execute("SELECT COALESCE(SUM(liters * rate_per_liter),0) FROM milk_sales WHERE sale_date = date('now')").fetchone()[0]
    expense_today = conn.execute("SELECT COALESCE(SUM(amount),0) FROM expenses WHERE expense_date = date('now')").fetchone()[0]

c1, c2, c3, c4 = st.columns(4)
c1.metric('Animals', animal_count)
c2.metric('Milk Today (L)', f'{milk_today:.1f}')
c3.metric('Sales Today', f'₹{sales_today:,.0f}')
c4.metric('Expenses Today', f'₹{expense_today:,.0f}')

st.subheader('Recent Milk Entries')
with get_conn() as conn:
    df = pd.read_sql_query('''
      SELECT m.entry_date, a.tag_no, a.name, m.session, m.liters
      FROM milk_yield m JOIN animals a ON m.animal_id = a.id
      ORDER BY m.entry_date DESC, m.id DESC LIMIT 20
    ''', conn)

st.dataframe(df, use_container_width=True)
st.info('Use the sidebar to open Animal Master, Milk Yield Entry, Animal Profile, and operational modules.')

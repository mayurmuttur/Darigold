import streamlit as st
from db.db import get_conn, init_db
init_db(); st.title('Profitability Snapshot')
with get_conn() as conn:
    rev = conn.execute('SELECT COALESCE(SUM(liters*rate_per_liter),0) FROM milk_sales').fetchone()[0]
    exp = conn.execute('SELECT COALESCE(SUM(amount),0) FROM expenses').fetchone()[0] + conn.execute('SELECT COALESCE(SUM(cost),0) FROM feed_logs').fetchone()[0]
profit = rev - exp
c1,c2,c3=st.columns(3)
c1.metric('Revenue', f'₹{rev:,.0f}')
c2.metric('Expense', f'₹{exp:,.0f}')
c3.metric('Profit', f'₹{profit:,.0f}')

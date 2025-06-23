import streamlit as st
import pandas as pd

df = pd.read_excel("SQL_Complete_Dictionary_A_to_Z.xlsx")

st.set_page_config(page_title="SQL Learning Dictionary", layout="wide")
st.title("📘 SQL Learning Dictionary A–Z")

st.sidebar.header("🔍 Filter Terms")
term_selected = st.sidebar.selectbox("Select SQL Term", sorted(df['Term'].unique()))
command_filter = st.sidebar.multiselect("Filter by Category (e.g. DML, Function)", df['Remark'].unique())

if command_filter:
    filtered_df = df[(df['Remark'].isin(command_filter)) & (df['Term'] == term_selected)]
else:
    filtered_df = df[df['Term'] == term_selected]

for _, row in filtered_df.iterrows():
    st.subheader(f"📌 Term: `{row['Term']}`")
    st.markdown(f"**Definition:** {row['Definition']}")
    st.markdown(f"**Use Case:** {row['Use Case']}")
    st.markdown(f"**Example:**\n```sql\n{row['Example']}```")
    st.markdown(f"**Code:**\n```sql\n{row['Code']}```")
    st.info(f"🔎 **Remark:** {row['Remark']}")

import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv('alwans_freezer.csv')
print(df.head())
print(df.columns)

st.set_page_config(page_title= "Alwan's Frozen Section", page_icon= "🧊🥩")

@st.cache_data
def load_data():
    df = pd.read_csv("alwans_freezer.csv")
    return df

df = load_data()

st.title("🧊 Alwan's Freezer Section")
st.write("Select a category and an item to see cooking instructions")

categories = sorted(df['CATEGORY'].unique().tolist())
selected_category = st.selectbox("Pick a category:", categories)

filtered_df = df[df["CATEGORY"] == selected_category]
items = filtered_df['NAME'].tolist()

selected_item = st.selectbox("Choose an item:", items)

if selected_item:
    item_data = filtered_df[filtered_df["NAME"] == selected_item].iloc[0]


    st.subheader("Ingredients")
    st.write(item_data["INGREDIENTS"])

    st.divider()
    st.header(f"How to prepare: {selected_item}")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Baking Instructions")
        st.info(item_data["COOKING_INSTRUCTIONS_BAKED"])
    
    with col2:
        st.subheader("Frying Instructions")
        st.info(item_data["COOKING_INSTRUCTIONS_FRIED"])
    
    st.divider()
    st.caption("Don't forget to check the package for specific oven variations!")
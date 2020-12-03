# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:11:42 2020

@author: PPG_Hugo
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff

st.title("streamlit demo")

@st.cache

def load_data(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower()

    return df

df = load_data("123.csv")

st.table(df.head(5))

author_list = df["author"].unique()

author_type = st.sidebar.selectbox(
    "Which author do you want to know?",
    author_list
)


part_df = df[(df["author"] == author_type)]
st.write(f"根据你的筛选，数据包含{len(part_df)}行")


st.title('使用streamlit的api画图')
sub_df = df[['id', 'price']]
sub_df = sub_df.groupby('id').agg(sum)
st.line_chart(sub_df["price"])


st.title('使用plotly的api画图')
fig = ff.create_distplot([sub_df['price']], group_labels = ['price'], bin_size=50)
st.plotly_chart(fig, use_container_width=True)


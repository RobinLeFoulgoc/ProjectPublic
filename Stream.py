#!/usr/bin/env python
# coding: utf-8
import GetData
import streamlit as st
from bokeh.plotting import figure
import matplotlib.pyplot as plt
import random
import numpy as np
def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#%02x%02x%02x' % (r, g, b)
def view(data):
    st.write(data)
    fig, ax = plt.subplots()
    data["GDP"].plot(kind='bar')
    st.pyplot(fig)

    for column in data.columns:
        p = figure(
            title=column,
            x_axis_label='date',
            y_axis_label=column,
            x_axis_type='datetime')
        p.line(x=data.index.tolist(), y=data[column], legend_label='Trend', line_width=2,line_color=generate_random_color())
        st.bokeh_chart(p, use_container_width=True)
    st.line_chart(data=data[["GDP","Public debt"]], x=None, y=None, width=50, height=0, use_container_width=True)
    st.line_chart(data=data[[ "CTB", "Public expenses"]], x=None, y=None, width=0, height=0,use_container_width=True)
    st.line_chart(data=data[["Inflation", "Unemployment"]], x=None, y=None, width=0, height=0, use_container_width=True)
D = GetData.get_cached_data()
view(D)
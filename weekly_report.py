import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel(r"new_report.xlsx")
df=df[['producer', 'change_quotes', 'change_nb_apps',
       'change_rw_apps', 'quotes', 'nb_apps', 'rw_apps', 'quotes.1',
       'nb_apps.1', 'rw_apps.1', 'quotes.2', 'nb_apps.2', 'rw_apps.2',
       'quotes.3', 'nb_apps.3', 'rw_apps.3']]

st.title('Weekly Report: JAN 22 - JAN 28 2023')
st.caption('_Data From: Top 25 Producers_')
#st.subheader('Dated: JAN 22 - JAN 28 2023')
#st.write('---')
#st.table(df.head())

# creating a slider
st.subheader('To view the report: Select the number of producers using the slider below: :point_down:')
slider_val=st.slider(label='', min_value=1, max_value=25, value=5, key=df['producer'])

st.caption(f'Number of Producers: {slider_val}')
st.subheader(f'Charts will change according to the slider value: {slider_val}')
st.write('---')

# avg of quotes, nb, rw apps side by side
st.subheader('Average Stats:')
st.caption(f'Based off slider value: {slider_val}')
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label='AVG Quotes', value=round(df['quotes'].head(slider_val).mean(), 2))
    
with col2:
    st.metric(label='AVG NB Apps', value=round(df['nb_apps'].head(slider_val).mean(), 2))
    
with col3:
    st.metric(label='AVG RW Apps', value=round(df['rw_apps'].head(slider_val).mean(), 2))
st.write('---')



st.subheader('Quotes by Producer:')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(x='producer', y='quotes', data=df.head(slider_val), ax=ax1)
ax1.set_facecolor("black")
fig.set_facecolor("black")
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax1.set_xlabel('PRODUCERS')
ax1.set_ylabel('# Quotes')
ax1.set_title('CURRENT QUOTES:  JAN 22 - JAN 28')
ax1.grid(axis='y')
ax1.bar_label(ax1.containers[0], rotation = 90, label_type='center')

sns.barplot(x='producer', y='quotes.1', data=df.head(slider_val), ax=ax2)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
ax2.set_xlabel('PRODUCERS')
ax2.set_ylabel('# Quotes')
ax2.set_title('PREVIOUS QUOTES:  JAN 15 - JAN 21')
ax2.grid(axis='y')
ax2.bar_label(ax2.containers[0], rotation = 90, label_type='center')


st.pyplot(fig)

st.subheader('NB Apps by Producer:')

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(x='producer', y='nb_apps', data=df.head(slider_val), ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax1.set_xlabel('PRODUCERS')
ax1.set_ylabel('# NB APPS')
ax1.set_title('CURRENT NB APPS:  JAN 22 - JAN 28')
ax1.grid(axis='y')
ax1.bar_label(ax1.containers[0], rotation = 90, label_type='center')


sns.barplot(x='producer', y='nb_apps.1', data=df.head(slider_val), ax=ax2)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
ax2.set_xlabel('PRODUCERS')
ax2.set_ylabel('# NB APPS')
ax2.set_title('PREVIOUS NB APPS:  JAN 15 - JAN 21')
ax2.grid(axis='y')
ax2.bar_label(ax2.containers[0], rotation = 90, label_type='center')


st.pyplot(fig2)

st.subheader('RW Apps by Producer:')

fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
sns.barplot(x='producer', y='rw_apps', data=df.head(slider_val), ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax1.set_xlabel('PRODUCERS')
ax1.set_ylabel('# RW APPS')
ax1.set_title('CURRENT RW APPS:  JAN 22 - JAN 28')
ax1.grid(axis='y')
ax1.bar_label(ax1.containers[0], rotation = 90, label_type='center')


sns.barplot(x='producer', y='rw_apps.1', data=df.head(slider_val), ax=ax2)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
ax2.set_xlabel('PRODUCERS')
ax2.set_ylabel('# RW APPS')
ax2.set_title('PREVIOUS RW APPS:  JAN 15 - JAN 21')
ax2.grid(axis='y')
ax2.bar_label(ax2.containers[0], rotation = 90, label_type='center')


st.pyplot(fig3)

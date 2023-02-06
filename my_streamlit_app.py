import streamlit as st
import pandas as pd
import seaborn as sns



st.title('Quete streamlit 1')



link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)

df_car

df_car_us =df_car[df_car['continent'].str.contains("US.")]


df_car_europe =df_car[df_car['continent'].str.contains("Europe.")]


df_car_japan =df_car[df_car['continent'].str.contains("Japan.")]

st.write('Repartition par pays selon le hp')
st.bar_chart(df_car,x='continent',y='hp')

st.write('Repartition par pays selon le weightlbs')
st.bar_chart(df_car,x='continent',y='weightlbs')

st.write('Repartition par pays selon le cubicinches')
st.bar_chart(df_car,x='continent',y='cubicinches')

US_button = st.button("US")

if US_button :
	st.write('Details des voitures au US')
	st.write(df_car_us)
	st.write('Heatmap US')
	viz_correlation_us = sns.heatmap(df_car_us.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

	st.pyplot(viz_correlation_us.figure)


Japan_button = st.button("Japan")

if Japan_button :
	st.write('Details des voitures au Japan')
	st.write(df_car_japan)
	st.write('Heatmap Japan')
	viz_correlation_japan = sns.heatmap(df_car_japan.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

	st.pyplot(viz_correlation_japan.figure)



Europe_button = st.button("Europe")

if Europe_button :
	st.write('Details des voitures en Europe')
	st.write(df_car_europe)
	st.write('Heatmap Europe')
	viz_correlation_europe = sns.heatmap(df_car_europe.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

	st.pyplot(viz_correlation_europe.figure)






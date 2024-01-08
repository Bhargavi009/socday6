import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1,col2=st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.video("https://www.youtube.com/watch?v=_Z9TRANg4c0",format="video/mp4", start_time=0)
  st.write("Persian cats are cute")
  with col2:
    st.subheader("Ragdoll Cat")
  st.image("https://github.com/Bhargavi009/socday6/blob/main/ragroll.jpg",caption="Ragdoll Cat",width=3000,use_column_width=True)
  st.write("Ragdoll cats are proud")

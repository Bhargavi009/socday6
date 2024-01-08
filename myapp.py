import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1,col2=st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("https://www.google.com/search?q=videos+link+on+ml&rlz=1C1GCEA_enIN1042IN1042&oq=videos+link+on+ml&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCggDECEYFhgdGB7SAQkxMDMwMmoxajeoAgCwAgA&sourceid=chrome&ie=UTF-8#",caption="Persian Cat",width=300,use_column_width=True)
  st.write("Persian cats are cute")
  with col2:
    st.subheader("Ragdoll Cat")
  st.image("https://github.com/Bhargavi009/socday6/blob/main/ragroll.jpg",caption="Ragdoll Cat",width=300,use_column_width=True)
  st.write("Ragdoll cats are proud")

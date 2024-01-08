import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1,col2=st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("https://media.istockphoto.com/id/1317748179/photo/ragdoll-cat-on-black-background.jpg?s=612x612&w=0&k=20&c=bsQUagSaeEoqGL4td7V2gOpQoDGy4jJ1GrSSHf7fyf8=",caption="Persian Cat",width=300,use_column_width=True)
  st.write("Persian cats are cute")
  with col2:
    st.subheader("Ragdoll Cat")
  st.image("https://media.istockphoto.com/id/1317748179/photo/ragdoll-cat-on-black-background.jpg?s=612x612&w=0&k=20&c=bsQUagSaeEoqGL4td7V2gOpQoDGy4jJ1GrSSHf7fyf8=",caption="Ragdoll Cat",width=300,use_column_width=True)
  st.write("Ragdoll cats are proud")

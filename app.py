import streamlit as st
from utils.constants import Choices as choices

st.set_page_config(layout="wide")


#sidebar
with st.sidebar:

    gender = st.selectbox("gender", choices.gender.value)
    if gender:
        st.session_state["gender"] = gender

    category = st.multiselect("category",choices.category.value)
    if category:
        st.session_state["category"] = category

    sub_category = st.multiselect("sub category", choices.sub_category.value)
    if sub_category :
        st.session_state["sub_category"] = sub_category

    article_type = st.multiselect("article", choices.article_type.value)
    if article_type :
        st.session_state["article_type"] = article_type

    usage = st.multiselect("usage", choices.usage.value)
    if article_type :
        st.session_state["usage"] = article_type







# Title of the app
st.title('A vector database recommendation engine')

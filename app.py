import os, json
import streamlit as st
from typing import List
from PIL import Image
from utils.constants import Choices as choices
from utils.configurations import SearchObject, settings
from vectordb.pinecone import pinecone
from langchain.schema import Document

st.set_page_config(layout="wide")

def search_recommendations():
    search_object = SearchObject(
        gender=st.session_state.get("gender",[""]),
        category=st.session_state.get("category",[""]),
        sub_category=st.session_state.get("sub_category",[""]),
        article_type=st.session_state.get("article_type",[""]),
        base_color=st.session_state.get("base_color",[""]),
        season=st.session_state.get("season",[""]),
        usage=st.session_state.get("usage",[""]),
        search=st.session_state.get("search",[""]),
    )

    query = search_object.search_query

    documents = pinecone.search_documents(query,20)

    for i in range(0, len(documents), 4):
        docs = documents[i:i+4]
        display_row(docs)

def display_row(docs: List[Document]):
    col1, col2, col3, col4 = st.columns(4)
    doc1, doc2, doc3, doc4 = docs
    expander_text = "more info"
    with col1.container():
        product_id = doc1.metadata.pop("id")
        image = Image.open(os.path.join(settings.IMAGES_PATH, product_id+".jpg"))
        st.image(image, caption=doc1.metadata.get("productDisplayName"))
        with st.expander(expander_text):
            st.json(doc1.metadata)
    with col2.container():
        product_id = doc2.metadata.pop("id")
        image = Image.open(os.path.join(settings.IMAGES_PATH, product_id+".jpg"))
        st.image(image, caption=doc2.metadata.get("productDisplayName"))
        with st.expander(expander_text):
            st.json(doc2.metadata)
    with col3.container():
        product_id = doc3.metadata.pop("id")
        image = Image.open(os.path.join(settings.IMAGES_PATH, product_id+".jpg"))
        st.image(image, caption=doc3.metadata.get("productDisplayName"))
        with st.expander(expander_text):
            st.json(doc3.metadata)
    with col4.container():
        product_id = doc4.metadata.pop("id")
        image = Image.open(os.path.join(settings.IMAGES_PATH, product_id+".jpg"))
        st.image(image, caption=doc4.metadata.get("productDisplayName"))
        with st.expander(expander_text):
            st.json(doc4.metadata)


#sidebar
with st.sidebar:

    gender = st.multiselect("gender", options=choices.gender.value,max_selections=1)
    if gender:
        st.session_state["gender"] = gender

    category = st.multiselect("category", options=choices.category.value)
    if category:
        st.session_state["category"] = category

    sub_category = st.multiselect("sub category", options = choices.sub_category.value)
    if sub_category :
        st.session_state["sub_category"] = sub_category

    article_type = st.multiselect("article", options = choices.article_type.value)
    if article_type :
        st.session_state["article_type"] = article_type

    usage = st.multiselect("usage", options = choices.usage.value)
    if article_type :
        st.session_state["usage"] = article_type

    base_color = st.multiselect("color", options=choices.base_color.value)
    if base_color:
        st.session_state["base_color"] = base_color

    season_choices = choices.get_seasons()
    season = st.multiselect("Season selects", options=season_choices, max_selections=1)
    if season:
        st.session_state["season"] = season

# Title of the app
st.header('A vector database recommendation engine', divider='blue')
text_search = st.text_input("Search",value="",placeholder="Looking for something in particular?")
if text_search:
    st.session_state["search"] = text_search
search = st.button("search")
if search:
    search_recommendations()
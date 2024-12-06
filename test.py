import streamlit as st
from streamlit_sortables import sort_items
import random

if "items" not in st.session_state:
    st.session_state.items = [
        {"header": "first container", "items": ["A", "B", "C"]},
        {"header": "second container", "items": ["D", "E", "F"]},
        {"header": "third container", "items": ["G", "H", "I"]},
    ]

if "need_rerun" not in st.session_state:
    st.session_state.need_rerun = -1


def add_new_item(sorted_items):
    sorted_items[0]["items"].append(str(random.randint(1, 1000)))
    return sorted_items


@st.fragment
def sort_items_and_rerun():
    st.session_state["items"] = sort_items(
        st.session_state["items"],
        multi_containers=True,
        direction="vertical",
        key=str(st.session_state["items"]),
    )
    if st.session_state.need_rerun > 0:
        st.session_state.need_rerun *= -1
        st.rerun()
    else:
        st.session_state.need_rerun *= -1


if st.button("Add New Item"):
    st.session_state["items"] = add_new_item(st.session_state["items"])
sort_items_and_rerun()

st.write(st.session_state["items"])

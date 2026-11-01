
import streamlit as st

from frontend.styles import render_brand


PAGES = {
    "Dashboard": {
        "key": "dashboard",
        "icon": ":material/dashboard:"
    },

    "Model Configuration": {
        "key": "configuration",
        "icon": ":material/settings:"
    },

    "Test Configuration": {
        "key": "test_configuration",
        "icon": ":material/science:"
    },

    "Custom Question Testing": {
        "key": "custom_testing",
        "icon": ":material/chat:"
    },

    "Evaluation Results": {
        "key": "results",
        "icon": ":material/analytics:"
    },

    "Version Comparison": {
        "key": "comparison",
        "icon": ":material/compare_arrows:"
    },

    "Reports": {
        "key": "reports",
        "icon": ":material/description:"
    },
}


def select_page(page):
    st.session_state["current_page"] = page


def show_navigation():

    with st.sidebar:

        render_brand()

        st.divider()

        st.caption("MAIN MENU")

        st.session_state.setdefault(
            "current_page",
            "Dashboard"
        )

        for page, details in PAGES.items():

            st.button(
                page,
                key=f"nav_{details['key']}",
                icon=details["icon"],
                type=(
                    "primary"
                    if st.session_state["current_page"] == page
                    else "secondary"
                ),
                use_container_width=True,
                on_click=select_page,
                args=(page,)
            )

        st.divider()

        st.markdown("**PLATFORM STATUS**")

        st.success("Frontend available")

        st.caption(
            "TRUST-AI · RESPONSIBLE AI PLATFORM · V1"
        )

    return st.session_state["current_page"]


def get_page_key(page_name=None):

    page_name = (
        page_name
        or st.session_state.get(
            "current_page",
            "Dashboard"
        )
    )

    return PAGES.get(
        page_name,
        PAGES["Dashboard"]
    )["key"]

import streamlit as st
from streamlit_option_menu import option_menu

import analyst
import guide


# sidebar
with st.sidebar:
    app = option_menu(
        menu_title="Smart-Export",
        options=["Analisis Ekspor", "Panduan Ekspor"],
        icons=["lightbulb", "person-walking"],
        # menu_icon="assets/smartExport.png",
        menu_icon="truck",
        default_index=0
    )
    
if app == "Analisis Ekspor":
    analyst.app()
if app == "Panduan Ekspor":
    guide.app()

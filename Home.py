# web development - Dashboard
import streamlit as st 


st.set_page_config(
    page_title="About",
    page_icon="🇺🇸",
    layout= "wide"    
)

st.write("# Welcome to NotFinancialAdvice! 👋")
st.image("./Streamlit/Resources/LandingPage.jpg")
st.markdown(
    """
    This is your one stop shop for all analysis as it relates to the Stock Markets. 
    Whether you are intersted in general information on the company, fundamental analysis, technical analysis 
    or perhaps you want to see what your asset looks like forecasted in the future, we have the tools you are
    looking for!
 
    
    **👈 Select a page from the sidebar** to see a variety of financial analysis!
    
    ### Feel Free to connect!
    - [Richie Garafola](https://www.linkedin.com/in/richie-garafola)

        
"""
)


tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Agenda", "Executive Summary", "High Level Architechtural Diagram", "NFT Token Gating: Proof of Concept", "Financial Analysis Dashboard", "Oracle Database", "Project Approach",  "Next Steps", "Results and Conclusions"])

with tab1:
    st.header("Agenda")
    st.image("./Streamlit/Resources/agenda.jpg")

with tab2:
    st.header("Executive Summary")
    st.image("./Streamlit/Resources/executive_summary.jpg")

with tab3:
    st.header("High Level Architechtural Diagram")
    st.image("./Streamlit/Resources/high_level_diagram.png")
    
with tab4:
    st.header("NFT Token Gating: Proof of Concept")
    st.image("./Streamlit/Resources/nft_token_gating.png")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.video("https://www.youtube.com/watch?v=jiKPlbJcd3Q&list=PLDNke-5WO5QfRG5FaB9-4Ly2WIRSOpuxJ&index=1")
    with col2:
        st.video("https://www.youtube.com/watch?v=3KPBPvwWlYA&list=PLDNke-5WO5QfRG5FaB9-4Ly2WIRSOpuxJ&index=2")
    with col3:
        st.video("https://www.youtube.com/watch?v=Z6vmJKkdzRo&list=PLDNke-5WO5QfRG5FaB9-4Ly2WIRSOpuxJ&index=3")
    with col4:
        st.video("https://www.youtube.com/watch?v=NP3PUB-6gyQ&list=PLDNke-5WO5QfRG5FaB9-4Ly2WIRSOpuxJ&index=4")
    st.markdown("""
    [NFA ERC1155 Demonstration](https://www.youtube.com/playlist?list=PLDNke-5WO5QfRG5FaB9-4Ly2WIRSOpuxJ""") 

with tab5:
    st.header("Financial Analysis Dashboard")
    st.image("./Streamlit/Resources/dashboardoverview.png")
    
with tab6:
    st.header("Oracle Database")
    st.image("./Streamlit/Resources/oracle_database.png")
    
with tab7:
    st.header("Project Approach")
    st.image("./Streamlit/Resources/project_approach.png")    
    
with tab8:
    st.header("Next Steps")
    st.image("./Streamlit/Resources/next_steps.png")    

with tab9:
    st.header("Results and Conclusions")
    st.image("./Streamlit/Resources/results.jpg")

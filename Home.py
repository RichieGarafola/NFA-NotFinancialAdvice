# web development - Dashboard
import streamlit as st 


st.set_page_config(
    page_title="About",
    page_icon="🇺🇸",
    layout= "wide"    
)

st.write("# Welcome to NotFinancialAdvice! 👋")
st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/LandingPage.jpg")
st.markdown(
    """
    This is your one stop shop for all analysis as it relates to the Stock Markets. 
    Whether you are intersted in general information on the company, fundamental analysis, technical analysis 
    or perhaps you want to see what your asset looks like forecasted in the future, we have the tools you are
    looking for!
 
    
    **👈 Select a page from the sidebar** to see a variety of financial analysis!
    
    ### Feel Free to connect!
    - [Richie Garafola](https://www.linkedin.com/in/richie-garafola)
    - [Jacob Edelbrock](https://www.linkedin.com/in/jacob-edelbrock-resume/)
    - [Mark Staten](https://www.linkedin.com/in/mark-staten-b9b3885/)
        
"""
)


tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Agenda", "Executive Summary", "High Level Architechtural Diagram", "NFT Token Gating: Proof of Concept", "Financial Analysis Dashboard", "Oracle Database", "Project Approach",  "Next Steps", "Results and Conclusions"])

with tab1:
    st.header("Agenda")
    st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/agenda.jpg")

with tab2:
    st.header("Executive Summary")
    st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/executive_summary.jpg")

with tab3:
    st.header("High Level Architechtural Diagram")
    st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/high_level_diagram.png")
    
with tab4:
    st.header("NFT Token Gating: Proof of Concept")
    st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/nft_token_gating.png")
    st.markdown("""
    [Part 1 NFA ERC 1155 Contract and Mint](https://www.youtube.com/watch?v=jiKPlbJcd3Q)
    
    [Part 2 NFA ERC1155 Etherscan Mint Transaction](https://www.youtube.com/watch?v=3KPBPvwWlYA)
    
    [Part 3 NFA ERC1155 Safe Transfer NFT](https://www.youtube.com/watch?v=Z6vmJKkdzRo)
    
    [Part 4 NFA ERC 1155 Etherscan NFT Transfer Details](https://www.youtube.com/watch?v=NP3PUB-6gyQ)""")

with tab5:
    st.header("Financial Analysis Dashboard")
    st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/dashboardoverview.png")
    
with tab6:
    st.header("Oracle Database")
    st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/oracle_database.png")
    
with tab7:
    st.header("Project Approach")
    st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/project_approach.png")    
    
with tab8:
    st.header("Next Steps")
    st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/next_steps.png")    

with tab9:
    st.header("Results and Conclusions")
    st.image("Desktop/Github/Project3/Project3/Richie/Streamlit/Resources/results.jpg")



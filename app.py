import streamlit as st
from crew import crewwork

# Streamlit UI
st.title("Multi-Agent System for AI Use Case Generation")

# Input for company name
company_name = st.text_input("Enter the Company's Name", value="")

# Button to execute the crew
if st.button("Generate Report") and company_name:
    # Execute the crew process
    result = crewwork.kickoff(inputs={"Company_name": company_name})
    
    # Convert result to markdown format
    with open("resource_asset_collection.md", "r") as md_file:
        resource_markdown_content = md_file.read()
    st.markdown(
    "<h1 style='color: #e74c3c; font-size: 24px;'>Use Cases with their Resources:</h1>",
    unsafe_allow_html=True
    )
    # Display the markdown content on the frontend
    st.markdown(resource_markdown_content)
    with open("solution_recommendation.md", "r") as file:
        solution_markdown_content = file.read()
    st.markdown(
    "<h1 style='color: #e74c3c; font-size: 24px;'>GenAI based Solutions:</h1>",
    unsafe_allow_html=True
    )
    st.markdown(solution_markdown_content)
else:
    st.write("Please enter a company name to generate the report.")
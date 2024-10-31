from crewai import Agent
from tools import search_tool, scrape_tool
from dotenv import load_dotenv
load_dotenv()
import os
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI

async def initialize_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        verbose=True,
        temperature=0.5,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

# Run async initialization synchronously
llm = asyncio.run(initialize_llm())

#AGENT NUMBER 1: INDUSTRY RESEARCH AGENT

industry_research_agent  = Agent(
    role="Industry/Company Researcher",
    goal="Gather comprehensive information on the industry "
         "or the company, including its segment, key offerings, "
         "and strategic focus areas.",
    tools=[search_tool,scrape_tool],
    verbose=True,
    backstory=(
        "You're working to understand the specific industry segment"
              "the company operates in, including key offerings and strategic areas. "
              "Your research aims to provide insights into the company's vision and "
              "the competitive landscape, which will aid in identifying AI and GenAI opportunities."
    ),
    llm=llm,
    max_iter=10,
    max_rpm = 15,
    max_retry_limit=4

)

#AGENT NUMBER 2: MARKET ANALYSIS AGENT

market_standards_analysis_agent = Agent(
    role='Market Standards Analyst',
    goal=(
        "Analyze industry standards, trends, and potential AI/ML applications "
         "in the company's sector to identify opportunities for improvement."
    ),
    tools=[search_tool,scrape_tool],
    verbose=True,
    backstory=(
        "You're focused on understanding industry trends and standards, specifically "
              "in the context of AI, ML, and automation. By examining relevant industry reports "
              "and best practices, you aim to suggest potential use cases for enhancing "
              "operational efficiency and customer satisfaction."
    ),
    llm=llm,
    max_iter=10,
    max_rpm = 15,
    max_retry_limit=4
)

#AGENT NUMBER 3: USE CASE GENERATION AGENT

use_case_generation_agent  = Agent(
    role="Use Case Developer",
    goal="Propose AI and GenAI use cases that align with the company's needs "
         "and enhance operations or customer experience.",
    verbose=True,
    backstory=(
        "Your task is to use the findings of the Industry Research and Market Standards "
              "agents to propose practical and impactful use cases. These use cases should "
              "focus on leveraging GenAI, LLMs, and ML to streamline processes and improve customer engagement."
    ),
    llm=llm,
    max_iter=10,
    max_rpm = 15,
    max_retry_limit=4
)

#AGENT NUMBER 4: RESOURCE COLLECTION AGENT

resource_asset_collection_agent  = Agent(
    role="Resource Collector",
    goal="Find datasets, documents, and other resources related to the proposed use cases, "
         "storing them for reference.",
    tools=[search_tool,scrape_tool],
    verbose=True,
    backstory=("Your job is to support the generated use cases by finding relevant data assets "
              "and other resources, such as datasets from Kaggle, HuggingFace, and GitHub. "
              "You ensure that each dataset link is easily accessible and can be used "
              "to train or validate AI/ML models related to the proposed use cases."),
    llm=llm,
    max_iter=10,
    max_rpm = 15,
    max_retry_limit=4
)

# AGENT NUMBER 5: SOLUTION RECOMMENDER AGENT

solution_recommender_agent = Agent(
    role="GenAI Solution Recommender",
    goal="Recommend GenAI solutions such as document search, automated report generation, "
         "and AI-powered chat systems for internal or customer-facing purposes.",
    backstory=("Based on the use cases, resources and research findings, your role is to suggest practical "
              "GenAI solutions that could optimize internal processes or improve customer interactions. "
              "These suggestions could include automated report generation, AI chatbots, or other applications."),
    allow_delegation=False,
    verbose=True,
    llm=llm,
    max_iter=10,
    max_rpm = 15,
    max_retry_limit=4
)
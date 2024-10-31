from crewai import Task
from tools import scrape_tool,search_tool
from agents import industry_research_agent,market_standards_analysis_agent, use_case_generation_agent,resource_asset_collection_agent, solution_recommender_agent

# TASK 1: INDUSTRY RESEARCH

industry_research = Task(
    description=(
        "1. Use web browsing tools to gather comprehensive data on "
            "the industry or company name and identify the specific segment.\n"
        "2. Collect information on key offerings and strategic focus "
            "areas, such as operations, supply chain, and customer experience.\n"
        "3. Gather insights into the company’s vision, competitive landscape, "
            "and product details.\n"
        "4. Organize the data in a structured format that will be used for "
            "further analysis and use case generation.\n"
        "5. The name of the industry or Company is: {Company_name}"
    ),
    expected_output="A detailed report in markdown format covering "
        "industry insights, company segment, key offerings, and focus areas.",
    agent=industry_research_agent,
    output_file="industry_research.md"
)

# TASK 2: MARKET ANALYSIS

market_analysis = Task(
    description=(
        "1. Review industry trends and standards relevant to the company’s sector, "
            "with a focus on AI, ML, and automation.\n"
        "2. Analyze reports and articles to identify standard practices, advancements, "
            "and competitive benchmarks.\n"
        "3. Summarize findings on AI/ML applications within the industry, particularly "
            "for operational efficiency and customer satisfaction.\n"
        "4. Highlight any key areas where AI/ML can offer a competitive advantage.\n"
        "5. The name of the industry or Company is: {Company_name}"
    ),
    expected_output="A concise analysis in markdown format outlining "
        "industry standards, trends, and AI/ML applications in the company's sector.",
    agent=market_standards_analysis_agent,
    output_file="market_analysis.md"
)

# TASK 3: USE CASE GENERATION 

use_case_generation = Task(
    description=(
        "1. Using insights from industry research, propose relevant AI and GenAI "
            "use cases for the company.\n"
        "2. Focus on enhancing operational efficiency, improving customer experience, "
            "and optimizing processes.\n"
        "3. Align use cases with industry trends and the company’s goals.\n"
        "4. Provide a brief description for each use case, specifying potential impact.\n"
        "5. The name of the industry or Company is: {Company_name}"
    ),
    expected_output="A list of actionable AI/GenAI use cases in markdown format, "
        "each with a brief description and potential impact on the company.",
    agent=use_case_generation_agent,
    context=[market_analysis,industry_research],
    output_file="use_case_generation.md"
)


# TASK 4: RESOURCE ASSET COLLECTION

resource_asset_collection = Task(
    description=(
        "1. Search for datasets, models, and other resources relevant to the "
            "proposed use cases on platforms like Kaggle, HuggingFace, and GitHub.\n"
        "2. Ensure resources are aligned with each use case, such as datasets for "
            "model training or reference documents for further understanding.\n"
        "3. Document each resource with clickable links for easy access.\n"
    ),
    expected_output="A markdown file with clickable links to relevant datasets, "
        "models, and resources for each use case.",
    agent=resource_asset_collection_agent,
    context=[use_case_generation],
    output_file="resource_asset_collection.md"
)

# TASK 5: SOLUTION RECOMMENDATION

solution_recommendation = Task(
    description=(
        "1. Based on the generated use cases, suggest specific GenAI solutions "
            "such as document search, automated report generation, or AI chat systems.\n"
        "2. Provide examples where these solutions can improve internal processes "
            "or enhance customer engagement.\n"
        "3. Explain the potential impact of each recommendation and its alignment "
            "with the company’s goals.\n"
    ),
    expected_output="A list of GenAI solution recommendations in markdown format, "
        "with a brief description of each solution’s impact and relevance.",
    agent=solution_recommender_agent,
    context=[industry_research,market_analysis,use_case_generation],
    output_file="solution_recommendation.md"
)
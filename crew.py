from crewai import Crew,Process
from tasks import industry_research,market_analysis,use_case_generation,resource_asset_collection
from agents import industry_research_agent,market_standards_analysis_agent, use_case_generation_agent,resource_asset_collection_agent

## Forming the tech focused crew with some enhanced configuration
crewwork=Crew(
    agents=[industry_research_agent,market_standards_analysis_agent,use_case_generation_agent,resource_asset_collection_agent],
    tasks=[industry_research,market_analysis,use_case_generation,resource_asset_collection],
    process=Process.sequential,

)

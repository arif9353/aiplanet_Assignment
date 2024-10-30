from crewai import Crew,Process
from tasks import industry_research, solution_recommendation,market_analysis,use_case_generation,resource_asset_collection
from agents import industry_research_agent,solution_recommender_agent,market_standards_analysis_agent, use_case_generation_agent,resource_asset_collection_agent

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[industry_research_agent,market_standards_analysis_agent,use_case_generation_agent,resource_asset_collection_agent,solution_recommender_agent],
    tasks=[industry_research,market_analysis,use_case_generation,resource_asset_collection,solution_recommendation],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'Company_name':'Delloite'})
print(result)
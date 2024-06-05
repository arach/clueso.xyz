from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.github_trending_tool.github_trending_tool import GithubTrendingTool
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool
from tools.perplexity_tool.perplexity_tool import PerplexityTool
from tools.supabase_tool.supabase_tool import SupabaseTool


web_search_tool = WebsiteSearchTool()
serper_dev_tool = SerperDevTool()
import agentops
import dotenv
import os
dotenv.load_dotenv()
agentops.init(os.getenv("AGENTOPS_API_KEY"))


@CrewBase
class AssistantCrew():
    """AssistantCrew crew"""
    agents_config = 'config/assistant-agents.yaml'
    tasks_config = 'config/assistant-tasks.yaml'

    @agent
    def assistant(self) -> Agent:
            return Agent(
                    config=self.agents_config['assistant'],
                    verbose=True
            )
    @task
    def save_research(self) -> Task:
          return Task(
            config=self.tasks_config['save_research_task'],
            agent=self.assistant(),
            tools=[SupabaseTool.save_report],
          )

    @task
    def save_outreach(self) -> Task:
          return Task(
            config=self.tasks_config['save_outreach_task'],
            agent=self.assistant(),
            tools=[SupabaseTool.save_outreach],
          )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Assistant crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
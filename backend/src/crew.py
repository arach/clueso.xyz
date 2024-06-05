from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.github_trending_tool.github_trending_tool import GithubTrendingTool
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool
from tools.perplexity_tool.perplexity_tool import PerplexityTool

web_search_tool = WebsiteSearchTool()
serper_dev_tool = SerperDevTool()

@CrewBase
class GithubResearchCrew():
    """GithubResearchCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def researcher(self) -> Agent:
            return Agent(
                    config=self.agents_config['researcher'],
                    tools=[GithubTrendingTool(), serper_dev_tool, PerplexityTool()],
                    verbose=True
            )

    @agent
    def partner(self) -> Agent:
            return Agent(
                    config=self.agents_config['partner'],
                    verbose=True
            )


    @task
    def research_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_report_task'],
            agent=self.researcher(),
            output_file='research_report.md'
        )

    @task
    def reach_out_task(self) -> Task:
        return Task(
            config=self.tasks_config['reach_out_task'],
            agent=self.partner(),
            output_file='reach_out.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the GithubTrending crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

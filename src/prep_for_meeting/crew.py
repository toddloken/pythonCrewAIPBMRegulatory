from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class PrepForMeetingCrew:
    """CrewAI Meeting Preparation Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def lead_researcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["lead_researcher_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def product_specialist_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["product_specialist_agent"],
            tools=[SerperDevTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def regulatory_compliance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["regulatory_compliance_agent"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def legal_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["legal_agent"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def briefing_coordinator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["briefing_coordinator_agent"],
            tools=[],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.lead_researcher_agent(),
        )

    @task
    def product_alignment_task(self) -> Task:
        return Task(
            config=self.tasks_config["product_alignment_task"],
            agent=self.product_specialist_agent(),
        )

    @task
    def regulatory_and_legal_task(self) -> Task:
        return Task(
            config=self.tasks_config["regulatory_and_legal_task"],
            agent=self.regulatory_compliance_agent(),
        )

    @task
    def meeting_preparation_task(self) -> Task:
        return Task(
            config=self.tasks_config["meeting_preparation_task"],
            agent=self.briefing_coordinator_agent(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Meeting Preparation Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

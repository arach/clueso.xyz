import asyncio
from typing import Optional, Any, Type
from pydantic.v1 import BaseModel, Field
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
from langchain.agents import tool
from pydantic.v1 import BaseModel, Field
from crewai_tools import BaseTool 

class GithubTrendingToolSchema(BaseModel):
    language: str = Field(description="python,javascript,java")
    since: str = Field(description="today,week,month,year")


class GithubTrendingTool(BaseTool):
    name: str = "Get Github Trending Repositories"
    description: str = "Load the top trending repositories from Github"
    args_schema: Type[BaseModel] = GithubTrendingToolSchema
    language: Optional[str] = None
    since: Optional[str] = None 

    def __init__(self, language: Optional[str] = None, since: Optional[str] = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.language = language
        self.since = since

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        print("args", args, "kwargs", kwargs)
        print("self.language", self.language, "self.since", self.since)
        with sync_playwright() as p:
            # Launch the browser
            browser = p.chromium.launch()
            page = browser.new_page()
            
            gh_trending_url = 'https://github.com/trending'
            if self.language:
                gh_trending_url = f'{gh_trending_url}/{self.language}'
            if self.since:
                gh_trending_url = f'{gh_trending_url}?since={self.since}'
            page.goto(gh_trending_url)

            repos = page.locator("article.Box-row").all()
            trending_repos = []

            for repo in repos:
                title = repo.locator("h2").locator("a").inner_text()
                try:
                    description = repo.locator("p.col-9")
                    if description.count():
                        description = description.inner_text()
                    else:
                        description = "Description not available"
                except Exception as e:
                    description = "Description not available"
                    print(f"Error retrieving description: {e}")
                link = repo.locator("h2").locator("a").get_attribute('href')
                stargazers = repo.locator(".f6").locator("a").nth(0).inner_text()
                forks = repo.locator(".f6").locator("a").nth(1).inner_text()
                # Join "github.com" and link to form URL
                url = "https://github.com" + link
                trending_repo = {
                    'title': title,
                    'link': url,
                    'description': description,
                    'stargazers': stargazers,
                    'forks': forks
                }
                trending_repos.append(trending_repo)
            # Close the browser
            browser.close()
            return trending_repos   

  
def getTrendingRepos(language=None, since=None) -> list:
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch()
        page = browser.new_page()
        
        gh_trending_url = 'https://github.com/trending'
        if language:
            gh_trending_url = f'{gh_trending_url}/{language}'
        if since:
            gh_trending_url = f'{gh_trending_url}?since={since}'
        page.goto(gh_trending_url)

        repos = page.locator("article.Box-row").all()
        trending_repos = []

        for repo in repos:
            title = repo.locator("h2").locator("a").inner_text()
            link = repo.locator("h2").locator("a").get_attribute('href')
            stargazers = repo.locator(".f6").locator("a").nth(0).inner_text()
            forks = repo.locator(".f6").locator("a").nth(1).inner_text()
            #in python join "github.com" and link to form url
            url = "https://github.com" + link
            trending_repo = {
                'title': title,
                'link': url,
                'stargazers': stargazers,
                'forks': forks
            }
            trending_repos.append(trending_repo)

        page.screenshot(path='screenshot.png')
        print('Screenshot captured and saved as screenshot.png')
        # Close the browser
        browser.close()
        return trending_repos

from openai import OpenAI
import os
from typing import Optional, Any, Type
from dotenv import load_dotenv
from crewai_tools import BaseTool
from pydantic.v1 import BaseModel, Field

load_dotenv()  # Load environment variables from a .env file
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")


class PerplexityToolSchema(BaseModel):
    repo: str = Field(description="the full URL of the github repository")
    context: str = Field(description="helpful context for perplexity to do a good research on the repo or the author.")


class PerplexityTool(BaseTool):
    name: str = "Perplexity Tool"
    description: str = (
        "Using the Perplexity API allows us to get great results from our conversation models and we can use it to get a detailed report on a github repository."
    )
    args_schema: Type[BaseModel] = PerplexityToolSchema

    def _run(self, repo: str, context: str) -> str:
        return getRepoResearchReport(repo, context)
    

def getRepoResearchReport(repo, context):
    messages = [
    {
        "role": "system",
        "content": (
            "You are an artificial intelligence assistant and you need to "
            "engage in a helpful, detailed, polite conversation with a user."
        ),
    },
    {
        "role": "user",
        "content": (
            f"I need a good research repo on {repo}. {context}. It's a trending repository and you need to find out what it is about. I'm going to need you to provide me with the following information about the repository: \nexplain what the repository is about, \nwhat programming language it uses, \nhow many stars it has, \nhow many forks it has, \nwhat the top competitors to the project is. If there's a link to a company website, please include that as well.\nPlease provide me with a detailed, structured report. If I am looking to contact the author of the repo, please include contact information and best way to contact them.\n"
        ),
    },
]
    print("Calling Perplexity API")
    response = client.chat.completions.create(
        model="llama-3-sonar-large-32k-online",
        messages=messages,
    )
    print("Done!")
    content = response.choices[0].message.content.replace('\\n', '\n').replace('\\t', '\t')
    return content

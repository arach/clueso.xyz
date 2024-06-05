from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")


def getRepoResearchReport(repo):
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
            f"You are an analyst at a Venture Capital Firm. We have given you the task to research a github repository. {repo} It's a trending repository and you need to find out what it is about. I'm going to need you to provide me with the following information about the repository: \nexplain what the repository is about, \nwhat programming language it uses, \nhow many stars it has, \nhow many forks it has, \nwhat the top competitors to the project is. If there's a link to a company website, please include that as well.\nPlease provide me with a detailed, structured report."
        ),
    },
]
    print("Fetching trending repositories...")
    response = client.chat.completions.create(
        model="llama-3-sonar-large-32k-online",
        messages=messages,
    )
    print(response)
    return response

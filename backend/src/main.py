#!/usr/bin/env python
import argparse
from perplexity import getRepoResearchReport
import asyncio
import sys
from crew import GithubResearchCrew

async def main(language=None, since=None):
    repos = await getTrendingRepos(language, since)
    for repo in repos:
        print("proceed with research for repo: ", repo['title'])
        getRepoResearchReport(repo)


def run():
    inputs = {
        'research': "Let's find the coolest new repos on Github"
    }
    print("Let's find the coolest new repos on Github")

    GithubResearchCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
#     parser = argparse.ArgumentParser(description="Get top trending repos from github")
#     parser.add_argument("--language", action="store_true", help="specify which language (default: None)")
#     parser.add_argument("--since", action="store_true", help="specify within which time period (default: None)")
#     args = parser.parse_args()

    
    # asyncio.run(main(args.language, args.since))
    
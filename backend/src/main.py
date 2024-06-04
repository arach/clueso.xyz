import argparse
from tools.github_search_tool.github_search_tool import getTrendingRepos
from perplexity import getRepoResearchReport
import asyncio

async def main(language=None, since=None):
    repos = await getTrendingRepos(language, since)
    for repo in repos:
        print("proceed with research for repo: ", repo['title'])
        getRepoResearchReport(repo)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get top trending repos from github")
    parser.add_argument("--language", action="store_true", help="specify which language (default: None)")
    parser.add_argument("--since", action="store_true", help="specify within which time period (default: None)")
    args = parser.parse_args()


    asyncio.run(main(args.language, args.since))
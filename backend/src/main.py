#!/usr/bin/env python
import argparse
import asyncio
import sys
from crew import GithubResearchCrew


def main():
    inputs = {
        'research': "Let's find the coolest new repos on Github"
    }
    print("Let's find the coolest new repos on Github")
    GithubResearchCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    main()
    
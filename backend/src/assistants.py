#!/usr/bin/env python
import argparse
import asyncio
import sys
from assistant_crew import AssistantCrew


def run():
    AssistantCrew().crew().kickoff()

if __name__ == "__main__":
    run()
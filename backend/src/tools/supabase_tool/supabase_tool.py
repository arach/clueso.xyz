from openai import OpenAI
import os
from typing import Optional, Any, Type
from dotenv import load_dotenv
from crewai_tools import BaseTool
from pydantic.v1 import BaseModel, Field
from supabase import create_client, Client
from datetime import datetime
from langchain.agents import tool

load_dotenv()  # Load environment variables from a .env file

class SupabaseTool():
    @tool("save_report")
    def save_report(content: str) -> str:
        """
            Useful to save a report to the database.
            Args:
                content (str): the content to be stored in the database
            Returns:
                str: the id of the report
        """
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        client: Client = create_client(url, key)
        day = datetime.now().strftime("%Y-%m-%d")

        report_path = os.path.join(os.path.dirname(__file__), '../../../research_report.md')
        with open(report_path, 'r') as file:
            report_content = file.read()
        
        data, count = client.table('research_reports').insert({
            "name": f"research_report_{day}",
            "content": report_content
        }).execute()
        return data
    
    @tool
    def save_outreach(content: str) -> str:
        """
            Useful to save outreach to the database.
            Args:
                content (str): the content to be stored in the database
            Returns:
                str: the id of the report
        """
        
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        client: Client = create_client(url, key)
        
        filepath = os.path.join(os.path.dirname(__file__), '../../../outreach.md')
        with open(filepath, 'r') as file:
            outreach_content = file.read()
        
        day = datetime.now().strftime("%Y-%m-%d")
        data, count = client.table('outreach').insert({
            "name": f"outreach_{day}",
            "content": outreach_content
        }).execute()
        return data

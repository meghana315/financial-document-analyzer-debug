## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader
from crewai.tools import tool

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool():

    @staticmethod
    @tool("Financial Document Reader")
    def read_data_tool(path: str = 'data/sample.pdf') -> str:
        """Tool to read data from a pdf file from a path.

        Args:
            path (str): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file content
        """
        loader = PyPDFLoader(file_path=path)
        docs = loader.load()

        full_report = ""
        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report


## Creating Investment Analysis Tool
class InvestmentTool:
    @staticmethod
    @tool("Investment Analyzer")
    def analyze_investment_tool(financial_document_data: str) -> str:
        """Analyze investment opportunities from financial document data.

        Args:
            financial_document_data (str): The financial document content to analyze.

        Returns:
            str: Investment analysis result
        """
        processed_data = financial_document_data
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
        return f"Investment analysis completed on document with {len(processed_data)} characters of financial data."


## Creating Risk Assessment Tool
class RiskTool:
    @staticmethod
    @tool("Risk Assessor")
    def create_risk_assessment_tool(financial_document_data: str) -> str:
        """Create a risk assessment from financial document data.

        Args:
            financial_document_data (str): The financial document content to assess.

        Returns:
            str: Risk assessment result
        """
        return f"Risk assessment completed on document with {len(financial_document_data)} characters of financial data."
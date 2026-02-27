## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from tools import search_tool, FinancialDocumentTool

### Loading LLM (Google Gemini - Free Tier)
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze the financial document thoroughly and answer the user's query: {query} with accurate, data-driven insights.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned financial analyst with 20+ years of experience analyzing corporate financial reports, "
        "earnings statements, balance sheets, and investment documents. You are known for your accuracy, attention to detail, "
        "and ability to extract meaningful insights from complex financial data. You strictly base your analysis on the "
        "actual data provided in documents and never fabricate information."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=2,
    allow_delegation=False
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify that the uploaded document is a legitimate financial document and confirm its type and key attributes.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a meticulous document verification specialist with deep expertise in financial compliance and document analysis. "
        "You carefully examine documents to confirm they are genuine financial reports such as earnings updates, balance sheets, "
        "income statements, or annual reports. You provide accurate assessments of document authenticity and type."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=2,
    allow_delegation=False
)

investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide sound, evidence-based investment insights derived strictly from the financial document data for the query: {query}",
    verbose=True,
    backstory=(
        "You are a certified investment advisor with 15+ years of experience in equity research and portfolio management. "
        "You provide clear, factual, and regulatory-compliant investment insights based solely on documented financial data. "
        "You always disclose that your analysis is for informational purposes only and not financial advice."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=2,
    allow_delegation=False
)

risk_assessor = Agent(
    role="Risk Assessment Analyst",
    goal="Identify and assess real financial risks present in the document relevant to the query: {query}",
    verbose=True,
    backstory=(
        "You are a risk management expert specializing in corporate financial risk assessment. "
        "You analyze financial statements to identify genuine risk factors such as liquidity risk, market risk, "
        "operational risk, and credit risk. Your assessments are grounded in actual data and follow industry best practices."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=2,
    allow_delegation=False
)
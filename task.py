## Importing libraries and files
from crewai import Task
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import search_tool, FinancialDocumentTool

## Task 1: Verify the document
verification = Task(
    description=(
        "Read the financial document at the given file path and verify it is a legitimate financial document. "
        "Identify the document type (e.g., earnings report, balance sheet, annual report), the company name, "
        "and the reporting period. Provide a brief summary of what the document contains.\n"
        "User query for context: {query}\n"
        "File path: {file_path}"
    ),
    expected_output=(
        "A clear verification report including:\n"
        "1. Document type and legitimacy confirmation\n"
        "2. Company name and reporting period\n"
        "3. Brief summary of document contents (3-5 sentences)\n"
        "4. Key sections identified in the document"
    ),
    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False
)

## Task 2: Core financial analysis
analyze_financial_document = Task(
    description=(
        "Thoroughly analyze the financial document at the file path provided and answer the user's query.\n"
        "User query: {query}\n"
        "File path: {file_path}\n\n"
        "Focus on:\n"
        "- Key financial metrics (revenue, profit, margins, cash flow)\n"
        "- Year-over-year and quarter-over-quarter trends\n"
        "- Business segment performance\n"
        "- Management commentary and outlook\n"
        "Base your analysis strictly on the data in the document."
    ),
    expected_output=(
        "A comprehensive financial analysis report including:\n"
        "1. Executive summary answering the user's query\n"
        "2. Key financial highlights with actual figures from the document\n"
        "3. Revenue and profitability analysis with trends\n"
        "4. Cash flow and balance sheet observations\n"
        "5. Business segment breakdown\n"
        "6. Notable risks and opportunities mentioned in the document"
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
    context=[verification]
)

## Task 3: Investment analysis
investment_analysis = Task(
    description=(
        "Based on the financial document analysis, provide objective investment insights.\n"
        "User query: {query}\n"
        "File path: {file_path}\n\n"
        "Focus on:\n"
        "- Key financial ratios and what they indicate\n"
        "- Growth trends and their investment implications\n"
        "- Competitive positioning based on reported data\n"
        "- Management's stated strategic priorities\n"
        "Always note that this is for informational purposes only and not financial advice."
    ),
    expected_output=(
        "An objective investment insights report including:\n"
        "1. Key financial ratios derived from the document\n"
        "2. Growth trajectory analysis based on actual reported figures\n"
        "3. Strengths and weaknesses identified from financial data\n"
        "4. Strategic outlook based on management commentary\n"
        "5. Important disclaimer that this is informational only"
    ),
    agent=investment_advisor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
    context=[analyze_financial_document]
)

## Task 4: Risk assessment
risk_assessment = Task(
    description=(
        "Identify and assess the real financial risks present in this document.\n"
        "User query: {query}\n"
        "File path: {file_path}\n\n"
        "Focus on:\n"
        "- Risks explicitly mentioned by management\n"
        "- Risks evident from financial data (e.g., declining margins, high debt)\n"
        "- Macroeconomic risks mentioned in the document\n"
        "- Operational risks highlighted in the report"
    ),
    expected_output=(
        "A structured risk assessment report including:\n"
        "1. Top financial risks identified from the document with supporting data\n"
        "2. Operational risks mentioned by management\n"
        "3. Market and macroeconomic risks\n"
        "4. Risk severity assessment (High/Medium/Low) with justification\n"
        "5. Risk mitigation strategies mentioned by the company"
    ),
    agent=risk_assessor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
    context=[analyze_financial_document]
)
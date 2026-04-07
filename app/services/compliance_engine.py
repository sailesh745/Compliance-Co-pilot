from app.services.rag_pipeline import get_rag_chain

def analyze_trade(trade_data: dict):
    query = f"""
    Analyze the following trade for compliance violations:

    Trade Details:
    {trade_data}

    Check against regulatory rules and internal policies.
    Provide:
    - Compliance status (Compliant / Violation)
    - Reason
    - Risk level
    - Suggested action
    """

    rag = get_rag_chain()
    result = rag(query)

    return {
        "analysis": result["result"],
        "sources": [doc.page_content for doc in result["source_documents"]]
    }

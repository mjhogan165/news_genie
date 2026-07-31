from typing import TypedDict


class NewsGenieState(TypedDict):
    """
    Defines the information that moves through the LangGraph workflow.
    """

    query: str
    query_type: str
    category: str
    response: str
    error: str

from src.state import NewsGenieState


def router_node(state: NewsGenieState) -> NewsGenieState:
    """
    Determines what type of request the user made.
    """

    query = state["query"].lower()
    if "news" in query:
        state["query_type"] = "news"
    else:
        state["query_type"] = "general"

    return state

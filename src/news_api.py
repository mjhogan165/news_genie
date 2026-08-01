import requests

from src.state import NewsGenieState
from src.config import NEWS_API_KEY


# Helper function to fetch news articles from the News API.
def fetch_news(category: str) -> list:
    """
    Fetches top US headlines for a selected news category.
    """

    url = "https://newsapi.org/v2/top-headlines"

    parameters = {
        "country": "us",
        "category": category,
        "apiKey": NEWS_API_KEY,
    }
    # Returns an HTTP response object.
    response = requests.get(url, params=parameters, timeout=10)
    # extract the JSON data from the response object.
    news_data = response.json()
    # hiding the messy API response and returning only the list of articles.
    return news_data["articles"]


def news_node(state: NewsGenieState) -> NewsGenieState:
    """
    Retrieves news articles and stores them in the workflow state.
    """

    category = state["category"]

    try:
        articles = fetch_news(category)

        state["response"] = str(articles)
        state["error"] = ""

    except Exception as error:
        state["response"] = ""
        state["error"] = f"News request failed: {error}"

    return state

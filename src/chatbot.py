from langchain_openai import ChatOpenAI
from src.state import NewsGenieState

# Create the language model once when this module loads.
chat_model = ChatOpenAI(
    model="gpt-4o-mini",
)


def chatbot_node(state: NewsGenieState) -> NewsGenieState:
    """
    Answers a general user question with the OpenAI chat model.
    """

    user_query = state["query"]

    try:
        model_response = chat_model.invoke(user_query)

        # ChatOpenAI returns a message object.
        # The readable answer is stored in its content attribute.
        state["response"] = str(model_response.content)
        state["error"] = ""

    except Exception as error:
        state["response"] = ""
        state["error"] = f"Chatbot request failed: {error}"

    return state

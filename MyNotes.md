## State Fields

**`query`**
The user's original message.
Example: "Show me recent sports news"

**`query_type`**
The route selected by the router.
Example: "news"
Possible values: news, search, general

**`category`**
The news category, when one exists.
Example: "sports"
For a general question, this may remain empty.

**`response`**
The final text that will be shown to the user.
Example: "Here are the latest sports headlines..."

**`error`**
Stores a useful error message when something fails.
Example: "The news service is currently unavailable."
Keeping errors in the state lets the graph decide what fallback to use instead of immediately crashing.

## Every node in LangGraph is going to follow the same pattern:

````python
def some_node(state: NewsGenieState) -> NewsGenieState:
    # Read from state

    # Do some work

    # Update state

    return state```
````

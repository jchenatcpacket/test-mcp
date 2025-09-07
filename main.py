from mcp import FastMCP

app = FastMCP('my_todos')

@app.tool()
async def get_id(id: str = "") -> str:
    """
    Get todos from JSONPlaceholder API

    Args:
        id: Optional todo item ID. If not provided, returns all todos.

    Returns:
        JSON string with todo details
    """
    return f"your id is {id}, thank you"

if __name__ == '__main__':
    app.run(transport='stdio')
 
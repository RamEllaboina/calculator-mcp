import os
from mcp.server.fastmcp import FastMCP

port = int(os.environ.get("PORT", 8001))

mcp = FastMCP(
    "Calculator",
    host="0.0.0.0",
    port=port
)

last_sum = None


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and store the latest result."""
    global last_sum

    last_sum = a + b
    return last_sum


@mcp.tool()
def get_last_sum() -> float:
    """Get the most recent sum."""
    if last_sum is None:
        return 0

    return last_sum


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
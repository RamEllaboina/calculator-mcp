from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Calculator",
    host="127.0.0.1",
    port=8001
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
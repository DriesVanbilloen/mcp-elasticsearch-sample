from mcp.server.fastmcp import FastMCP
import json

# Create server
mcp = FastMCP("Components server")

@mcp.tool()
def get_components(name: str) -> list:
    """Provides a list of available components in the database"""
    print("Searching for components with name {}".format(name))

    # unfiltered_data = json.dumps(data)
    # filtered_data = [d for d in unfiltered_data if d["componentName"] == name]
    # print(json.dumps(filtered_data))

    return [{"componentName": "title", "sling:resourceType": "wknd/components/title"},
            {"componentName": "text", "sling:resourceType": "wknd/components/text"}]

if __name__ == "__main__":
    mcp.run(transport="sse")

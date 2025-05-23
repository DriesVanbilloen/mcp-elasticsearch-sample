import asyncio

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, ModelSettings
from agents.mcp import MCPServerSse, MCPServer

# Initialise the Google flash api
googleApiKey = ""
googleClient = deepseek_client = AsyncOpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=googleApiKey)

async def run(mcp_server: MCPServer):
    general_agent = Agent(
        name="XPath generator",
        instructions="You only response for questions related to generating reports and will return a AEM JCR xpath query as response.",
        mcp_servers=[mcp_server],
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=googleClient,
        ),
        model_settings=ModelSettings(tool_choice="required"),
    )

    result = await Runner.run(starting_agent=general_agent,
                        input="Generate a report that will give me the pages where all title components are used.")

    print(result.final_output)

async def main():
    print("Hello from mcp-agents!")
    async with MCPServerSse(
            name="Elastic search database",
            params={
                "url": "http://localhost:8000/sse",
            },
    ) as server:
        await run(server)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        print("done")
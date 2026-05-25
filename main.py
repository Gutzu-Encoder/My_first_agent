import asyncio
import os
from openai import OpenAI
from dotenv import load_dotenv
from orchestrator import orchestrator

load_dotenv()

async def main():
    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
    )
    result = await orchestrator(client, "latest road accident in Thailand")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
    

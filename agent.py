import asyncio
from tool import execute_tool
import json

tools = [{
    "type": "function",
    "function": {
        "name": "web_search",
        "description": "Search the web",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            },
            "required": ["query"]
        }
    }
}]

async def run_agent(client, task):
    messages = [{"role": "user", "content": task}]

    while True:
        response = await asyncio.to_thread(
            client.chat.completions.create,
            model="deepseek-v4-flash",
            messages=messages,
            tools=tools
        )

        msg = response.choices[0].message

        if not msg.tool_calls:
            return msg.content

        messages.append(msg)
        for tool_call in msg.tool_calls:
            result = execute_tool(tool_call.function.name, json.loads(tool_call.function.arguments))
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

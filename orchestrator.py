import asyncio
from agent import run_agent
async def orchestrator(client, task):
    results = await asyncio.gather(
        run_agent(client, f"Research: {task}"),
        run_agent(client, f"Summarize: {task}"),
    )

    research, summary = results
    return f"Research:\n{research}\n\nSummary:\n{summary}"
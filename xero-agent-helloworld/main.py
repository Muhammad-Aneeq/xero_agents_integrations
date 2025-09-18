#!/usr/bin/env python3
"""
OpenAI Agents SDK Integration Example

This example demonstrates how to use the Xero MCP Server
with the OpenAI Agents SDK to create AI agents that can
manage Xero accounting operations.
"""

import asyncio
import os
import shutil
from dotenv import load_dotenv
from agents.mcp import MCPServerStdio
from xero_agent_demos import run_demo_with_mcp
# Load environment variables
load_dotenv()


async def run_with_retry(max_retries=3, base_delay=5, timeout=90):
    """Try connecting to the Xero MCP server with retries and backoff."""
    for attempt in range(1, max_retries + 1):
        try:
            async with MCPServerStdio(
                name="Xero",
                params={
                    "command": "npx",
                    "args": ["-y", "@xeroapi/xero-mcp-server@latest"],
                    "env": {
                        "XERO_CLIENT_ID": os.environ['XERO_CLIENT_ID'],
                        "XERO_CLIENT_SECRET": os.environ['XERO_CLIENT_SECRET']
                    }
                },
                client_session_timeout_seconds=timeout,
            ) as server:
                return await run_demo_with_mcp(server)

        except Exception as e:
            if attempt == max_retries:
                print(f"❌ Failed after {max_retries} attempts. Error: {e}")
                raise
            wait_time = base_delay * attempt
            print(f"⚠️ Attempt {attempt} failed: {e}\nRetrying in {wait_time}s...")
            await asyncio.sleep(wait_time)


async def main():
    """Run the OpenAI Agents SDK integration examples."""
    # Check for required environment variables
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not set in environment")
        print("Please set your OpenAI API key to run this example")
        return
    
    if not os.getenv("XERO_CLIENT_ID") or not os.getenv("XERO_CLIENT_SECRET"):
        print("Error: Xero credentials not set in environment")
        print("Please set XERO_CLIENT_ID and XERO_CLIENT_SECRET")
        return
    
    # Check if npx is available
    if not shutil.which("npx"):
        raise RuntimeError("npx is not installed. Please install it with `npm install -g npx`.")
     
    # Run with retry logic
    await run_with_retry(max_retries=3, base_delay=5, timeout=90)

if __name__ == "__main__":
    asyncio.run(main()) 
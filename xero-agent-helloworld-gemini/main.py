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


async def main():
    """Run the OpenAI Agents SDK integration examples."""
    # Check for required environment variables
    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not set in environment")
        print("Please set your OpenAI API key to run this example")
        return
    
    if not os.getenv("XERO_CLIENT_ID") or not os.getenv("XERO_CLIENT_SECRET"):
        print("Error: Xero credentials not set in environment")
        print("Please set XERO_CLIENT_ID and XERO_CLIENT_SECRET")
        return
    
    # Check if npx is available
    if not shutil.which("npx"):
        raise RuntimeError("npx is not installed. Please install it with `npm install -g npx`.")
    # Initialize MCP server and run demos
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
        client_session_timeout_seconds=20
    ) as server:
        # trace_id = gen_trace_id()
        # with trace(workflow_name="Xero MCP Example", trace_id=trace_id):
        # print(f"View trace: https://platform.openai.com/traces/{trace_id}\n")
        await run_demo_with_mcp(server)


if __name__ == "__main__":
    asyncio.run(main()) 
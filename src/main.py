#!/usr/bin/env python3
"""
Main entry point for the Gemini MCP Server.

This server provides integration with Google Gemini CLI for AI-powered
development assistance through the Model Context Protocol.
"""

import asyncio
import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.server.gemini_server import create_server


def main() -> None:
    """
    Main entry point for the Gemini MCP Server.
    
    Starts the FastMCP server and handles the async event loop.
    """
    server = create_server()

    try:
        # Run the server with default settings
        asyncio.run(server.run())
    except KeyboardInterrupt:
        print("\nShutting down Gemini MCP Server...")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

"""
Program entry point for the OpenWeather CLI application.
Initalizes required resources and starts the CLI loop
"""

import sys
from cli import cli
from utils import tool_startup

if __name__ == "__main__":
    
    try:
        tool_startup()
        cli()
    except KeyboardInterrupt:
        print("\n")
    except Exception as e:
        sys.exit(f"Unexpected error: {e}.\nExiting")
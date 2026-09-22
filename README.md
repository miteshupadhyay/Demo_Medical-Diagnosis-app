# Demo_Medical-Diagnosis-app

# We will be exposing this tool in MCP as well.

# 1. uv init
# 2. uv venv
# 3.  .venv\Scripts\activate
# 4. uv add -r requirements.txt

# To Run the application
uvicorn app:app --host 0.0.0.0 --port 8083 --reload

http://localhost:8083/docs

{
  "description": "I am having fever"
}

# To register this MCP tool inside your Claude Deskop (inside JSON file) & claude desktop would be able to use this tool
mcp install mcp_tool.py

# To run it from inspector, it will open the MCP inspector and you can execute the same tool from there
uv run mcp dev mcp_tool.py
# This script runs a Python script using PowerShell

# Define the path to the Python script
$pythonScriptPath = "C:\Users\colem\PycharmProjects\ai_chatbot\main.py"

# Run the Python script
python $pythonScriptPath

# Optional: Wait for a key press before closing
Read-Host -Prompt "Press Enter to exit"

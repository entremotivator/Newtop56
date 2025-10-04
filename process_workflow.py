import json

with open("/home/ubuntu/upload/pasted_content.txt", "r") as f:
    workflow_data = json.load(f)

workflow_name = workflow_data.get("name", "Untitled Workflow")
description = "No description provided."
for node in workflow_data.get("nodes", []):
    if node.get("name") == "Sticky Note" and "content" in node.get("parameters", {}):
        description = node["parameters"]["content"]
        break

with open("streamlit_app/workflow_details.txt", "w") as f:
    f.write(f"Name: {workflow_name}\n")
    f.write(f"Description: {description}")

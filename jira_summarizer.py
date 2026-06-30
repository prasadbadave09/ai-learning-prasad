from groq import Groq
from dotenv import load_dotenv
import os
from prompt_library import get_ticket_summary_prompt
import json

load_dotenv()

client = Groq(api_key= os.getenv("GROQ_API_KEY"))


mock_tickets = [
    {
        "id": "PROJ-101",
        "title": "ADF page hangs on employee search with large dataset",
        "description": "When searching employees with more than 10,000 records, the search page freezes for 30+ seconds. Users report timeout errors in WebLogic logs.",
        "priority": "High",
        "status": "Open"
    },
    {
        "id": "PROJ-102",
        "title": "Salary update fails silently for contract employees",
        "description": "When HR updates salary for contract-type employees, the commit succeeds but the UI doesn't refresh. Database shows correct value but users think it failed.",
        "priority": "Medium",
        "status": "In Progress"
    },
    {
        "id": "PROJ-103",
        "title": "SQL injection vulnerability reported in legacy AM",
        "description": "Security audit flagged string concatenation in WHERE clause of EmployeeAMImpl.updateEmployeeSalary method. Needs immediate remediation.",
        "priority": "Critical",
        "status": "Open"
    }
]

print("Jira Ticket Summary Report\n")

message =[
    {
        "role":"system",
        "content" : get_ticket_summary_prompt()
    }
    ]

for jira_ticket in mock_tickets:
       
    message.append(
        {
            "role" : "user",
            "content" : json.dumps(jira_ticket)
        }
    )   
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=message
    )
    print(f"Summary for ticket id {jira_ticket['id']}\n")
    print(response.choices[0].message.content)
    message.pop()
    



from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key= os.getenv("GROQ_API_KEY"))

print("Paste your ADF code below. Type 'END' on a new line when done:")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)
code = "\n".join(lines)

messages = [
    {
        "role": "system",
        "content": """You are an expert Oracle ADF architect and Java developer.
Analyze ADF code step by step:
1. First identify what type of ADF component it is
2. Then explain what each method does
3. Then identify ADF-specific concepts used
4. Finally highlight any issues or improvements

Here are examples of good explanations:

Example 1:
Input: 
public ViewObject getEmployeeVO() {
    return findViewObject("EmployeeView1");
}
Output:
Component: Application Module method
What it does: Returns a reference to the EmployeeView1 ViewObject instance
ADF Concept: ViewObject lookup using findViewObject() — standard AM pattern
Issues: None — clean implementation

Example 2:
Input:
vo.setWhereClause("DEPT_ID = " + deptId);
Output:
Component: ViewObject query filter
What it does: Filters ViewObject data by department ID
ADF Concept: Dynamic WHERE clause on ViewObject
Issues: SQL injection risk — use setWhereClauseParam() instead

Now analyze the following ADF code using the same format:"""
            
    },
    {
        "role": "user",
        "content": code
    }
    
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages



)
print(response.choices[0].message.content)
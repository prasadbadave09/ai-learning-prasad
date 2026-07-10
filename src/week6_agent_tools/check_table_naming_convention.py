import re

def check_table_naming_convention(name: str) -> dict:
    if " " in name:
        return {
            "valid": False,
            "message": "Entity Object name should not contain spaces."
        }

    pattern = r"^[A-Z][a-zA-Z0-9]*EO$"

    if not re.match(pattern, name):
        return {
            "valid": False,
            "message": (
                "Entity Object name must follow PascalCase and end with 'EO'. "
                "Example: EmployeeEO"
            )
        }

    return {
        "valid": True,
        "message": "Valid Entity Object name."
    }


check_table_naming_convention_tool = {
    "type": "function",
    "function": {
        "name": "check_table_naming_convention",
        "description": "Returns the table naming convention is valid or not with the reason.",
        "parameters": {
            "type": "object",
            "properties": {
                "paragraph": {
                    "type": "string",
                    "description": "The table name to validate"
                }
            },
            "required": ["paragraph"]
        }
    }
}
from prompt_library import get_adf_explainer_prompt
from prompt_library import get_code_review_prompt

# Test 1 — print ADF explainer prompt
print("=== ADF Explainer Prompt ===")
print(get_adf_explainer_prompt())

print("\n=== Code Review Prompt (Java/ADF) ===")
print(get_code_review_prompt())

print("\n=== Code Review Prompt (Python/FastAPI) ===")
print(get_code_review_prompt(language="Python", framework="FastAPI"))
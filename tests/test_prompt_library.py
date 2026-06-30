import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from prompt_library import get_adf_explainer_prompt, get_code_review_prompt


def test_adf_explainer_prompt_not_empty():
    prompt = get_adf_explainer_prompt()
    assert prompt is not None
    assert len(prompt) > 0


def test_adf_explainer_prompt_mentions_adf():
    prompt = get_adf_explainer_prompt()
    assert "ADF" in prompt


def test_code_review_prompt_default_params():
    prompt = get_code_review_prompt()
    assert "Oracle ADF" in prompt
    assert "Java" in prompt


def test_code_review_prompt_custom_params():
    prompt = get_code_review_prompt(language="Python", framework="FastAPI")
    assert "Python" in prompt
    assert "FastAPI" in prompt
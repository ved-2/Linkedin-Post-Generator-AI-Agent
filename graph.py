from typing import Any
from pydantic import BaseModel

from llm import llm, feedback_llm, final_eval_llm
from prompts import (
    GENERATE_POST_PROMPT,
    ENGAGEMENT_PROMPT,
    READABILITY_PROMPT,
    RECRUITER_PROMPT,
    OPTIMIZE_POST_PROMPT,
    FINAL_EVALUATION_PROMPT,
)


def _normalize_feedback(feedback: Any) -> dict[str, Any]:
    if isinstance(feedback, BaseModel):
        return feedback.model_dump()
    return dict(feedback)


def _build_ai_feedback_text(feedbacks: list[dict[str, Any]]) -> str:
    result = ""
    for item in feedbacks:
        result += f"""
Evaluator: {item['evaluator']}
Score: {item['score']}
Strengths: {item['strengths']}
Weaknesses: {item['weaknesses']}
Suggestions: {item['suggestions']}

"""
    return result.strip()


def _strip_changelog(text: str) -> str:
    marker = "CHANGELOG:"
    marker_index = text.upper().find(marker)
    if marker_index == -1:
        return text.strip()
    return text[:marker_index].strip()


def generate_post(topic: str) -> str:
    prompt = GENERATE_POST_PROMPT.format(topic=topic)
    response = llm.invoke(prompt)
    return getattr(response, "content", str(response))


def _evaluate_with_prompt(prompt: str, post: str, evaluator_name: str) -> dict[str, Any]:
    result = feedback_llm.invoke(prompt.format(post=post))
    feedback = _normalize_feedback(result)
    feedback["evaluator"] = evaluator_name
    return feedback


def run_evaluators(post: str, audience: str = "Developers") -> list[dict[str, Any]]:
    evaluators = [
        (ENGAGEMENT_PROMPT, "Engagement Evaluator"),
        (READABILITY_PROMPT, "Readability Evaluator"),
    ]
    if audience == "Recruiters":
        evaluators.append((RECRUITER_PROMPT, "Recruiter Evaluator"))
    return [_evaluate_with_prompt(prompt, post, name) for prompt, name in evaluators]


def final_evaluation(feedbacks: list[dict[str, Any]]) -> dict[str, Any]:
    feedback_text = _build_ai_feedback_text(feedbacks)
    result = final_eval_llm.invoke(FINAL_EVALUATION_PROMPT.format(feedback=feedback_text))
    if isinstance(result, BaseModel):
        return result.model_dump()
    if hasattr(result, "content"):
        return getattr(result, "content")
    return _normalize_feedback(result)


def _build_advanced_optimize_prompt(post: str, ai_feedback: str, human_feedback: str, audience: str, tone: str, length: str, emojis: bool) -> str:
    length_map = {
        "Short": "~100 words",
        "Medium": "~200 words",
        "Long": "300+ words",
    }

    emoji_instruction = "Add 3-5 professional emojis." if emojis else "Do not add emojis."

    prompt = f"""
Improve this LinkedIn post.

Original Post:
{post}

AI Feedback:
{ai_feedback}

Human Feedback:
{human_feedback}

Target Audience:
{audience}

Tone:
{tone}

Requirements:

1. Fix all weaknesses
2. Improve engagement (questions, curiosity, CTA)
3. Improve readability (sentence & paragraph length)
4. Improve recruiter appeal (if audience is Recruiters)
5. Apply human feedback
6. Keep tone consistent
7. Add a clear CTA
8. Add relevant hashtags
9. Respect length: {length_map.get(length, 'Medium')}
10. {emoji_instruction}

Return only the improved LinkedIn-ready post. Do not include a changelog, JSON, labels, or explanation.
"""

    return prompt


def optimize_post(post: str, human_feedback: str, feedbacks: list[dict[str, Any]], audience: str = "Developers", tone: str = "Storytelling", length: str = "Medium", emojis: bool = False) -> str:
    ai_feedback = _build_ai_feedback_text(feedbacks)
    prompt = _build_advanced_optimize_prompt(
        post=post,
        ai_feedback=ai_feedback,
        human_feedback=human_feedback or "No additional human feedback provided.",
        audience=audience,
        tone=tone,
        length=length,
        emojis=emojis,
    )
    response = llm.invoke(prompt)
    return _strip_changelog(getattr(response, "content", str(response)))


def generate_workflow(topic: str, audience: str = "Developers") -> dict[str, Any]:
    generated_post = generate_post(topic)
    feedbacks = run_evaluators(generated_post, audience)
    final_eval = final_evaluation(feedbacks)
    return {
        "topic": topic,
        "generated_post": generated_post,
        "feedbacks": feedbacks,
        "final_evaluation": final_eval,
        "optimized_post": "",
    }


def optimize_workflow(post: str, human_feedback: str, feedbacks: list[dict[str, Any]], audience: str = "Developers", tone: str = "Storytelling", length: str = "Medium", emojis: bool = False) -> dict[str, Any]:
    # preserve the before score for comparison
    before_eval = final_evaluation(feedbacks)
    before_score = before_eval.get("overall_score") if isinstance(before_eval, dict) else None

    optimized_post = optimize_post(post, human_feedback, feedbacks, audience=audience, tone=tone, length=length, emojis=emojis)
    new_feedbacks = run_evaluators(optimized_post, audience)
    final_eval = final_evaluation(new_feedbacks)

    return {
        "optimized_post": optimized_post,
        "feedbacks": new_feedbacks,
        "final_evaluation": final_eval,
        "before_score": before_score,
    }

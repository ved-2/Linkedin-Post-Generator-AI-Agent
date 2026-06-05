from typing import TypedDict, Annotated
from pydantic import BaseModel, Field
import operator

class Feedback(BaseModel):
    evaluator: str = Field(
        description="Name of evaluator"
    )

    score: int = Field(
        description="Score out of 10"
    )

    strengths: list[str]

    weaknesses: list[str]

    suggestions: list[str]



class FinalEvaluation(BaseModel):
    overall_score: float

    summary: str

    strengths: list[str]

    weaknesses: list[str]

    suggestions: list[str]



class LinkedInState(TypedDict):
    topic: str

    generated_post: str

    feedbacks: Annotated[
        list[Feedback],
        operator.add
    ]

    human_feedback: str

    optimized_post: str

    final_evaluation: FinalEvaluation
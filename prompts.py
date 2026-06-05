# ==========================================
# Generate LinkedIn Post Prompt
# ==========================================

GENERATE_POST_PROMPT = """
You are an expert LinkedIn content creator.

Write a high-quality LinkedIn post on the topic below.

Topic:
{topic}

Requirements:
- Strong hook in first line
- Professional tone
- Storytelling style
- Actionable insights
- Clear Call-To-Action
- 150-250 words
- Use spacing for readability
- Optimize for engagement

Return only the LinkedIn post.
"""


# ==========================================
# Engagement Evaluator Prompt
# ==========================================

ENGAGEMENT_PROMPT = """
You are a LinkedIn engagement expert.

Evaluate the LinkedIn post.

Focus on:

- Hook quality
- Curiosity generation
- Engagement potential
- CTA effectiveness
- Virality potential

Post:

{post}

Return structured feedback.
"""


# ==========================================
# Readability Evaluator Prompt
# ==========================================

READABILITY_PROMPT = """
You are a content writing expert.

Evaluate the LinkedIn post.

Focus on:

- Readability
- Clarity
- Simplicity
- Grammar
- Flow

Post:

{post}

Return structured feedback.
"""


# ==========================================
# Recruiter Evaluator Prompt
# ==========================================

RECRUITER_PROMPT = """
You are a senior technical recruiter.

Evaluate this LinkedIn post.

Focus on:

- Professionalism
- Personal branding
- Recruiter appeal
- Industry relevance
- Career impact

Post:

{post}

Return structured feedback.
"""


# ==========================================
# Optimization Prompt
# ==========================================

OPTIMIZE_POST_PROMPT = """
You are an elite LinkedIn ghostwriter.

Improve the LinkedIn post.

Current Post:

{post}

AI Feedback:

{ai_feedback}

Human Feedback:

{human_feedback}

Requirements:

- Fix all weaknesses
- Incorporate human feedback
- Improve hook
- Improve readability
- Improve engagement
- Keep professional tone

Generate a completely improved version.
"""


# ==========================================
# Final Evaluation Prompt
# ==========================================

FINAL_EVALUATION_PROMPT = """
You are a LinkedIn content strategist.

Review all evaluator feedback below.

Feedback:

{feedback}

Generate:

1. Overall Score
2. Summary
3. Key Strengths
4. Key Weaknesses
5. Improvement Suggestions

Return structured output.
"""
import streamlit as st
import streamlit.components.v1 as components
import json

from graph import generate_workflow, optimize_workflow


st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")
st.title("LinkedIn Post Generator")
st.markdown(
    "Generate a LinkedIn post, get AI evaluation, and improve it with human feedback — all without popups."
)

# Sidebar controls (audience, tone, length, emojis, approve/reject)
st.sidebar.header("Optimization Controls")
audience = st.sidebar.selectbox("Audience", ["Recruiters", "Developers", "Students", "Founders"], index=1)
tone = st.sidebar.selectbox("Tone", ["Professional", "Technical", "Storytelling", "Motivational", "Founder"], index=2)
length = st.sidebar.selectbox("Length", ["Short", "Medium", "Long"], index=1)
emojis = st.sidebar.checkbox("Add emojis", value=False)

# st.sidebar.markdown("---")
# approve_choice = st.sidebar.radio("Approve or Reject", ["Pending", "Approve", "Reject"], index=0)
# reject_feedback = st.sidebar.text_area("If rejecting, what's the feedback?", value="", height=80)


def init_state() -> None:
    defaults = {
        "topic": "",
        "generated_post": "",
        "optimized_post": "",
        "human_feedback": "",
        "feedbacks": [],
        "final_evaluation": None,
        "status_message": "",
        "prev_final_evaluation": None,
        "before_score": None,
    }
    for key, default in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default


def render_feedback_section(feedbacks: list[dict[str, any]]) -> None:
    if not feedbacks:
        return

    st.markdown("### AI Evaluator Feedback")
    for item in feedbacks:
        st.markdown(f"**{item['evaluator']}**")
        st.markdown(f"- Score: {item.get('score', 'N/A')}/10")
        st.markdown(f"- Strengths: {', '.join(item.get('strengths', []))}")
        st.markdown(f"- Weaknesses: {', '.join(item.get('weaknesses', []))}")
        st.markdown(f"- Suggestions: {', '.join(item.get('suggestions', []))}")
        st.markdown("---")


def render_final_evaluation(final_eval: dict[str, any]) -> None:
    if not final_eval:
        return

    st.markdown("### AI Final Evaluation")
    st.markdown(f"**Overall score:** {final_eval.get('overall_score', 'N/A')}/10")
    st.markdown(f"**Summary:** {final_eval.get('summary', '')}")

    strengths = final_eval.get("strengths", [])
    weaknesses = final_eval.get("weaknesses", [])
    suggestions = final_eval.get("suggestions", [])

    if strengths:
        st.markdown("**Strengths:**")
        for strength in strengths:
            st.markdown(f"- {strength}")

    if weaknesses:
        st.markdown("**Weaknesses:**")
        for weakness in weaknesses:
            st.markdown(f"- {weakness}")

    if suggestions:
        st.markdown("**Suggestions:**")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")


def reset_generation_state() -> None:
    st.session_state.generated_post = ""
    st.session_state.optimized_post = ""
    st.session_state.feedbacks = []
    st.session_state.final_evaluation = None
    st.session_state.human_feedback = ""
    st.session_state.status_message = ""
    st.session_state.prev_final_evaluation = None
    st.session_state.before_score = None


init_state()

with st.form(key="generate_form"):
    topic = st.text_input(
        "Topic",
        value=st.session_state.topic,
        placeholder="Learning LangGraph",
        key="topic_input",
    )
    generate_pressed = st.form_submit_button("Generate Post")

if generate_pressed:
    if not topic.strip():
        st.warning("Please enter a topic before generating a post.")
    else:
        st.session_state.topic = topic.strip()
        reset_generation_state()
        with st.spinner("Generating post and evaluating AI feedback..."):
            result = generate_workflow(st.session_state.topic, audience=audience)
            st.session_state.generated_post = result["generated_post"]
            st.session_state.feedbacks = result["feedbacks"]
            st.session_state.final_evaluation = result["final_evaluation"]
            st.session_state.prev_final_evaluation = result["final_evaluation"]
            st.session_state.status_message = "Generated new post"
        st.success("Post generated successfully.")


current_post = st.session_state.optimized_post or st.session_state.generated_post
if current_post:
    heading = "Optimized Post" if st.session_state.optimized_post else "Generated Post"
    st.markdown(f"## {heading}")
    st.text_area("Post preview", value=current_post, height=280, key="post_preview")

    st.markdown("---")
    st.markdown("### Your Feedback")
    feedback_input = st.text_area(
        "What would you like to improve?",
        value=st.session_state.human_feedback,
        key="human_feedback_input",
        height=130,
    )
    st.session_state.human_feedback = feedback_input

    col1, col2 = st.columns(2)
    with col1:
        improve_pressed = st.button("Improve Post")
    with col2:
        approve_pressed = st.button("Approve & Finish")

    if improve_pressed:
        with st.spinner("Optimizing post with AI feedback..."):
            result = optimize_workflow(
                current_post,
                st.session_state.human_feedback,
                st.session_state.feedbacks,
                audience=audience,
                tone=tone,
                length=length,
                emojis=emojis,
            )
            st.session_state.optimized_post = result["optimized_post"]
            st.session_state.feedbacks = result["feedbacks"]
            st.session_state.final_evaluation = result["final_evaluation"]
            # retain previous evaluation for comparison
            st.session_state.prev_final_evaluation = st.session_state.prev_final_evaluation or st.session_state.final_evaluation
            st.session_state.before_score = result.get("before_score")
            st.session_state.status_message = "Post optimized"
        st.success("Post optimized. Review the updated version below.")
        st.rerun()

    if approve_pressed:
        st.success("Approved — your LinkedIn post is ready to publish.")

# # Sidebar approve/reject handling
# if approve_choice == "Approve":
#     st.sidebar.success("Post marked Approved")
# elif approve_choice == "Reject":
#     st.sidebar.warning("Post marked Rejected")
#     if reject_feedback.strip():
#         st.sidebar.info("Reviewer feedback saved")

# if st.session_state.status_message:
#     st.info(st.session_state.status_message)

# LinkedIn quick-share: copy to clipboard and open LinkedIn composer
if current_post:
    try:
        
        share_html = f"""
    <style>
    #shareBtn {{
        background: linear-gradient(135deg, #0A66C2, #004182);
        color: white;
        border: none;
        padding: 14px 24px;
        border-radius: 12px;
        cursor: pointer;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
    }}

    #shareBtn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(10,102,194,.4);
    }}

    .container {{
        text-align:center;
    }}

    .small {{
        display:block;
        margin-top:10px;
        color:#888;
    }}
    </style>

    <div class="container">

        <button id="shareBtn">
            Copy Post & Open LinkedIn
        </button>

        <span class="small">
            Copies post to clipboard and opens LinkedIn
        </span>

    </div>

    <script>

    const text = {json.dumps(current_post)};

    document
      .getElementById("shareBtn")
      .addEventListener("click", async () => {{

        try {{

            await navigator.clipboard.writeText(text);

            window.open(
                "https://www.linkedin.com/feed/?shareActive=true",
                "_blank"
            );

        }}

        catch(err) {{
            alert(
                "Clipboard access denied."
            );
        }}

      }});

    </script>
"""
        components.html(share_html, height=80)
    except Exception:
        st.write("Copy to LinkedIn not available in this environment. You can manually copy the post.")


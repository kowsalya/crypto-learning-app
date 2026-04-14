import streamlit as st
import json

st.set_page_config(page_title="Vibha Crypto Learning ")

st.title("📘Vibha Crypto Learning ")
st.subheader("Learn Step by Step")

# Load JSON
with open("faq.json", "r", encoding="utf-8") as f:
    all_topics = json.load(f)

# ---------------------------
# CATEGORY FILTER
# ---------------------------
categories = ["All"] + sorted(list(set([t["category"] for t in all_topics])))

selected_category = st.selectbox("📂 Select Category", categories)

# Filter topics
if selected_category == "All":
    topics = all_topics
else:
    topics = [t for t in all_topics if t["category"] == selected_category]

# ---------------------------
# SESSION STATE INDEX
# ---------------------------
if "index" not in st.session_state:
    st.session_state.index = 0

# Reset index when category changes
if "last_category" not in st.session_state:
    st.session_state.last_category = selected_category

if st.session_state.last_category != selected_category:
    st.session_state.index = 0
    st.session_state.last_category = selected_category

# Safety check
if len(topics) == 0:
    st.warning("No questions available")
    st.stop()

# Ensure index is in range
st.session_state.index = min(st.session_state.index, len(topics) - 1)

# ---------------------------
# DISPLAY CURRENT QUESTION
# ---------------------------
topic = topics[st.session_state.index]

st.markdown("---")

st.header(f"Q{st.session_state.index + 1}: {topic['question']}")
st.success(topic["answer"])

st.markdown("---")

# ---------------------------
# NAVIGATION BUTTONS
# ---------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅ Previous"):
        if st.session_state.index > 0:
            st.session_state.index -= 1

with col2:
    st.write(f"{st.session_state.index + 1} / {len(topics)}")

with col3:
    if st.button("Next ➡"):
        if st.session_state.index < len(topics) - 1:
            st.session_state.index += 1
           # ---------------------------
# EXTRA (TIP SECTION)
# ---------------------------
st.info("⚠ Always understand crypto before investing.")
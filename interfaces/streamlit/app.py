import streamlit as st
import requests

st.set_page_config(page_title="microsteps-ai", page_icon="🧠")

st.title("🧠 microsteps-ai")
st.subheader("Start something. Not everything.")

# --- Input ---
user_input = st.text_input(
    "What do you want to do?",
    placeholder="e.g. clean kitchen"
)

# --- Generate ---
if st.button("Generate microsteps"):
    if not user_input.strip():
        st.warning("Please enter something to start.")
    else:
        with st.spinner("Generating..."):
            try:
                response = requests.post(
                    "http://localhost:8006/generate-microsteps",
                    json={"task": user_input},
                    timeout=10
                )

                if response.status_code != 200:
                    st.error(f"Backend error: {response.status_code}")
                else:
                    data = response.json()
                    steps = data.get("microsteps", [])

                    if not steps:
                        st.warning("No steps generated. Try being more specific.")
                    else:
                        st.markdown("---")

                        # Step 1 (highlighted)
                        st.markdown(f"👉 **Step 1: {steps[0]}**")

                        st.markdown("")

                        # Remaining steps (less emphasis)
                        for i, step in enumerate(steps[1:], 2):
                            st.markdown(f"   Step {i}: {step}")

                        st.markdown("---")


            except Exception as e:
                st.error(f"Error: {e}")
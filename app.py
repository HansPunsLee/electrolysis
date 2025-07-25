import streamlit as st
from predict import predict_products
from half_equations import get_half_equation
from streamlit_lottie import st_lottie
from lottie_loader import load_lottie_url
from explanation_engine import get_explanation


st.set_page_config(page_title="Electrolysis Made Easy", layout="centered")

st.title("⚡ Electrolysis Made Easy")

st.markdown("""
This app helps you learn and predict products of **electrolytic cells**.  
It includes **Student Mode** for guided learning and **Practice Mode** for testing your understanding.
""")

# --- Mode selection ---
mode = st.radio("Choose your mode:", ["Student Mode", "Practice Mode"], horizontal=True)

# --- Input Section ---
st.header("🧪 Input Electrolysis Conditions")

cation = st.selectbox("Select Cation", ["Na⁺", "Cu²⁺", "Zn²⁺", "H⁺", "Ag⁺", "K⁺"])
anion = st.selectbox("Select Anion", ["Cl⁻", "SO₄²⁻", "NO₃⁻", "Br⁻", "I⁻", "OH⁻"])
concentration = st.selectbox("Electrolyte Concentration", ["low", "high"])
electrode_type = st.selectbox("Electrode Type", ["inert", "reactive"])
state = st.selectbox("Electrolyte State", ["aqueous", "molten"])

input_features = {
    "cation": cation,
    "anion": anion,
    "concentration": concentration,
    "electrode_type": electrode_type,
    "state": state
}

# --- Predict + Display ---
st.header("📲 Results & Feedback")

def to_subscript(text):
    subscript_map = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    result = ""
    for i, char in enumerate(text):
        if i > 0 and char.isdigit():
            result += char.translate(subscript_map)
        else:
            result += char
    return result



if st.button("🔍 Predict Products"):
    cathode_product, anode_product = predict_products(input_features)

    st.session_state.predicted = True
    st.session_state.cathode_product = cathode_product
    st.session_state.anode_product = anode_product

if st.session_state.get("predicted", False):
    cathode_product = st.session_state.cathode_product
    anode_product = st.session_state.anode_product

    st.success("✅ Prediction complete!")

    st.subheader("🔬 Predicted Products")
    st.markdown(f"**Cathode product:** {to_subscript(cathode_product)}")
    st.markdown(f"**Anode product:** {to_subscript(anode_product)}")

    st.subheader("⚗️ Half Equations")
    st.markdown(f"**Cathode reaction:** {get_half_equation(cathode_product)}")
    st.markdown(f"**Anode reaction:** {get_half_equation(anode_product)}")

    if mode == "Student Mode":
        st.subheader("📘 Explanation")
        explanation = get_explanation(
            cation=cation,
            anion=anion,
            concentration=concentration,
            electrode_type=electrode_type,
            state=state
        )

        if explanation:
            st.info(explanation)
        else:
            st.warning("No explanation available for this combination yet.")

    elif mode == "Practice Mode":
        st.subheader("📝 Your Answer")

        # Student dropdowns
        cathode_options = ["H₂", "Cu", "Ag", "Zn", "Na", "K", "none"]
        anode_options = ["O₂", "Cl₂", "Br₂", "I₂", "none"]

        user_cathode = st.selectbox("What is the **cathode product**?", options=cathode_options, key="user_cathode")
        user_anode = st.selectbox("What is the **anode product**?", options=anode_options, key="user_anode")

        if st.button("✅ Check Your Answer"):
            st.session_state.checked = True

        if st.session_state.get("checked", False):
            st.subheader("🔎 Results")

            if user_cathode.lower() == cathode_product.lower():
                st.success("Cathode product is correct! ✅")
            else:
                st.error(f"Incorrect. The correct cathode product is **{cathode_product}**.")

            if user_anode.lower() == anode_product.lower():
                st.success("Anode product is correct! ✅")
            else:
                st.error(f"Incorrect. The correct anode product is **{anode_product}**.")


    # Visual learner support
st.subheader("🎥 Visual Reaction")
fallback_animation_url = "https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json"  # Safe science-style animation

animation = load_lottie_url(fallback_animation_url)
if animation:
    st_lottie(animation, speed=1, height=300)
else:
    st.error("⚠️ Animation failed to load.")


# --- Footer ---
st.markdown("---")
st.caption("Developed by Hans Lee | © Electrolysis Made Easy")

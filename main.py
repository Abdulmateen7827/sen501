import streamlit as st

# Sample knowledge base
knowledge_base = [
    {"illness": "Flu", "symptoms": ["fever", "cough", "fatigue"]},
    {"illness": "Common Cold", "symptoms": ["runny nose", "sore throat", "cough"]},
    {"illness": "Allergies", "symptoms": ["sneezing", "itchy eyes", "runny nose"]}
]

def create_rules(knowledge_base):
    rules = []
    for item in knowledge_base:
        antecedent = " AND ".join(item["symptoms"])
        consequent = item["illness"]
        rule = f"IF {antecedent} THEN {consequent}"
        rules.append(rule)
    return rules

def forward_chaining(symptoms, rules):
    for rule in rules:
        antecedent, consequent = rule.split(" THEN ")
        conditions = antecedent.split(" AND ")
        if all(symptom.strip().lower() in symptoms for symptom in conditions):
            return consequent.strip()
    return "Unknown illness"

def main():
    st.set_page_config(page_title="🧠 Symptom Diagnosis App", page_icon="🩺")
    st.title("🧠 Intelligent Health Diagnosis Assistant")
    st.markdown(
        "<p style='font-size:16px; color:gray;'>"
        "Select your symptoms and get an instant diagnosis using simple rule-based AI."
        "</p>",
        unsafe_allow_html=True
    )

    # Extract all possible symptoms from the knowledge base
    all_symptoms = sorted({symptom for entry in knowledge_base for symptom in entry["symptoms"]})

    # UI for symptom selection
    user_symptoms = st.multiselect("🤒 What symptoms are you experiencing?", options=all_symptoms)

    if st.button("🔍 Diagnose"):
        rules = create_rules(knowledge_base)
        diagnosis = forward_chaining([s.lower() for s in user_symptoms], rules)
        st.success(f"🩺 Based on the symptoms, the diagnosis is: **{diagnosis}**")

    with st.expander("📜 View Diagnosis Rules"):
        for rule in create_rules(knowledge_base):
            st.markdown(f"- {rule}")

    st.markdown("<br><hr><small>Built with ❤️ by Group 6</small>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

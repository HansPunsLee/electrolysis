def get_explanation(cation, anion, concentration, electrode_type, state):
    explanations = []

    # --- Cation discharge logic ---
    if state == "aqueous":
        if cation in ["K⁺", "Na⁺", "Ca²⁺", "Mg²⁺"]:
            explanations.append(f"{cation} is more reactive than hydrogen, so H⁺ is reduced instead at the cathode.")
        elif cation in ["Cu²⁺", "Ag⁺"]:
            explanations.append(f"{cation} is less reactive than hydrogen, so it is reduced at the cathode.")
        else:
            explanations.append(f"The cation's reactivity is close to hydrogen, so discharge depends on exact conditions.")

    elif state == "molten":
        explanations.append("In molten state, only the cation and anion are present, so the metal cation is discharged.")

    # --- Anion discharge logic ---
    if anion in ["Cl⁻", "Br⁻", "I⁻"]:
        if concentration == "high":
            explanations.append(f"{anion} is a halide and is preferentially discharged at high concentration.")
        else:
            explanations.append(f"{anion} is a halide but at low concentration, OH⁻ may be discharged instead.")
    elif anion in ["SO₄²⁻", "NO₃⁻"]:
        explanations.append(f"{anion} is not discharged. OH⁻ from water is oxidised instead at the anode.")

    # --- Electrode type logic ---
    if electrode_type == "reactive":
        explanations.append("The reactive electrode may participate in the reaction (e.g., copper dissolving into solution).")
    else:
        explanations.append("Inert electrodes do not participate in the reaction. Only ions are involved.")

    return " ".join(explanations)

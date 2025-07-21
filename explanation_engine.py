def get_explanation(cation, anion, concentration, electrode_type, state):
    explanations = []

    # --- Molten State Logic ---
    if state == "molten":
        explanations.append(f"In the **molten state**, only **{cation}** and **{anion}** ions are present. "
                            "There is **no water**, so no H⁺ or OH⁻ ions are involved.")

        explanations.append(f"At the **cathode**, **{cation}** is reduced to form the metal.")

        if anion in ["Cl⁻", "Br⁻", "I⁻"]:
            explanations.append(f"At the **anode**, **{anion}** is oxidized to form the halogen gas.")
        else:
            explanations.append(f"At the **anode**, **{anion}** is oxidized to form its respective element.")

        if electrode_type == "reactive":
            explanations.append("The **reactive electrode** may participate in the reaction.")
        else:
            explanations.append("**Inert electrodes** do not participate in the reaction.")

        return " ".join(explanations)

    # --- Aqueous State Logic ---
    if state == "aqueous":
        # Cation logic
        if cation in ["K⁺", "Na⁺", "Ca²⁺", "Mg²⁺"]:
            explanations.append(f"{cation} is more reactive than hydrogen, so **H⁺** is reduced instead at the cathode.")
        elif cation in ["Cu²⁺", "Ag⁺"]:
            explanations.append(f"{cation} is less reactive than hydrogen, so it is reduced at the cathode.")
        else:
            explanations.append(f"{cation}'s reactivity is close to hydrogen, so discharge depends on conditions.")

        # Anion logic
        if anion in ["Cl⁻", "Br⁻", "I⁻"]:
            if concentration == "high":
                explanations.append(f"{anion} is a halide and is preferentially discharged at **high concentration**.")
            else:
                explanations.append(f"{anion} is a halide but at **low concentration**, **OH⁻** from water is discharged instead.")
        elif anion in ["SO₄²⁻", "NO₃⁻"]:
            explanations.append(f"{anion} is not discharged. **OH⁻** from water is oxidised instead at the anode.")

        # Electrode logic
        if electrode_type == "reactive":
            explanations.append("The **reactive electrode** may participate in the reaction (e.g., copper dissolving into solution).")
        else:
            explanations.append("**Inert electrodes** do not participate in the reaction.")

        return " ".join(explanations)

    return "No explanation available for the selected combination."

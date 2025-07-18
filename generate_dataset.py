# ml/generate_dataset.py

import pandas as pd
import os

# Rule-based function to simulate electrolysis outcome and redox equations
def simulate_electrolysis(electrolyte, cation, anion, concentration, electrode_type, state):
    reactive_vs_h = {
        "K⁺": "more", "Na⁺": "more", "Ca²⁺": "more",
        "Zn²⁺": "more", "Fe²⁺": "more",
        "H⁺": "equal",
        "Cu²⁺": "less", "Ag⁺": "less"
    }

    anion_type = {
        "Cl⁻": "halide", "Br⁻": "halide", "I⁻": "halide",
        "SO₄²⁻": "non-halide", "NO₃⁻": "non-halide", "OH⁻": "non-halide"
    }

    # Redox equation lookup table
    half_eqs = {
        "Cu": ("Cu²⁺ + 2e⁻ → Cu", "Cu → Cu²⁺ + 2e⁻"),
        "Zn": ("Zn²⁺ + 2e⁻ → Zn", "Zn → Zn²⁺ + 2e⁻"),
        "H₂": ("2H⁺ + 2e⁻ → H₂", "H₂ → 2H⁺ + 2e⁻"),
        "Ag": ("Ag⁺ + e⁻ → Ag", "Ag → Ag⁺ + e⁻"),
        "Na": ("Na⁺ + e⁻ → Na", "Na → Na⁺ + e⁻"),
        "Cl₂": ("2Cl⁻ → Cl₂ + 2e⁻", "Cl₂ + 2e⁻ → 2Cl⁻"),
        "Br₂": ("2Br⁻ → Br₂ + 2e⁻", "Br₂ + 2e⁻ → 2Br⁻"),
        "I₂": ("2I⁻ → I₂ + 2e⁻", "I₂ + 2e⁻ → 2I⁻"),
        "O₂": ("4OH⁻ → O₂ + 2H₂O + 4e⁻", "O₂ + 2H₂O + 4e⁻ → 4OH⁻")
    }

    # Default values
    cathode_product = "H₂"
    anode_product = "O₂"

    if state == "molten":
        cathode_product = cation[:-1]  # metal
        anode_product = anion[:-1] + "2"  # Cl₂, Br₂, etc.
    else:
        # Aqueous case
        if reactive_vs_h.get(cation, "more") == "less":
            cathode_product = cation[:-1]
        else:
            cathode_product = "H₂"

        if anion_type.get(anion, "non-halide") == "halide" and concentration == "high":
            anode_product = anion[:-1] + "2"
        else:
            anode_product = "O₂"

        if electrode_type == "reactive" and cation in ["Cu²⁺", "Zn²⁺"]:
            anode_product = cation[:-1]

    # Fetch half-equations
    cathode_eq = half_eqs.get(cathode_product, "")
    anode_eq = half_eqs.get(anode_product, "")

    return cathode_product, anode_product, cathode_eq, anode_eq


# Generate dataset
def build_dataset():
    records = []

    electrolytes = [
        ("NaCl", "Na⁺", "Cl⁻"),
        ("CuSO₄", "Cu²⁺", "SO₄²⁻"),
        ("ZnCl₂", "Zn²⁺", "Cl⁻"),
        ("H₂SO₄", "H⁺", "SO₄²⁻"),
        ("AgNO₃", "Ag⁺", "NO₃⁻"),
        ("KBr", "K⁺", "Br⁻"),
        ("KI", "K⁺", "I⁻"),
        ("NaOH", "Na⁺", "OH⁻"),
    ]

    concentrations = ["low", "high"]
    electrodes = ["inert", "reactive"]
    states = ["aqueous", "molten"]

    for (name, cation, anion) in electrolytes:
        for conc in concentrations:
            for elec in electrodes:
                for state in states:
                    cathode, anode, cath_eq, an_eq = simulate_electrolysis(
                        name, cation, anion, conc, elec, state
                    )
                    records.append({
                        "electrolyte": name,
                        "cation": cation,
                        "anion": anion,
                        "concentration": conc,
                        "electrode_type": elec,
                        "state": state,
                        "cathode_product": cathode,
                        "anode_product": anode,
                        "cathode_half_eq": cath_eq,
                        "anode_half_eq": an_eq
                    })

    return pd.DataFrame(records)


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    df = build_dataset()
    df.to_csv("data/electrolytic_dataset.csv", index=False)
    print("✅ Dataset generated and saved to data/electrolytic_dataset.csv")

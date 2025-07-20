# half_equations.py

def get_half_equation(species):
    half_equation_dict = {
        # Cathode (reduction) products
        "H⁺": "2H⁺ + 2e⁻ → H₂",
        "Cu²⁺": "Cu²⁺ + 2e⁻ → Cu",
        "Ag⁺": "Ag⁺ + e⁻ → Ag",
        "Na⁺": "Na⁺ + e⁻ → Na  (not usually discharged in aqueous solutions)",
        "Zn²⁺": "Zn²⁺ + 2e⁻ → Zn",
        "K⁺": "K⁺ + e⁻ → K  (not usually discharged in aqueous solutions)",

        # Anode (oxidation) ions
        "Cl⁻": "2Cl⁻ → Cl₂ + 2e⁻",
        "Br⁻": "2Br⁻ → Br₂ + 2e⁻",
        "I⁻": "2I⁻ → I₂ + 2e⁻",
        "OH⁻": "4OH⁻ → O₂ + 2H₂O + 4e⁻",
        "SO₄²⁻": "no discharge; usually H₂O or OH⁻ oxidized",
        "NO₃⁻": "no discharge; usually H₂O or OH⁻ oxidized",

        # Product name mappings (redundant but useful for clarity)
        "H₂": "2H⁺ + 2e⁻ → H₂",
        "Cu": "Cu²⁺ + 2e⁻ → Cu",
        "Ag": "Ag⁺ + e⁻ → Ag",
        "Zn": "Zn²⁺ + 2e⁻ → Zn",
        "Na": "Na⁺ + e⁻ → Na",

        "Cl₂": "2Cl⁻ → Cl₂ + 2e⁻",
        "Br₂": "2Br⁻ → Br₂ + 2e⁻",
        "I₂": "2I⁻ → I₂ + 2e⁻",
        "O₂": "4OH⁻ → O₂ + 2H₂O + 4e⁻",
    }

    return half_equation_dict.get(species, "⚠️ No half-equation available for this species.")

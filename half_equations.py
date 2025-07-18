# Dictionary lookup for half-equations

half_equations = {
    "Na⁺": "Na⁺ + e⁻ → Na",
    "K⁺": "K⁺ + e⁻ → K",
    "Cu²⁺": "Cu²⁺ + 2e⁻ → Cu",
    "Ag⁺": "Ag⁺ + e⁻ → Ag",
    "H⁺": "2H⁺ + 2e⁻ → H₂",

    "Cl⁻": "2Cl⁻ → Cl₂ + 2e⁻",
    "Br⁻": "2Br⁻ → Br₂ + 2e⁻",
    "I⁻": "2I⁻ → I₂ + 2e⁻",
    "OH⁻": "4OH⁻ → O₂ + 2H₂O + 4e⁻",
    "SO₄²⁻": "4OH⁻ → O₂ + 2H₂O + 4e⁻",
    "NO₃⁻": "4OH⁻ → O₂ + 2H₂O + 4e⁻",
}

def get_half_equation(ion):
    return half_equations.get(ion, "Equation not available")

import json
import os

# --- LE CERVEAU ULTRA-COMPLET (Tes 4 Piliers) ---
SEARCH_CONFIG = {
    "Piliers": {
        "Intégration Interculturelle": [
            "Interculturalisme", "Intégration Interculturelle", "Politiques de citoyenneté (Québec)", 
            "immigration", "Législation en immigration (Québec)", "politiques d’immigration", 
            "intégration au marché du travail", "parents immigrants"
        ],
        "Sciences Sociales": [
            "ingénierie sociale", "Médiation interculturelle", "Intégration en milieu de travail", 
            "Gestion de la diversité en entreprise", "Psychologie de l'acculturation", "inclusion sociale", 
            "Rapports de pouvoir en entreprise", "Acfas", "recherche universitaire", "sociologie", "éducation", "Pratiques culturelles", "cohésion sociale", 
            "lien social", "capital social", "dialogue citoyen", "participation démocratique", 
            "médiation communautaire", "gestion axée sur les résultats", "données terrain"
        ],
        "Politique et identité nationale": [
            "histoire du Québec", "identité nationale", "Politiques de citoyenneté", "identité québécoise",
            "Transmission de la mémoire collective", "Identité québécoise contemporaine", "laïcité", "valeurs québécoises", 
            "Muséologie et appartenance", "indépendance du Québec", "souveraineté", "Parti Québécois", 
            "récit national", "mémoire collective", "patrimoine", "socialisation civique"
        ],
        "Gouvernance collaborative & concertation": [
            "gouvernance multi-acteurs", "concertation", "gouvernance collaborative", "innovation sociale", "coordination interinstitutionnelle", 
            "tables de concertation"
        ]
    },
    "Villes": ["Montréal", "Québec", "Laval", "Sherbrooke"],
    "Année": 2026
}

# --- DONNÉES DE RECHERCHE (Conférences 2026) ---
CONFERENCES_DATA = [
    {
        "id": 1, "titre": "93e Congrès de l'Acfas (UQAM)", "date": "2026-05-11", "dateFin": "2026-05-15",
        "lieu": "Montréal (UQAM)", "categorie": "Sciences Sociales",
        "description": "Cohésion sociale, lien social et participation démocratique.",
        "lien": "https://www.acfas.ca"
    },
    {
        "id": 2, "titre": "Salon de l'immigration et de l'intégration (SIIQ)", "date": "2026-05-27", "dateFin": "2026-05-28",
        "lieu": "Montréal", "categorie": "Intégration Interculturelle",
        "description": "Législation en immigration et intégration au marché du travail.",
        "lien": "https://salonimmigration.com"
    },
    {
        "id": 3, "titre": "Colloque international du CELAT 2026", "date": "2026-06-15", "dateFin": "2026-06-17",
        "lieu": "Montréal", "categorie": "Politique et identité nationale",
        "description": "Identité québécoise contemporaine et muséologie de l'appartenance.",
        "lien": "https://celat.ca"
    },
    {
        "id": 4, "titre": "ICGPP : Governance and Public Policy", "date": "2026-08-14", "dateFin": "2026-08-14",
        "lieu": "Montréal", "categorie": "Gouvernance collaborative & concertation",
        "description": "Gouvernance multi-acteurs et coordination interinstitutionnelle.",
        "lien": "https://researchfoundation.net"
    }
]

def update_app_js():
    js_path = 'app.js'
    if not os.path.exists(js_path): return
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    import re
    new_data = "const conferences = " + json.dumps(CONFERENCES_DATA, indent=4, ensure_ascii=False) + ";"
    pattern = r"const conferences = \[.*?\];"
    new_content = re.sub(pattern, new_data, content, flags=re.DOTALL)
    with open(js_path, 'w', encoding='utf-8') as f: f.write(new_content)
    print("Mise à jour réussie !")

if __name__ == "__main__":
    update_app_js()

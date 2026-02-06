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


# --- TES 16 CONFÉRENCES (Sauvegardées dans le Cloud) ---
CONFERENCES_DATA = [
    {"id": 1, "titre": "Salon de l'immigration et de l'intégration (SIIQ)", "date": "2026-05-27", "dateFin": "2026-05-28", "lieu": "Palais des congrès de Montréal", "categorie": "Intégration Interculturelle", "description": "Législation en immigration et intégration au marché du travail.", "lien": "https://salonimmigration.com"},
    {"id": 2, "titre": "ICILRPP : Immigration Law Reforms & Policy", "date": "2026-06-06", "dateFin": "2026-06-06", "lieu": "Montréal", "categorie": "Intégration Interculturelle", "description": "Analyse des réformes législatives en immigration au Québec.", "lien": "https://waset.org"},
    {"id": 3, "titre": "Journée d'étude OIRQ : Laïcité et Inégalités", "date": "2026-03-24", "dateFin": "2026-03-24", "lieu": "UQAM, Montréal", "categorie": "Intégration Interculturelle", "description": "Enjeux de laïcité et de cohésion sociale à l'école.", "lien": "https://sacr.ca"},
    {"id": 4, "titre": "Concordia : From Departure to Belonging", "date": "2026-10-15", "dateFin": "2026-10-17", "lieu": "Montréal", "categorie": "Intégration Interculturelle", "description": "Inclusion numérique et parcours migratoires.", "lien": "https://www.concordia.ca"},
    {"id": 5, "titre": "93e Congrès de l'Acfas (UQAM)", "date": "2026-05-11", "dateFin": "2026-05-15", "lieu": "Montréal", "categorie": "Sciences Sociales", "description": "Cohésion sociale, capital social et participation démocratique.", "lien": "https://www.acfas.ca"},
    {"id": 6, "titre": "ICEDI : Equality, Diversity and Inclusion", "date": "2026-05-18", "dateFin": "2026-05-19", "lieu": "Montréal", "categorie": "Sciences Sociales", "description": "Gestion de la diversité en entreprise et rapports de pouvoir.", "lien": "https://waset.org"},
    {"id": 7, "titre": "IIIe Congrès international de l'ÉDIQ", "date": "2026-06-02", "dateFin": "2026-06-04", "lieu": "Québec", "categorie": "Sciences Sociales", "description": "Médiation interculturelle et psychologie de l'acculturation.", "lien": "https://www.ediq.ulaval.ca"},
    {"id": 8, "titre": "Colloque international du CELAT 2026", "date": "2026-06-15", "dateFin": "2026-06-17", "lieu": "Montréal / Québec", "categorie": "Sciences Sociales", "description": "Médiation interculturelle et appartenance.", "lien": "https://celat.ca"},
    {"id": 9, "titre": "Measuring Beyond 2026 (HEC Montréal)", "date": "2026-02-10", "dateFin": "2026-02-10", "lieu": "HEC Montréal", "categorie": "Sciences Sociales", "description": "Gestion axée sur les résultats et innovation responsable.", "lien": "https://www.hec.ca"},
    {"id": 10, "titre": "Colloque FHQ : Notre histoire politique", "date": "2026-09-18", "dateFin": "2026-09-19", "lieu": "Québec", "categorie": "Politique et Identité", "description": "Récit national et transmission de la mémoire collective.", "lien": "https://histoirequebec.qc.ca"},
    {"id": 11, "titre": "Colloque CÉRIUM : International et Recherche", "date": "2026-01-29", "dateFin": "2026-01-30", "lieu": "Montréal", "categorie": "Politique et Identité", "description": "Socialisation civique et décolonialité au Québec.", "lien": "https://cerium.umontreal.ca"},
    {"id": 12, "titre": "Conference on Identity, Memory and Narratives", "date": "2026-04-18", "dateFin": "2026-04-18", "lieu": "Montréal", "categorie": "Politique et Identité", "description": "Transmission de la mémoire et identité nationale.", "lien": "https://researchleagues.com"},
    {"id": 13, "titre": "ICGPP : Governance and Public Policy", "date": "2026-08-14", "dateFin": "2026-08-14", "lieu": "Montréal", "categorie": "Gouvernance collaborative", "description": "Gouvernance multi-acteurs et coordination interinstitutionnelle.", "lien": "https://conferencealerts.co.in"},
    {"id": 14, "titre": "International Organizations & Global Governance", "date": "2026-10-12", "dateFin": "2026-10-12", "lieu": "Montréal", "categorie": "Gouvernance collaborative", "description": "Concertation internationale et gérance multi-acteurs.", "lien": "https://researchfoundation.net"},
    {"id": 15, "titre": "Appel de projets : Programmation Citoyenne", "date": "2026-01-01", "dateFin": "2026-12-31", "lieu": "Québec", "categorie": "Gouvernance collaborative", "description": "Participation démocratique et dialogue citoyen.", "lien": "http://assnat.qc.ca"},
    {"id": 16, "titre": "Mois de l'innovation publique", "date": "2026-06-01", "dateFin": "2026-06-30", "lieu": "Québec / Montréal", "categorie": "Gouvernance collaborative", "description": "Collaboration interinstitutionnelle et transformation publique.", "lien": "https://www.quebec.ca"}
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

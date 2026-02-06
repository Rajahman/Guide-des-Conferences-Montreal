import json
import os
import re

# --- LE CERVEAU & LE RADAR COMPLET ---
SEARCH_CONFIG = {
    "Piliers": {
        "Intégration Interculturelle": ["Interculturalisme", "Intégration Interculturelle", "Politiques de citoyenneté (Québec)", "immigration", "Législation en immigration (Québec)", "politiques d’immigration", "intégration au marché du travail", "parents immigrants"],
        "Sciences Sociales": ["ingénierie sociale", "Médiation interculturelle", "Intégration en milieu de travail", "Gestion de la diversité en entreprise", "Psychologie de l'acculturation", "inclusion sociale", "Rapports de pouvoir en entreprise", "Acfas", "recherche universitaire", "sociologie", "éducation", "Pratiques culturelles", "cohésion sociale", "lien social", "capital social", "dialogue citoyen", "participation démocratique", "médiation communautaire", "gestion axée sur les résultats", "données terrain"],
        "Politique et identité nationale": ["histoire du Québec", "identité nationale", "Politiques de citoyenneté", "identité québécoise", "Transmission de la mémoire collective", "Identité québécoise contemporaine", "laïcité", "valeurs québécoises", "Muséologie et appartenance", "indépendance du Québec", "souveraineté", "Parti Québécois", "récit national", "mémoire collective", "patrimoine", "socialisation civique"],
        "Gouvernance collaborative & concertation": ["gouvernance multi-acteurs", "concertation", "gouvernance collaborative", "innovation sociale", "coordination interinstitutionnelle", "tables de concertation"]
    },
    "Villes": ["Montréal", "Québec", "Laval", "Sherbrooke"],
    "Année": 2026,
    "Sources_Scanning": [
        "https://waset.org/social-sciences-conferences-in-montreal", "https://allconferencealert.com/montreal.html", "http://www.wikicfp.com/cfp/call?conference=montreal", "https://internationalconferencealerts.com/canada/montreal.html",
        "https://www.acfas.ca/evenements/congres", "https://www.celat.ca/activites/", "https://crises.uqam.ca/activites/", "https://calenda.org/search?q=Quebec", "https://www.banq.qc.ca/calendrier/",
        "https://socialinnovationforum.ca/evenements/", "https://mis.quebec/nos-activites/", "https://inm.qc.ca/evenements/",
        "https://www.ccmm.ca/fr/evenements/", "https://www.corim.qc.ca/fr/evenements", "https://congresmtl.com/calendrier/",
        "https://www.eventbrite.ca/d/canada--montreal/conferences/", "https://www.mtl.org/fr/quoi-faire/evenements", "https://www.quebec.ca/immigration/services-accueil-integration/", "https://www.lavitrine.com/evenements",
        "https://calendrier.umontreal.ca/", "https://evenements.uqam.ca/", "https://www.mcgill.ca/events/", "https://www.hec.ca/evenements/", "https://www.concordia.ca/events.html", "https://montreal.ca/agenda"
    ]
}

# --- TA MÉMOIRE SACRÉE (Heures ajoutées en démonstration) ---
BASE_DATA = [
    {"id": 1, "titre": "Salon de l'immigration et de l'intégration (SIIQ)", "date": "2026-05-27", "dateFin": "2026-05-28", "lieu": "Palais des congrès de Montréal", "categorie": "Intégration Interculturelle", "description": "Législation en immigration, intégration au marché du travail et ressources pour parents immigrants.", "lien": "https://salonimmigration.com", "heure": "09:00 - 17:00"},
    {"id": 2, "titre": "ICILRPP : Immigration Law Reforms & Policy", "date": "2026-06-06", "dateFin": "2026-06-06", "lieu": "Montréal", "categorie": "Intégration Interculturelle", "description": "Analyse des réformes législatives en immigration et des politiques de citoyenneté du Québec.", "lien": "https://waset.org", "heure": "10:30"},
    {"id": 3, "titre": "Journée d'étude OIRQ : Laïcité et Inégalités", "date": "2026-03-24", "dateFin": "2026-03-24", "lieu": "UQAM, Montréal", "categorie": "Intégration Interculturelle", "description": "Analyse des enjeux de laïcité, de racisme et de cohésion sociale dans l'école québécoise.", "lien": "https://sacr.ca"},
    {"id": 4, "titre": "Concordia : From Departure to Belonging", "date": "2026-10-15", "dateFin": "2026-10-17", "lieu": "Université Concordia, Montréal", "categorie": "Intégration Interculturelle", "description": "Technologies numériques et parcours migratoires : inclusion, contrôle et participation citoyenne.", "lien": "https://www.concordia.ca"},
    {"id": 5, "titre": "93e Congrès de l'Acfas (UQAM)", "date": "2026-05-11", "dateFin": "2026-05-15", "lieu": "Université du Québec à Montréal (UQAM)", "categorie": "Sciences Sociales", "description": "Le plus grand rassemblement scientifique francophone. Focus : cohésion sociale, capital social et participation démocratique.", "lien": "https://www.acfas.ca"},
    {"id": 6, "titre": "ICEDI : Equality, Diversity and Inclusion", "date": "2026-05-18", "dateFin": "2026-05-19", "lieu": "Montréal", "categorie": "Sciences Sociales", "description": "Gestion de la diversité en entreprise, rapports de pouvoir et psychologie de l'acculturation.", "lien": "https://waset.org"},
    {"id": 7, "titre": "IIIe Congrès international de l'ÉDIQ", "date": "2026-06-02", "dateFin": "2026-06-04", "lieu": "Université Laval", "categorie": "Sciences Sociales", "description": "Immigrer, vivre et se (re)construire : médiation interculturelle et psychologie de l'acculturation.", "lien": "https://www.ediq.ulaval.ca"},
    {"id": 8, "titre": "Colloque international du CELAT 2026", "date": "2026-06-15", "dateFin": "2026-06-17", "lieu": "Montréal / Québec", "categorie": "Sciences Sociales", "description": "Médiation interculturelle et appartenance : le(s) monde(s) en train de se faire.", "lien": "https://celat.ca"},
    {"id": 9, "titre": "Measuring Beyond 2026 (HEC Montréal)", "date": "2026-02-10", "dateFin": "2026-02-10", "lieu": "HEC Montréal", "categorie": "Sciences Sociales", "description": "Gestion axée sur les résultats, innovation responsable et leadership en entreprise.", "lien": "https://www.hec.ca"},
    {"id": 10, "titre": "Colloque FHQ : Notre histoire politique", "date": "2026-09-18", "dateFin": "2026-09-19", "lieu": "Ville de Québec", "categorie": "Politique et identité nationale", "description": "Récit national, transmission de la mémoire collective et identité québécoise contemporaine.", "lien": "https://histoirequebec.qc.ca"},
    {"id": 11, "titre": "Colloque CÉRIUM : International et Recherche", "date": "2026-01-29", "dateFin": "2026-01-30", "lieu": "Université de Montréal", "categorie": "Politique et identité nationale", "description": "Tensions entre recherche et médias : décolonialité et socialisation civique au Québec.", "lien": "https://cerium.umontreal.ca"},
    {"id": 12, "titre": "Conference on Identity, Memory and Narratives", "date": "2026-04-18", "dateFin": "2026-04-18", "lieu": "Montréal", "categorie": "Politique et identité nationale", "description": "Étude interdisciplinaire sur la transmission de la mémoire et l'identité nationale.", "lien": "https://researchleagues.com"},
    {"id": 13, "titre": "ICGPP : Governance and Public Policy", "date": "2026-08-14", "dateFin": "2026-08-14", "lieu": "Montréal", "categorie": "Gouvernance collaborative & concertation", "description": "Gouvernance multi-acteurs, coordination interinstitutionnelle et tables de concertation.", "lien": "https://conferencealerts.co.in"},
    {"id": 14, "titre": "International Organizations & Global Governance", "date": "2026-10-12", "dateFin": "2026-10-12", "lieu": "Montréal", "categorie": "Gouvernance collaborative & concertation", "description": "Concertation internationale et gérance multi-acteurs face aux enjeux mondiaux.", "lien": "https://researchfoundation.net"},
    {"id": 15, "titre": "Appel de projets : Programmation Citoyenne", "date": "2026-01-01", "dateFin": "2026-12-31", "lieu": "Assemblée nationale du Québec", "categorie": "Gouvernance collaborative & concertation", "description": "Participation démocratique et dialogue citoyen : conférences et tables rondes 2026-2027.", "lien": "http://assnat.qc.ca"},
    {"id": 16, "titre": "Mois de l'innovation publique", "date": "2026-06-01", "dateFin": "2026-06-30", "lieu": "Québec / Montréal", "categorie": "Gouvernance collaborative & concertation", "description": "Collaboration interinstitutionnelle et transformation des services publics.", "lien": "https://www.quebec.ca"}
]

def update_app_js():
    js_path = 'app.js'
    if not os.path.exists(js_path): return
    with open(js_path, 'r', encoding='utf-8') as f: content = f.read()
    
    # Tri par date
    BASE_DATA.sort(key=lambda x: x['date'])
    
    new_data_str = "const conferences = " + json.dumps(BASE_DATA, indent=4, ensure_ascii=False) + ";"
    pattern = r"const conferences = \[.*?\];"
    new_content = re.sub(pattern, new_data_str, content, flags=re.DOTALL)
    
    with open(js_path, 'w', encoding='utf-8') as f: f.write(new_content)
    print(f"Robot : {len(BASE_DATA)} conférences à jour avec support de l'heure !")

if __name__ == "__main__":
    update_app_js()

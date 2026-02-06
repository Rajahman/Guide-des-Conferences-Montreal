document.addEventListener('DOMContentLoaded', () => {
    const conferences = [
        {"id": 1, "titre": "Salon de l'immigration et de l'intégration (SIIQ)", "date": "2026-05-27", "dateFin": "2026-05-28", "lieu": "Palais des congrès de Montréal", "categorie": "Intégration Interculturelle", "description": "Législation en immigration, intégration au marché du travail et ressources pour parents immigrants.", "lien": "https://salonimmigration.com", "heure": "09:00 - 17:00"},
        {"id": 11, "titre": "Colloque CÉRIUM : International et Recherche", "date": "2026-01-29", "dateFin": "2026-01-30", "lieu": "Université de Montréal", "categorie": "Politique et identité nationale", "description": "Tensions entre recherche et médias : décolonialité et socialisation civique au Québec.", "lien": "https://cerium.umontreal.ca"},
        {"id": 15, "titre": "Appel de projets : Programmation Citoyenne", "date": "2026-01-01", "dateFin": "2026-12-31", "lieu": "Assemblée nationale du Québec", "categorie": "Gouvernance collaborative & concertation", "description": "Participation démocratique et dialogue citoyen : conférences et tables rondes 2026-2027.", "lien": "http://assnat.qc.ca"},
        {"id": 9, "titre": "Measuring Beyond 2026 (HEC Montréal)", "date": "2026-02-10", "dateFin": "2026-02-10", "lieu": "HEC Montréal", "categorie": "Sciences Sociales", "description": "Gestion axée sur les résultats, innovation responsable et leadership en entreprise.", "lien": "https://www.hec.ca"},
        {"id": 3, "titre": "Journée d'étude OIRQ : Laïcité et Inégalités", "date": "2026-03-24", "dateFin": "2026-03-24", "lieu": "UQAM, Montréal", "categorie": "Intégration Interculturelle", "description": "Analyse des enjeux de laïcité, de racisme et de cohésion sociale dans l'école québécoise.", "lien": "https://sacr.ca"},
        {"id": 12, "titre": "Conference on Identity, Memory and Narratives", "date": "2026-04-18", "dateFin": "2026-04-18", "lieu": "Montréal", "categorie": "Politique et identité nationale", "description": "Étude interdisciplinaire sur la transmission de la mémoire et l'identité nationale.", "lien": "https://researchleagues.com"},
        {"id": 5, "titre": "93e Congrès de l'Acfas (UQAM)", "date": "2026-05-11", "dateFin": "2026-05-15", "lieu": "Université du Québec à Montréal (UQAM)", "categorie": "Sciences Sociales", "description": "Le plus grand rassemblement scientifique francophone. Focus : cohésion sociale, capital social et participation démocratique.", "lien": "https://www.acfas.ca"},
        {"id": 6, "titre": "ICEDI : Equality, Diversity and Inclusion", "date": "2026-05-18", "dateFin": "2026-05-19", "lieu": "Montréal", "categorie": "Sciences Sociales", "description": "Gestion de la diversité en entreprise, rapports de pouvoir et psychologie de l'acculturation.", "lien": "https://waset.org"},
        {"id": 7, "titre": "IIIe Congrès international de l'ÉDIQ", "date": "2026-06-02", "dateFin": "2026-06-04", "lieu": "Université Laval", "categorie": "Sciences Sociales", "description": "Immigrer, vivre et se (re)construire : médiation interculturelle et psychologie de l'acculturation.", "lien": "https://www.ediq.ulaval.ca"},
        {"id": 16, "titre": "Mois de l'innovation publique", "date": "2026-06-01", "dateFin": "2026-06-30", "lieu": "Québec / Montréal", "categorie": "Gouvernance collaborative & concertation", "description": "Collaboration interinstitutionnelle et transformation des services publics.", "lien": "https://www.quebec.ca"},
        {"id": 2, "titre": "ICILRPP : Immigration Law Reforms & Policy", "date": "2026-06-06", "dateFin": "2026-06-06", "lieu": "Montréal", "categorie": "Intégration Interculturelle", "description": "Analyse des réformes législatives en immigration et des politiques de citoyenneté du Québec.", "lien": "https://waset.org", "heure": "10:30"},
        {"id": 8, "titre": "Colloque international du CELAT 2026", "date": "2026-06-15", "dateFin": "2026-06-17", "lieu": "Montréal / Québec", "categorie": "Sciences Sociales", "description": "Médiation interculturelle et appartenance : le(s) monde(s) en train de se faire.", "lien": "https://celat.ca"},
        {"id": 13, "titre": "ICGPP : Governance and Public Policy", "date": "2026-08-14", "dateFin": "2026-08-14", "lieu": "Montréal", "categorie": "Gouvernance collaborative & concertation", "description": "Gouvernance multi-acteurs, coordination interinstitutionnelle et tables de concertation.", "lien": "https://conferencealerts.co.in"},
        {"id": 10, "titre": "Colloque FHQ : Notre histoire politique", "date": "2026-09-18", "dateFin": "2026-09-19", "lieu": "Ville de Québec", "categorie": "Politique et identité nationale", "description": "Récit national, transmission de la mémoire collective et identité québécoise contemporaine.", "lien": "https://histoirequebec.qc.ca"},
        {"id": 14, "titre": "International Organizations & Global Governance", "date": "2026-10-12", "dateFin": "2026-10-12", "lieu": "Montréal", "categorie": "Gouvernance collaborative & concertation", "description": "Concertation internationale et gérance multi-acteurs face aux enjeux mondiaux.", "lien": "https://researchfoundation.net"},
        {"id": 4, "titre": "Concordia : From Departure to Belonging", "date": "2026-10-15", "dateFin": "2026-10-17", "lieu": "Université Concordia, Montréal", "categorie": "Intégration Interculturelle", "description": "Technologies numériques et parcours migratoires : inclusion, contrôle et participation citoyenne.", "lien": "https://www.concordia.ca"}
    ];

    const listContainer = document.getElementById('conferences-list');
    const filtersContainer = document.getElementById('filters-container');

    function initFilters() {
        const categories = ['Tous', 'Sciences Sociales', 'Intégration Interculturelle', 'Politique et identité nationale', 'Gouvernance collaborative & concertation'];
        filtersContainer.innerHTML = '';
        categories.forEach(cat => {
            const btn = document.createElement('button');
            btn.className = 'filter-btn' + (cat === 'Tous' ? ' active' : '');
            btn.textContent = cat;
            btn.onclick = () => {
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                filterByCategory(cat);
            };
            filtersContainer.appendChild(btn);
        });
    }

    function filterByCategory(category) {
        let filtered = conferences;
        if (category !== 'Tous') {
            filtered = conferences.filter(c => c.categorie === category);
        }
        renderConferences(filtered);
    }

    function renderConferences(list) {
        listContainer.innerHTML = '';
        list.forEach(conf => {
            const tile = document.createElement('div');
            tile.className = 'tile';
            const dateStr = conf.date === conf.dateFin ? formatDate(conf.date) : `Du ${formatDate(conf.date)} au ${formatDate(conf.dateFin)}`;

            tile.innerHTML = `
                <div class="tile-header">
                    <div class="tile-header-main">
                        <span class="tile-category">${conf.categorie}</span>
                        <span class="tile-title">${conf.titre}</span>
                        <div class="tile-location-preview">
                            <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                            <span>${conf.lieu}</span>
                        </div>
                    </div>
                    <div class="tile-icon">
                        <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"></path></svg>
                    </div>
                </div>
                <div class="tile-content">
                    <div class="info-row">
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                        <span>${dateStr}</span>
                    </div>
                    ${conf.heure ? `
                    <div class="info-row">
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        <span>${conf.heure}</span>
                    </div>
                    ` : ''}
                    <p class="tile-description">${conf.description}</p>
                    <div class="tile-actions">
                        <a href="${conf.lien}" class="tile-link" target="_blank">Site de l'événement</a>
                    </div>
                </div>
            `;

            tile.querySelector('.tile-header').addEventListener('click', () => {
                tile.classList.toggle('expanded');
            });

            listContainer.appendChild(tile);
        });
    }

    function formatDate(dateString) {
        const options = { day: 'numeric', month: 'long', year: 'numeric' };
        return new Date(dateString).toLocaleDateString('fr-FR', options);
    }

    initFilters();
    renderConferences(conferences);
});

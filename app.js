document.addEventListener('DOMContentLoaded', () => {
    const conferences = [
    {
        "id": 1,
        "titre": "93e Congrès de l'Acfas (UQAM)",
        "date": "2026-05-11",
        "dateFin": "2026-05-15",
        "lieu": "Montréal (UQAM)",
        "categorie": "Sciences Sociales",
        "description": "Cohésion sociale, lien social et participation démocratique.",
        "lien": "https://www.acfas.ca"
    },
    {
        "id": 2,
        "titre": "Salon de l'immigration et de l'intégration (SIIQ)",
        "date": "2026-05-27",
        "dateFin": "2026-05-28",
        "lieu": "Montréal",
        "categorie": "Intégration Interculturelle",
        "description": "Législation en immigration et intégration au marché du travail.",
        "lien": "https://salonimmigration.com"
    },
    {
        "id": 3,
        "titre": "Colloque international du CELAT 2026",
        "date": "2026-06-15",
        "dateFin": "2026-06-17",
        "lieu": "Montréal",
        "categorie": "Politique et identité nationale",
        "description": "Identité québécoise contemporaine et muséologie de l'appartenance.",
        "lien": "https://celat.ca"
    },
    {
        "id": 4,
        "titre": "ICGPP : Governance and Public Policy",
        "date": "2026-08-14",
        "dateFin": "2026-08-14",
        "lieu": "Montréal",
        "categorie": "Gouvernance collaborative & concertation",
        "description": "Gouvernance multi-acteurs et coordination interinstitutionnelle.",
        "lien": "https://researchfoundation.net"
    }
];

    const listContainer = document.getElementById('conferences-list');
    const filtersContainer = document.getElementById('filters-container');
    const updateBtn = document.getElementById('update-btn');
    const updateModal = document.getElementById('update-modal');
    const closeModal = document.getElementById('close-modal');

    // -- GESTION DES FILTRES --
    function initFilters() {
        const categories = ['Tous', ...new Set(conferences.map(c => c.categorie))];
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
        if (category === 'Tous') {
            renderConferences(conferences);
        } else {
            const filtered = conferences.filter(c => c.categorie === category);
            renderConferences(filtered);
        }
    }

    // -- AGENDA GOOGLE --
    function generateGoogleCalendarUrl(conf) {
        const baseUrl = 'https://www.google.com/calendar/render?action=TEMPLATE';
        const title = encodeURIComponent(conf.titre);
        const details = encodeURIComponent(`${conf.description}\n\nLien: ${conf.lien}`);
        const location = encodeURIComponent(conf.lieu);
        const startDate = conf.date.replace(/-/g, '');
        const endDay = new Date(conf.dateFin);
        endDay.setDate(endDay.getDate() + 1);
        const endDate = endDay.toISOString().split('T')[0].replace(/-/g, '');
        return `${baseUrl}&text=${title}&details=${details}&location=${location}&dates=${startDate}/${endDate}`;
    }

    // -- RENDU DES TUILES --
    function renderConferences(list) {
        listContainer.innerHTML = '';
        list.forEach(conf => {
            const tile = document.createElement('div');
            tile.className = 'tile';
            const dateStr = conf.date === conf.dateFin ? formatDate(conf.date) : `Du ${formatDate(conf.date)} au ${formatDate(conf.dateFin)}`;
            const googleUrl = generateGoogleCalendarUrl(conf);

            tile.innerHTML = `
                <div class="tile-header">
                    <span class="tile-category">${conf.categorie}</span>
                    <span class="tile-title">${conf.titre}</span>
                    <div class="tile-icon">
                        <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"></path></svg>
                    </div>
                </div>
                <div class="tile-content">
                    <div class="info-row">
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                        <span>${dateStr}</span>
                    </div>
                    <div class="info-row">
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                        <span>${conf.lieu}</span>
                    </div>
                    <p class="tile-description">${conf.description}</p>
                    <div class="tile-actions">
                        <a href="${conf.lien}" class="tile-link" target="_blank">Site de l'événement</a>
                        <a href="${googleUrl}" class="btn-google" target="_blank">Ajouter à mon agenda</a>
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

    // -- MODAL MISE À JOUR --
    updateBtn.onclick = () => updateModal.classList.add('active');
    closeModal.onclick = () => {
        updateModal.classList.remove('active');
        location.reload(); // Simule le rafraîchissement des données
    };

    // Fermer les modales en cliquant à l'extérieur
    window.onclick = (event) => {
        if (event.target == updateModal) updateModal.classList.remove('active');
    };

    initFilters();
    renderConferences(conferences);
});

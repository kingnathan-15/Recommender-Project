async function addRecommendationCard(result) {
    const jsonElements = [];
    const resultElement = [];

    result.similar_anime_ids.forEach((id, i) => {
        resultElement[i] = result.similar_anime_ids[i];
        
    });

    for (const id of resultElement) {
        console.log(id);
        const response = await fetch(`/api/anime/${id}`);
                            
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
                            
        jsonElements[anime_id] = await response.json();
        console.log('Received anime details:', jsonElements[anime_id]);
    }

    let count = 1;

    for (const anime_id in jsonElements) {
        const anime = jsonElements[anime_id];
        const container = document.getElementById(`recommendationsList`);
        const card = document.createElement('div');
        card.classList.add('card', 'mb-3', 'w-50', 'h-50');
        card.id = `RecommendationCard_${anime_id}`;

        const img = document.createElement('img');
        img.src = anime.main_picture?.medium || '';
        img.className = 'card-img-top';
        img.alt = anime.title || 'No image available';

        const cardBody = document.createElement('div');
        cardBody.className = 'card-body';

        const title = document.createElement('h5');
        title.className = 'card-title';
        title.innerText = anime.title || 'No Title';

        const body = document.createElement('p');
        body.className = 'card-text';
        body.innerText = anime.synopsis || 'N/A';

        cardBody.appendChild(title);
        cardBody.appendChild(body);
        card.appendChild(img);
        card.appendChild(cardBody);

        container.appendChild(card);
        count++;
    }
}
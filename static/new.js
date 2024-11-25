document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    const resultsDiv = document.getElementById('results');
    const searchButton = document.getElementById('searchButton');
    const buttonText = document.querySelector('.button-text');
    const loader = document.querySelector('.loader');
    const suggestionsUl = document.getElementById('suggestions');

    // Fetch suggestions from the server
    async function fetchSuggestions(query) {
        try {
            const response = await fetch(`/get_suggestions/?q=${encodeURIComponent(query)}`);
            if (!response.ok) throw new Error('Failed to fetch suggestions');
            const suggestions = await response.json();
            return suggestions;
        } catch (error) {
            console.error('Error fetching suggestions:', error);
            return [];
        }
    }

    // Display suggestions in the dropdown
    function displaySuggestions(suggestions) {
        suggestionsUl.innerHTML = ''; // Clear previous suggestions
        if (suggestions.length > 0) {
            suggestions.forEach(suggestion => {
                const li = document.createElement('li');
                li.textContent = suggestion;
                li.addEventListener('click', () => {
                    searchInput.value = suggestion; // Set the clicked suggestion in the input
                    suggestionsUl.style.display = 'none'; // Hide suggestions
                });
                suggestionsUl.appendChild(li);
            });
            suggestionsUl.style.display = 'block'; // Show suggestions
        } else {
            suggestionsUl.style.display = 'none'; // Hide suggestions if none available
        }
    }

    // Handle input event for fetching suggestions
    searchInput.addEventListener('input', async (e) => {
        const inputValue = e.target.value.trim().toLowerCase();
        if (inputValue.length > 2) {
            const suggestions = await fetchSuggestions(inputValue);
            displaySuggestions(suggestions);
        } else {
            suggestionsUl.style.display = 'none';
        }
    });

    // Handle form submission
    // searchForm.addEventListener('submit', function (e) {
    //     e.preventDefault();

    //     const query = searchInput.value.trim();
    //     if (!query) {
    //         resultsDiv.innerHTML = '<p class="error">Iltimos, qidiruv uchun biror so\'rov kiriting!</p>';
    //         return;
    //     }

    //     // Show loader and disable button during request
    //     buttonText.style.display = 'none';
    //     loader.style.display = 'inline-block';
    //     searchButton.disabled = true;

    //     // Perform search query
    //     fetch(`/qidirish/?q=${encodeURIComponent(query)}`)
    //         .then(response => {
    //             if (!response.ok) {
    //                 throw new Error(`Server xatosi: ${response.statusText}`);
    //             }
    //             return response.json();
    //         })
    //         .then(data => {
    //             if (data.error) {
    //                 resultsDiv.innerHTML = `<p class="error">${data.error}</p>`;
    //             } else {
    //                 const mashinalarHTML = data.mashinalar.map(mashina => `
    //             <li>
    //                 <strong>Raqam:</strong> ${mashina.raqam}<br>
    //                 <strong>Nomi:</strong> ${mashina.nomi}<br>
    //                 <strong>Rangi:</strong> ${mashina.rangi}<br>
    //                 <strong>Ishlab chiqarilgan yili:</strong> ${mashina.ishlab_chiqarilgan_yili}
    //             </li>
    //         `).join('');

    //                 resultsDiv.innerHTML = `
    //             <h3>Haydovchi: ${data.haydovchi}</h3>
    //             <ul>${mashinalarHTML}</ul>
    //         `;
    //             }
    //         })
    //         .catch(error => {
    //             resultsDiv.innerHTML = `<p class="error">Xatolik yuz berdi: ${error.message}</p>`;
    //         });

    // });

    // Close suggestions when clicking outside
    document.addEventListener('click', (e) => {
        if (e.target !== searchInput && e.target !== suggestionsUl) {
            suggestionsUl.style.display = 'none';
        }
    });
});

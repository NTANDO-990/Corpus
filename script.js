const SEARCH_API_URL = 'http://127.0.0.1:5000/api/translations';
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

let allWords = [];

// Fetch all words once when the page loads
async function loadWords() {
    try {
        const response = await fetch(SEARCH_API_URL);
        if (!response.ok) throw new Error('Failed to fetch words');
        allWords = await response.json();
    } catch (error) {
        searchResults.innerHTML = '<p style="color:red;">Could not load words.</p>';
    }
}

// Filter and display results as user types
searchInput.addEventListener('input', function() {
    const query = searchInput.value.trim().toLowerCase();
    searchResults.innerHTML = '';
    if (!query) return;

    // Search across all columns for a match
    const matches = allWords.filter(item =>
        Object.values(item).some(val =>
            val && val.toString().toLowerCase().includes(query)
        )
    );

    if (matches.length === 0) {
        searchResults.innerHTML = '<p>No results found.</p>';
        return;
    }

    // Display results
    matches.slice(0, 10).forEach(item => {
        const row = document.createElement('div');
        row.style.padding = '8px 0';
        row.style.borderBottom = '1px solid #eee';
        row.innerHTML = Object.entries(item)
            .map(([lang, word]) => `<strong>${lang}:</strong> ${word}`)
            .join(' &nbsp; | &nbsp; ');
        searchResults.appendChild(row);
    });
});

// Load words on page load
loadWords();
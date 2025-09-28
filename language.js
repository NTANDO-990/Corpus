const API_URL = 'http://127.0.0.1:5000/api/translations';

const sourceSelect = document.getElementById('sourceLang');
const targetSelect = document.getElementById('translatedLang');
const inputText = document.getElementById('inputText');
const outputText = document.getElementById('outputText');
const translateBtn = document.getElementById('translateButton');

async function fetchTranslations() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok)
            throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();

        // Get selected columns and input
        const sourceCol = sourceSelect.value.charAt(0).toUpperCase() + sourceSelect.value.slice(1);
        const targetCol = targetSelect.value.charAt(0).toUpperCase() + targetSelect.value.slice(1);
        const input = inputText.value.trim();

        // Find translation and display it
        const match = data.find(item => item[sourceCol] && item[sourceCol].toLowerCase() === input.toLowerCase());
        if (match && match[targetCol]) {
            outputText.value = match[targetCol];
        } else {
            outputText.value = 'Translation not found.';
        }
    } catch (error) {
        outputText.value = 'Sorry, could not load translations. Please try again later.';
        console.error('There was a problem with the fetch operation:', error);
    }
}

translateBtn.addEventListener('click', fetchTranslations);

const SEARCH_API_URL = 'http://127.0.0.1:5000/api/translations';
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');
const container = document.querySelector('.container');

let allWords = [];

// fetch the words as soon as the page loads
async function loadWords() {
    try {
        const response = await fetch(SEARCH_API_URL);
        if (!response.ok) throw new Error('Error');
        allWords = await response.json();
    } catch (error) {    
        searchResults.innerHTML = '<p style="color:red;">Could not load words.</p>';
    }
}
loadWords();

window.onload = function() {
    const username = localStorage.getItem('username');
    if (username) {
        document.getElementById("user").textContent = `Welcome, ${username}!`;
    }
};
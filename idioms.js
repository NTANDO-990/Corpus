const API_URL = 'http://127.0.0.1:5000/api/idioms'
const idiomsContainer = document.getElementById('idiomsContainer')

async function fetchIdioms(){
    try{
        const response = await fetch(API_URL);
        if(!response.ok){
            throw new Error(`Error! status: ${response.status}`); //logical response if the response id not ok
        }
        const data = await response.json();

        idiomsContainer.innerHTML = '';
        data.forEach(idiom => {
            const idiomDiv = document.createElement('div'); //create a new element to place the idioms
            idiomDiv.className = 'idiom_entry';
            idiomDiv.textContent = `${idiom['Zulu']} -> ${idiom['English']} (${idiom['Meaning']})`;
            idiomsContainer.appendChild(idiomDiv);
        });
    } catch (error){
        console.error('Error fetching idioms:', error);
        idiomsContainer.innerHTML = '<p style="color:red;">Could not load idioms.</p>';
    }
}

fetchIdioms();
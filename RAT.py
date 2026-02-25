// 1. Select DOM elements
const form = document.getElementById('app-form');
const dashboard = document.getElementById('dashboard');

// 2. Load data from LocalStorage safely
let apps = JSON.parse(localStorage.getItem('rat_data')) || [];

// 3. Function to save and refresh UI
const updateUI = () => {
    localStorage.setItem('rat_data', JSON.stringify(apps));
    renderCards();
};

// 4. Function to build the HTML cards
const renderCards = () => {
    // Clear current lists
    document.querySelectorAll('.list').forEach(list => list.innerHTML = '');

    apps.forEach((app, index) => {
        const listContainer = document.querySelector(`#${app.status}-col .list`);
        if (!listContainer) return; // Safety check

        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <strong>${app.company}</strong><br>
            <small>${app.role}</small><br>
            <button onclick="deleteApp(${index})" style="color:red; border:none; background:none; cursor:pointer;">× Remove</button>
        `;
        listContainer.appendChild(card);
    });
};

// 5. Add new application
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const newApp = {
        company: document.getElementById('company').value,
        role: document.getElementById('role').value,
        status: document.getElementById('status').value
    };
    apps.push(newApp);
    form.reset();
    updateUI();
});

// 6. Delete application (Global function for the button)
window.deleteApp = (index) => {
    apps.splice(index, 1);
    updateUI();
};

// Initial Render
renderCards();

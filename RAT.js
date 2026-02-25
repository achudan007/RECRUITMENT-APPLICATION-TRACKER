document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('app-form');
    let applications = JSON.parse(localStorage.getItem('rat_apps')) || [];

    const render = () => {
        // Clear columns
        document.querySelectorAll('.list').forEach(list => list.innerHTML = '');

        applications.forEach((app, index) => {
            const card = document.createElement('div');
            card.className = `card ${app.status}`;
            card.innerHTML = `
                <h3>${app.company}</h3>
                <p>${app.role}</p>
                <button onclick="deleteApp(${index})">Delete</button>
            `;
            
            const targetCol = document.querySelector(`#${app.status}-col .list`);
            if (targetCol) targetCol.appendChild(card);
        });
        
        localStorage.setItem('rat_apps', JSON.stringify(applications));
    };

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const newApp = {
            company: document.getElementById('company').value,
            role: document.getElementById('role').value,
            status: document.getElementById('status').value,
            date: new Date().toLocaleDateString()
        };
        applications.push(newApp);
        form.reset();
        render();
    });

    window.deleteApp = (index) => {
        applications.splice(index, 1);
        render();
    };

    render(); // Initial load
});

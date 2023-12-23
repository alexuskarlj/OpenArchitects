document.addEventListener('DOMContentLoaded', function() {
    fetchRecentLogins();
    fetchRecentDashboardViews();
    fetchDashboardStats(); 
});

function insertRowInTable(tableBodyId, rowData) {
    const tableBody = document.getElementById(tableBodyId);
    const row = document.createElement('tr');
    rowData.forEach(cellData => {
        const cell = document.createElement('td');
        cell.textContent = cellData;
        row.appendChild(cell);
    });
    tableBody.appendChild(row);
}

function fetchRecentLogins() {
    fetch('/recent_logins')
        .then(response => response.json())
        .then(data => {
            const loginsTableBody = document.getElementById('logins-tbody');
            loginsTableBody.innerHTML = ''; // Clear existing table data
            data.forEach(login => {
                // Create a new row element
                const newRow = document.createElement('tr');

                // Create and append table data cells with styles
                const nameCell = document.createElement('td');
                nameCell.textContent = login.name;
                nameCell.style.color = '#007BFF'; // Set text color
                newRow.appendChild(nameCell);

                const organizationCell = document.createElement('td');
                organizationCell.textContent = login.organization;
                newRow.appendChild(organizationCell);

                const timestampCell = document.createElement('td');
                timestampCell.textContent = login.timestamp;
                newRow.appendChild(timestampCell);

                // Append the new row to the table body
                loginsTableBody.appendChild(newRow);
            });
        })
        .catch(error => console.error('Error:', error));
}


function fetchRecentDashboardViews() {
    fetch('/recent_dashboard_views')
        .then(response => response.json())
        .then(data => {
            const viewsTableBody = document.getElementById('views-tbody');
            viewsTableBody.innerHTML = ''; // Clear existing table data
            data.forEach(view => {
                // Create a new row element
                const newRow = document.createElement('tr');

                // Create and append table data cells with styles
                const nameCell = document.createElement('td');
                nameCell.textContent = view.name;
                nameCell.style.color = '#007BFF'; // Set text color
                newRow.appendChild(nameCell);

                const organizationCell = document.createElement('td');
                organizationCell.textContent = view.organization;
                newRow.appendChild(organizationCell);

                const dashboardCell = document.createElement('td');
                dashboardCell.textContent = view.dashboard;
                dashboardCell.style.color = '#007BFF'; // Set text color
                newRow.appendChild(dashboardCell);

                const timestampCell = document.createElement('td');
                timestampCell.textContent = view.timestamp;
                newRow.appendChild(timestampCell);

                // Append the new row to the table body
                viewsTableBody.appendChild(newRow);
            });
        })
        .catch(error => console.error('Error:', error));
}

function fetchDashboardStats() {
    fetch('/dashboard_stats')
        .then(response => response.json())
        .then(data => {
            // Update the Dashboard card with the actual count
            document.querySelector('#data-cards .data-card:nth-child(1) h3').textContent = data.dashboard_count;
            
            // Update the Users card with the actual count
            document.querySelector('#data-cards .data-card:nth-child(2) h3').textContent = data.user_count;
            
            // Update the Organizations / Schools card with the actual count
            const orgSchoolsCount = `${data.org_count} / ${data.org_count}`; // Assuming the same count for both
            document.querySelector('#data-cards .data-card:nth-child(3) h3').textContent = orgSchoolsCount;
            
            // Update the Logins / Views card with the actual count
            const loginsViewsCount = `${data.login_count} / ${data.view_count}`;
            document.querySelector('#data-cards .data-card:nth-child(4) h3').textContent = loginsViewsCount;
        })
        .catch(error => console.error('Error:', error));
}
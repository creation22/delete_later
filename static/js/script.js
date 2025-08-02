console.log("🔒 Incident Response Tool Loaded Successfully");

// Auto-hide flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
    });
});

// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(function(field) {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#dc3545';
                } else {
                    field.style.borderColor = '#28a745';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });
});

// Add confirmation for status changes
document.addEventListener('DOMContentLoaded', function() {
    const statusForms = document.querySelectorAll('form[action*="update-status"]');
    statusForms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            const status = form.querySelector('input[name="status"], select[name="status"]').value;
            if (!confirm(`Are you sure you want to change the status to "${status}"?`)) {
                e.preventDefault();
            }
        });
    });
});
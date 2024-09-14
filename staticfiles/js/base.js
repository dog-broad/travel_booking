document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.fade-in-up').forEach((element) => {
        element.style.opacity = '0';
        element.style.animation = 'none';
        element.offsetHeight; // Trigger reflow
        element.style.animation = null;
    });
});
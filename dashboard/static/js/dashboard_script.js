document.addEventListener('DOMContentLoaded', () => {
    // Form fields ka subtle focus effect
    document.querySelectorAll('input, textarea').forEach(el => {
        el.addEventListener('focus', () => {
            el.style.border = "2px solid #FFCC00";
        });
        el.addEventListener('blur', () => {
            el.style.border = "2px solid #eee";
        });
    });

    // Table rows ke liye entry animation
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach((row, index) => {
        row.style.animation = `fadeInUp 0.5s ease forwards ${index * 0.1}s`;
    });
});
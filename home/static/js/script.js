document.addEventListener("DOMContentLoaded", () => {
    // Entrance Animation
    const card = document.querySelector(".form-card");
    card.style.opacity = "0";
    card.style.transition = "0.8s ease-out";
    setTimeout(() => { card.style.opacity = "1"; }, 100);

    // Click Effect
    document.querySelectorAll('button').forEach(btn => {
        btn.onclick = () => btn.style.transform = "scale(0.98)";
    });
});
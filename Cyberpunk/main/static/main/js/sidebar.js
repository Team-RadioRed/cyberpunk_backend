function toggleDropdown(id) {
    var content = document.getElementById(id);
    var arrow = content.previousElementSibling.querySelector('.arrow');

    // Переключаем видимость контента
    if (content.style.display === "block") {
        content.style.display = "none";
        arrow.classList.remove("arrow-down");
    } else {
        content.style.display = "block";
        arrow.classList.add("arrow-down");
    }
}
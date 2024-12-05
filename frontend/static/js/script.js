function toggleMenu() {
    var navLinks = document.getElementById('nav-links');
    navLinks.classList.toggle('show-menu');
}

function showSuggestions(str) {
    if (str.length == 0) {
        document.getElementById("suggestions").innerHTML = "";
        return;
    }
    fetch(`/authors/suggestions?q=${str}`)
        .then(response => response.json())
        .then(data => {
            let suggestions = data.map(author => `<a href="/authors/${author.pk}" class="author-name">${author.first_name} ${author.last_name}</a>`).join('');
            document.getElementById("suggestions").innerHTML = suggestions;
        });
}
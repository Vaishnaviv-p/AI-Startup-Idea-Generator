function toggleTheme() {

    document.body.classList.toggle("light-mode");

    const button = document.getElementById("themeButton");

    if (document.body.classList.contains("light-mode")) {

        button.innerHTML = "🌙 Switch to Dark Mode";

        localStorage.setItem("theme", "light");

    } else {

        button.innerHTML = "☀️ Switch to Light Mode";

        localStorage.setItem("theme", "dark");

    }

}

window.onload = function () {

    const theme = localStorage.getItem("theme");

    const button = document.getElementById("themeButton");

    if (theme === "light") {

        document.body.classList.add("light-mode");

        button.innerHTML = "🌙 Switch to Dark Mode";

    } else {

        button.innerHTML = "☀️ Switch to Light Mode";

    }

}
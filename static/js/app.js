const menuButton = document.querySelector(".menu-toggle");
        const navLinks = document.querySelector("#nav-links");
        const themeToggle = document.querySelector("#theme-toggle");
        const contactForm = document.querySelector("#contact-form");
        const formNote = document.querySelector("#form-note");

        menuButton.addEventListener("click", () => {
            const isOpen = navLinks.classList.toggle("is-open");
            menuButton.setAttribute("aria-expanded", String(isOpen));
        });

        navLinks.addEventListener("click", (event) => {
            if (event.target.tagName === "A") {
                navLinks.classList.remove("is-open");
                menuButton.setAttribute("aria-expanded", "false");
            }
        });

        themeToggle.addEventListener("click", () => {
            document.body.classList.toggle("light-mode");
            themeToggle.textContent = document.body.classList.contains("light-mode") ? "Light" : "Dark";
            localStorage.setItem("portfolio-theme", document.body.classList.contains("light-mode") ? "light" : "dark");
        });

        contactForm.addEventListener("submit", (event) => {
            if (!contactForm.getAttribute("action")) {
                event.preventDefault();
                formNote.style.display = "block";
                contactForm.reset();
            }
        });

        document.querySelectorAll(".reveal").forEach((element, index) => {
            element.style.setProperty("--delay", `${Math.min(index % 5, 4) * 80}ms`);
        });

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    entry.target.closest(".section")?.classList.add("is-active");
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.14 });

        document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));

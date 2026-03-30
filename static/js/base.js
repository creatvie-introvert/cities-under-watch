function initAnnouncementBanner() {
    const announcementBanner = document.querySelector("[data-announcement-banner]");
    const announcementCloseButton = document.querySelector("[data-announcement-close]");

    if (!announcementBanner || !announcementCloseButton) {
        return;
    }

    announcementCloseButton.addEventListener("click", () => {
        announcementBanner.style.display = "none";
    });
}

function initMobileMenu() {
    const menuToggleButton = document.querySelector("[data-mobile-menu-toggle]");
    const mobileMenu = document.querySelector("[data-mobile-menu]");

    if (!menuToggleButton || !mobileMenu) {
        return
    }

    function closeMenu() {
        menuToggleButton.setAttribute("aria-expanded", "false");
        mobileMenu.hidden = true
    }

    function openMenu() {
        menuToggleButton.setAttribute("aria-expanded", "true");
        mobileMenu.hidden = false
    }

    menuToggleButton.addEventListener("click", () => {
        const isExpanded = menuToggleButton.getAttribute("aria-expanded") === "true";

        if (isExpanded) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeMenu();
        }
    });
}

initAnnouncementBanner();
initMobileMenu();

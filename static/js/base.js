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

function initCatalogueFilterToggle() {
    const filterToggleButton = document.querySelector("[data-filter-toggle]");
    const filterPanel = document.querySelector("[data-filter-panel]");

    if (!filterToggleButton || !filterPanel) {
        return;
    }

    console.log("Catalogue filter toggle initialised");

    function openFilterPanel() {
        filterToggleButton.setAttribute("aria-expanded", "true");
        filterPanel.hidden = false;
    }

    function closeFilterPanel() {
        filterToggleButton.setAttribute("aria-expanded", "false");
        filterPanel.hidden = true;
    }

    filterToggleButton.addEventListener("click", () => {
        const isExpanded = filterToggleButton.getAttribute("aria-expanded") === "true";

        if (isExpanded) {
            closeFilterPanel();
        }
        else {
            openFilterPanel();
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeFilterPanel();
        }
    });
}

initAnnouncementBanner();
initMobileMenu();
initCatalogueFilterToggle();
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

function initCatalogueAutoFilterSubmit() {
    const filterForm = document.querySelector("[data-auto-filter-form]");
    const filterInputs = document.querySelectorAll("[data-auto-filter-input]");

    if (!filterForm || !filterInputs.length) {
        return;
    }

    filterInputs.forEach((input) => {
        input.addEventListener("change", () => {
            filterForm.submit();
        });
    });
}

function initProductGallery() {
    const mainImage = document.querySelector("[data-product-main-image]");
    const thumbnailButtons = document.querySelectorAll("[data-product-thumbnail]");

    if (!mainImage || !thumbnailButtons.length) {
        return;
    }

    thumbnailButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const newImageSrc = button.getAttribute("data-image-src");
            const newImageAlt = button.getAttribute("data-image-alt");

            if (!newImageSrc) {
                return;
            }

            mainImage.src = newImageSrc;
            mainImage.alt = newImageAlt || "";

            thumbnailButtons.forEach((thumbnailButton) => {
                thumbnailButton.classList.remove("is-active");
                thumbnailButton.setAttribute("aria-pressed", "false");
            });

            button.classList.add("is-active");
            button.setAttribute("aria-pressed", "true");
        });
    });
}

function initCollectionNarrative() {
    const narrative = document.querySelector("[data-collection-narrative]");
    const panels = document.querySelectorAll("[data-narrative-panel]");
    const triggers = document.querySelectorAll("[data-narrative-trigger]")

    if (!narrative || !panels.length || !triggers.length) {
        return;
    }

    function setActivePanel(activePanel) {
        panels.forEach((panel) => {
            const trigger = panel.querySelector("[data-narrative-trigger]");

            panel.classList.remove("collection-narrative__panel--active");
            panel.classList.add("collection-narrative__panel--collapsed");

            if (trigger) {
                trigger.setAttribute("aria-expanded", "false");
            }
        });

        const activeTrigger = activePanel.querySelector("[data-narrative-trigger]");
        const activeIndex = Array.from(panels).indexOf(activePanel) + 1;

        activePanel.classList.remove("collection-narrative__panel--collapsed");
        activePanel.classList.add("collection-narrative__panel--active");

        narrative.setAttribute("data-active-panel", String(activeIndex));

        if (activeTrigger) {
            activeTrigger.setAttribute("aria-expanded", "true");
        }
    }

    const initialActivePanel = narrative.querySelector(".collection-narrative__panel--active") || panels[0];

    setActivePanel(initialActivePanel);

    triggers.forEach((trigger) => {
        trigger.addEventListener("click", () => {
            const panel = trigger.closest("[data-narrative-panel]");

            if (!panel) {
                return;
            }

            setActivePanel(panel);
        });
    });
}

function initToasts() {
    const toasts = document.querySelectorAll("[data-toast");

    if (!toasts.length) {
        return;
    }

    function hideToast(toast) {
        toast.classList.add("is-hiding");

        window.setTimeout(() => {
            toast.remove();
        }, 250);
    }

    toasts.forEach((toast) => {
        const closeButton = toast.querySelector("[data-toast-close");

        if (closeButton) {
            closeButton.addEventListener("click", () => {
                hideToast(toast);
            });
        }

        window.setTimeout(() => {
            hideToast(toast);
        }, 4000);
    });
}

initAnnouncementBanner();
initMobileMenu();
initCatalogueFilterToggle();
initCatalogueAutoFilterSubmit();
initProductGallery();
initCollectionNarrative();
initToasts();
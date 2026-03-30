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

initAnnouncementBanner();

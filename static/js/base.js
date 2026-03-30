const announcementBanner = document.querySelector("[data-announcement-banner]");
const announcementCloseButton = document.querySelector("[data-announcement-close]");

if (announcementBanner && announcementCloseButton) {
    announcementCloseButton.addEventListener("click", () => {
        announcementBanner.style.display = "none"
    })
}
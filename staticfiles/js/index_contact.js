const contactModal = new bootstrap.Modal(document.getElementById("contactModal"));
const contactButton = document.getElementsByClassName("contact-me");

/**
 * Initializes contact form modal for the provide contact buttons.
 * 
 * For each button in the `contactButtons` array:
 * - On click, contact modal ('contactModal') is displayed 
 * for the user to enter required form details
 */
for (let button of contactButton) {
    button.addEventListener("click", (e) => {
        contactModal.show();
    });
}

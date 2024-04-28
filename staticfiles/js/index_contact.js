const contactModal = new bootstrap.Modal(document.getElementById("contactModal"));
const contactButton = document.getElementsByClassName("contact-me");
const contactConfirm = document.getElementById("contactConfirm");

for (let button of contactButton) {
    button.addEventListener("click", (e) => {
        contactModal.show()
    })
}
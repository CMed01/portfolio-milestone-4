const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes delete functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` array:
 * - On click, associated comment ID is retrieved.
 * - href for 'deleteConfirm' updated to the correct endpoint -
 *  `delete_comment/${commentId}`
 * - Delete confirmation modal ('deleteModal') is displayed 
 * for the user to confirm
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let workoutcommentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${workoutcommentId}`;
        deleteModal.show()
    })

}
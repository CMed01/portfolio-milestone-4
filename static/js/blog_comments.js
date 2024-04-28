const editButtons = document.getElementsByClassName("btn-edit");
const blogCommentText = document.getElementById("id_body");
const blogCommentForm = document.getElementById("blogcommentForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` array:
 * - On click, associated comment ID is retrieved.
 * - Content of the corresponding comment is stored.
 * - Input/text area of `blogCommentText` populated with editable comment.
 * - Subite button text amended to 'Update'
 * - Form's action attribute set to the `edit_comment/{commentId}`.
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        blogCommentText.value = commentContent;
        submitButton.innerText = "Update";
        blogCommentForm.setAttribute("action", `edit_comment/${commentId}`);
    })
}

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
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show()
    })

}

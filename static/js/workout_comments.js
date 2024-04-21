const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * 
 */

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let workoutcommentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${workoutcommentId}`;
        deleteModal.show()
    })

}
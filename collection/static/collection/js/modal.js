import { createCollection } from "./collectionOperations.js";

const modal = document.querySelectorAll('#modal');
const openModalBtn = document.querySelectorAll("[data-modal-target]");
const closeModalBtn = document.querySelectorAll("[data-close-button]");
const overlay = document.getElementById("overlay");
const modalCreatePost = document.getElementById("modal-create-post");


openModalBtn.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget);
        openModal(modal);
    });
});

closeModalBtn.forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('#modal');
        closeModal(modal);
    });
});

overlay.addEventListener('click', () => {
    const modal = document.querySelector('#modal');
    closeModal(modal);
});

modalCreatePost.addEventListener('click', () => {
    const title = $("#title-input").val();
    const content = $("#content-input").val();

    if (title == "" || content == "") {
        console.log('title val or desc val is empty')
        if ($("#field-error").length >  0) {
            $("#field-error").remove()
        }
        $("#modal-cta").prepend(`<p id="field-error" class="text-lg py-2 font-base text-rose-500">Please fill the empty fields!</p>`);
    } else {
        console.log("REACHED POST AJAX");

        $.post({
            // Current url: collection/forum/
            url: 'items/add/',
            type: 'post',
            data: {
                'title': title,
                'content': content,
            },
            success: [createCollection, function () { console.log ("post success")}],
        });


        // Clear input box values
        $("#title-input").val("")
        $("#content-input").val("")
        $("#field-error").remove()

        // Close modal
        const modal = modalCreatePost.closest("#modal");
        closeModal(modal)
    }
})   
    
// Helper functions
function openModal(modal) {
    if (modal == null) {
        return;
    }
    
    modal.classList.remove('scale-0');
    modal.classList.add('scale-100');

    overlay.classList.remove('opacity-0');
    overlay.classList.add('opacity-50');
    overlay.classList.add('z-10');
    overlay.classList.add('pointer-events-auto');
}

function closeModal(modal) {
    if (modal == null) {
        return;
    }

    modal.classList.remove('scale-100');
    modal.classList.add('scale-0');

    overlay.classList.remove('z-10');
    overlay.classList.remove('opacity-50');
    overlay.classList.remove('pointer-events-auto');
    overlay.classList.add('opacity-0');
    overlay.classList.add('pointer-events-none');

    const fieldError = document.querySelector("#field-error");
    if (fieldError !== null) {
        fieldError.remove();
    }
}
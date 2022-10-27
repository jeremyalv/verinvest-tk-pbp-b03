const modal = document.querySelectorAll('#modal');
const openModalBtn = document.querySelectorAll("[data-modal-target]");
const closeModalBtn = document.querySelectorAll("[data-close-button]");
const overlay = document.getElementById("overlay");
const modalAddTask = document.getElementById("modal-add-task");


openModalBtn.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget);
        openModal(modal);
    });
});

closeModalBtn.forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('#modal');
        console.log(modal);
        closeModal(modal);
    });
});

overlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('#modal.active');
    modals.forEach(modal => {
        closeModal(modal);
    });
});

modalAddTask.addEventListener('click', () => {
    const titleVal = $("#title-input").val();
    const descVal = $("#description-input").val();

    if (titleVal == "" || descVal == "") {
        if ($("#field-error").length >  0) {
            $("#field-error").remove()
        }
        $("#modal-cta").prepend(`<p id="field-error" class="text-lg py-2 font-base text-rose-500">Please fill the empty fields!</p>`);
    } else {
        $.post({
            url: 'add/',
            type: 'post',
            data: {
                'title': titleVal,
                'description': descVal,
            },
            success: [createSections, loadTasksList],
        });


        // Clear input box values
        $("#title-input").val("")
        $("#description-input").val("")
        $("#field-error").remove()

        // Close modal
        const modal = modalAddTask.closest("#modal.active");
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
    overlay.classList.add('pointer-events-auto');
}

function closeModal(modal) {
    if (modal == null) {
        return;
    }

    modal.classList.remove('scale-100');
    modal.classList.add('scale-0');

    overlay.classList.remove('opacity-50');
    overlay.classList.remove('pointer-events-auto');
    overlay.classList.add('opacity-0');
    overlay.classList.add('pointer-events-none');

    const fieldError = document.querySelector("#field-error");
    if (fieldError !== null) {
        fieldError.remove();
    }
}
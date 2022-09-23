const weightModal = new bootstrap.Modal(document.getElementById("modal"))

htmx.on("htmx:afterSwap", (e) => {
    if (e.detail.target.id == "modal-dialog") {
        weightModal.show()
    }
})

htmx.on("htmx:beforeSwap", (e) => {
    if (e.detail.target.id == "modal-dialog" && !e.detail.xhr.response) {
        weightModal.hide()
        e.detail.shouldSwap = false
    }
})

htmx.on("hidden.bs.modal", () => {
    document.getElementById("modal-dialog").innerHTML = ""
    location.reload()
})
const weightModal = new bootstrap.Modal(document.getElementById("animal-weight"))

htmx.on("htmx:afterSwap", (e) => {
    if (e.detail.target.id == "weight-dialog") {
        weightModal.show()
    }
})

htmx.on("htmx:beforeSwap", (e) => {
    if (e.detail.target.id == "weight-dialog" && !e.detail.xhr.response) {
        weightModal.hide()
        e.detail.shouldSwap = false
        location.reload()
    }
})

htmx.on("hidden.bs.modal", () => {
    document.getElementById("weight-dialog").innerHTML = ""
})
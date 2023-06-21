function deleteNote(noteId) {
    //sending request is done with fetch
    fetch(
        "/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
            //this reloads the window (home page) by
            //redirecting to home page
            window.location.href="/";
    })
}
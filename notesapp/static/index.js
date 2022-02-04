function deleteNote(noteId) {
  
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

  // noteData = document.getElementById("note-data");

  function updateNote() {
    document.getElementById("note-data-form").submit();
  }

  

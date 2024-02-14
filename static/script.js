$(document).ready(function() {
    $('#dragElement').draggable();
    $('#dropZone').droppable({
        drop: function(event, ui) {
            // Handle drop event here
        }
    });
});

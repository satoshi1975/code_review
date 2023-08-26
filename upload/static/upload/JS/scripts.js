const fileInput = document.getElementById("id_file");
const submitBtn = document.getElementById("upload-btn");
const errorMsg = document.getElementById("error-msg");
const resultMessage = document.getElementById("result-message");

//extension access
fileInput.addEventListener("change", function () {
  const fileName = fileInput.value;
  const fileExtension = fileName.split(".").pop().toLowerCase();

  if (fileExtension === "py") {
    submitBtn.removeAttribute("disabled");
    errorMsg.style.display = "none";
  } else {
    submitBtn.setAttribute("disabled", "true");
    errorMsg.style.display = "block";
  }
});
//send file
$(document).ready(function () {
  $("#upload-btn").click(function () {
    var formData = new FormData($("#upload-form")[0]);
    $.ajax({
      type: "POST",
      url: "/files/upload_file",
      data: formData,
      processData: false,
      contentType: false,
      success: function (data) {
        $("#upload-form").hide();
        var newText = "<span style='color: green;'>Complete</span>";
        var newFile =
          ' <button class="file-button" data-file-id="' +
          data.data.id +
          '">' +
          data.data.name +
          "</button>";
        $("#upload").html(newText);
        $("#files").append(newFile);
      },
      error: function () {
        console.log("false");
      },
    });
  });
});
//show file
$(document).ready(function () {
  $(".file-button").click(function () {
    var editor = ace.edit("file-content");
    editor.setTheme("ace/theme/twilight");
    editor.session.setMode("ace/mode/python");
    editor.setFontSize("15");
    var fileId = $(this).data("file-id");
    $.ajax({
      url: "/files/show_file/" + fileId,
      method: "GET",
      success: function (response) {
        var fileDetails = `
                    <p><a href="/files/edit_file/${fileId}">Edit</a></p>
                    <button class="delete-button" data-id="${fileId}">Delete</button>
                `;
        $("#file-detail").html(fileDetails);
        $("#file-content").html(response.file);
      },
      error: function () {
        alert("Ошибка при загрузке контента файла.");
      },
    });
  });
  $(document).on("click", ".delete-button", function () {
    var fileId = $(this).data("id");
    $("#delete-confirm-modal").fadeIn();

    $(".confirm-delete-button").click(function () {
      $.ajax({
        url: "/files/delete_file/" + fileId,
        method: "GET",
        success: function (data) {
          var $clickedButton = $(".file-button[data-file-id='" + fileId + "']");
          $clickedButton.hide();
          $("#file-content").empty();
          $("#file-detail").empty();
        },
        error: function (xhr, status, error) {
          console.error(error);
        },
      });
      $("#delete-confirm-modal").fadeOut();
    });

    $(".cancel-delete-button").click(function () {
      $("#delete-confirm-modal").fadeOut();
    });
  });
});

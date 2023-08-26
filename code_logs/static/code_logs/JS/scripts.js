//вывод логов файла
$(document).on("click", ".show-log-button", function () {
  var fileId = $(this).data("id");
  $.ajax({
    url: "/logs/get_logs/" + fileId,
    method: "GET",
    success: function (data) {
      $("#logs").html(data.logs);
    },
    error: function (data) {
      $("#logs").html(data.logs);
    },
  });
});

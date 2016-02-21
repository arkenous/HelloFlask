$(window).load(init());

function init() {
  $("#button").click(function() {
    $("#hello").text("Yeah!");
  });
}

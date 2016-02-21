$(window).load(init());

function init() {
  $("#button").click(function() {
    var textData = JSON.stringify({"text":$("#input-text").val()});
    $.ajax({
      type:'POST',
      url:'/postText',
      data:textData,
      contentType:'application/json',
      success:function(data) {
        var result = JSON.parse(data.ResultSet).result;
        $("#hello").text(result);
        }
    });
    return false;
  });
}

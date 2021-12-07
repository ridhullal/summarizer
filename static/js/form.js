$(document).ready(function(){

$('#summarize-form').on('submit',function (e) {
    e.preventDefault();
     $.ajax({
      type: 'post',
      url: '/summarize',
      data: $('#summarize-form').serialize(),
      dataType:"json",
      success:function (data)
      {
          console.log(data)
        $('#output').replaceWith(data)
        window.location.hash = "#outputcount";
      }
      });
      
      
     
     });
    })

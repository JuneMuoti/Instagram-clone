$(document).ready(function(){
  $('form').submit(function(event){
    event.preventDefault()
  }) // End of submit event

})
$.ajax({
    'url':'/ajax/comments/',
    'type':'POST',
    'data':form.serialize(),
    'dataType':'json',
    'success': function(data){
      alert(data['success'])
    },
  })// END of Ajax method
  $('#id_your_comment').val('')
  
}) // End of submit event

})

$(function(){
  
    var embed = $('.youtube');
    $('.video').append(embed);

    /* click 'PLAY'  button */
    $('.pop_open').click( function() {
      // show popup background
      $('.gray_mask').show();
      // show popup 
      $('#popup').show();
      // append youtube iframe on popup
      $('.video').append(embed);
    });
 
  /* click 'CLOSE' button */
  $('.gray_mask, .close').click( function() {
    // hide popup background
    $('#popup').hide();
    // hide popup 
    $('.gray_mask').hide();
    // empty youtube iframe on popup
    $('.video').empty(); 
  }); 
  
  /* click 'popu background' */
  $('.gray_mask, .close').click( function() {
    // hide popup background
    $('#popup').hide();
    // hide popup 
    $('.gray_mask').hide();
    // empty youtube iframe on popup
    $('.video').empty(); 
  }); 
  
});
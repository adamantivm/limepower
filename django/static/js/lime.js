$('document').ready(function(){
  resetLimes();
  var sock = io.connect('/lime');
  sock.on('value', updateLimes);
  sock.on('connect',function(){
    sock.emit('connected',1);
  });
  sock.on('disconnect', resetLimes);
  $('#heart').on('click',function() {
    newval = ($('#my-status').html() == 'online') ? 0 : 1;
    updateLime( 'my-status', newval ? 'online': 'offline');
    updateHeart();
    sock.emit('changed', newval);
  });
});

/*
 Set the limes to an initial (unknown / disconnected) state
 */
function resetLimes() {
  ['her-status','my-status'].map(function(lime){
    updateLime( lime, 'unknown');
  });
}

function updateLimes( limeValues) {
  ['her-status','my-status'].map(function(lime){
    updateLime( lime, limeValues[lime] ? 'online' : 'offline');
  });
  updateHeart();
}

function updateLime( whichLime, limeText) {
  $('#'+whichLime).html( limeText);
}

function updateHeart() {
  var me = $('#my-status').html() == 'online';
  var them = $('#her-status').html() == 'online';

  var img = $('#heart');
  if (me && them) {
    img.attr('src', 'img/heart-full.png'); 
  } else if (me) {
    img.attr('src', 'img/heart-left.png'); 
  } else if (them) {
    img.attr('src', 'img/heart-right.png'); 
  } else {
    img.attr('src', 'img/heart-outline.png'); 
  }
}

$('document').ready(function(){
  resetLimes();
  var sock = io.connect('/lime');
  sock.on('value', updateLimes);
  sock.on('connect',function(){
    sock.emit('connected',1);
  });
  sock.on('disconnect', resetLimes);
  $('#heart-container').on('click',function() {
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

  if (me) {
    $('#heart-left').removeClass('transparent');
  } else {
    $('#heart-left').addClass('transparent');
  }

  if (them) {
    $('#heart-right').removeClass('transparent');
  } else {
    $('#heart-right').addClass('transparent');
  }
}

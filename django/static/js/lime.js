$('document').ready(function(){
  resetLimes();
  var sock = io.connect('/lime');
  sock.on('value', updateLimes);
  sock.on('connect',function(){
    sock.emit('connected',1);
  });
  sock.on('disconnect', resetLimes);
  $('#my-status').on('click',function() {
    newval = ($('#my-status').html() == 'online') ? 0 : 1;
    updateLime( 'my-status', newval ? 'online': 'offline');
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
}

function updateLime( whichLime, limeText) {
  $('#'+whichLime).html( limeText);
}

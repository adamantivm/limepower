function LimeCtrl($scope) {
  $scope.myStatus = false;
  $scope.theirStatus = false;

  $scope.resetStatus = function() {
    $scope.myStatus = false;
    $scope.theirStatus = false;
  };

  $scope.updateLime = function(which, text) {
    if (which == 'my-status') {
      $scope.myStatus = text;
    } else if (which == 'her-status') {
      $scope.theirStatus = text;
    }
  };

  $scope.updateLimes = function(newvalues) {
    console.log('received new lime statii:', newvalues);
    $scope.myStatus = newvalues['my-status'];
    $scope.theirStatus = newvalues['her-status'];
  };

  $scope.toggleMyStatus = function() {
    $scope.myStatus = !$scope.myStatus;
  };

  $scope.getStatusText = function(val) {
    return val ? 'online' : 'offline';
  };

  $('document').ready(function(){
    $scope.resetStatus();
    var sock = io.connect('/lime');
    sock.on('value', $scope.updateLimes);
    sock.on('connect',function(){
      sock.emit('connected',1);
    });
    sock.on('disconnect', $scope.resetLimes);

  });
};



var app = angular.module('myApp', ['ui.bootstrap']);
app.controller('myCtrl', function($scope, $http, $timeout, $interval, $q) {

  $scope.game_service_url = localStorage.getItem("serverAddress")  // "http://127.0.0.1/gameservice" 

  $scope.usrid = localStorage.getItem("usrid")
  $scope.usrtkn = localStorage.getItem("token")
  $scope.game_id = localStorage.getItem("game_id")
  $scope.curr_player = null
  $scope.next_player = null
  $scope.game = []
  $scope.mymove = []

  /*$interval(function () {
      $scope.reloadRoute();
  },2000);
  */
  $scope.get_game = function(){
    $http(
        {
          url: $scope.game_service_url + '/move',
          method : 'GET',
          params: {
              gi_id: $scope.game_id
          }
        }
    ).then(
            function (response) {
                console.log(response.data.cstate)
                $scope.game = response.data
                angular.copy($scope.game,$scope.mymove)
            }
    )
  }

  $scope.my_move = function(i,j){
        if ($scope.usrid == $scope.mymove.user1){
            $scope.mymove.cstate[i][j] = "X"
            $scope.next_player = $scope.mymove.user2
            $scope.curr_player = $scope.mymove.user1
        }
        else{
            $scope.mymove.cstate[i][j] = "O"
            $scope.next_player = $scope.mymove.user1
            $scope.curr_player = $scope.mymove.user2
        }
        $scope.make_move()
  }

  $scope.make_move = function() {
    $http(
        {
          url: $scope.game_service_url + '/move',
          method : 'POST',
          headers : {
              'Content-Type':'application/json'
          },
          data : {
            gi_id : $scope.game_id,
            cstate : $scope.mymove.cstate,
            curr_player : $scope.curr_player, 
            next_player : $scope.next_player,
            token :  $scope.usrtkn
            }
        }
        ).then(
            function (response) {
                console.log(response.data)
                $scope.mymove = response.data
                $scope.game = response.data
            }
        ).then(
            function (response) {
                console.log(response.data.response)
                angular.copy($scope.mymove,$scope.game)
            }
        )
    }

    $scope.go_to_profile = function(){
        localStorage.removeItem("game_id")
        window.open("user_profile.html","_self");
    }

    $scope.get_game ()
});
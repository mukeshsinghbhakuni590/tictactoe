
var app = angular.module('myApp', ['ui.bootstrap']);
app.controller('myCtrl', function($scope, $http, $timeout, $interval, $q) {

  $scope.game_service_url =localStorage.getItem("serverAddress") //"http://127.0.0.1/gameservice" 

  $scope.users = []
  $scope.user_gi = []
  $scope.user_completed_games = []
  $scope.user_running_games = []
  $scope.user_requests = []
  $scope.usrid = localStorage.getItem("usrid")
  $scope.usrtkn = localStorage.getItem("token")
  $scope.userinfo = []

  $scope.get_users = function() {
    $http(
         {
                url: $scope.game_service_url + '/user',
                method: 'GET',
                params: {
                token: $scope.usrtkn //localStorage.getItem("token")
             }
         }
    ).then(
         function (response) {
             //$scope.token_str = response.data.responseData['X-Authorization-Token']
             console.log(response)
             $scope.users = response.data.response
         } 
        ) 	
    }

    $scope.create_game_instance = function(user_2) {
        $http(
            {
              url: $scope.game_service_url + '/gameinstance',
              method : 'POST',
              headers : {
                  'Content-Type':'application/json'
              },
              data : {
                  user1 : $scope.usrid, 
                  user2 : user_2, 
                  token : $scope.usrtkn 
              }
            }
        ).then(
                  function (response) {
                      console.log(response.data)
                      $scope.show_game_instances()
                  }
        )
    }
  
    $scope.accept_game_request = function(game_ins_id) {
        $http(
            {
              url: $scope.game_service_url + '/gameinstance',
              method : 'PUT',
              headers : {
                  'Content-Type':'application/json'
              },
              data : {
                  user_id : $scope.usrid, 
                  gi_id : game_ins_id, 
                  token : $scope.usrtkn 
              }
            }
        ).then(
                  function (response) {
                      console.log(response)
                      $scope.show_game_instances()
                  }
        ) 
    }
  
    $scope.chk_requests = function() {
        $http(
            {
              url: $scope.game_service_url + '/requests',
              method : 'GET',
              params: {
                  user_id: $scope.usrid
              }
            }
        ).then(
                  function (response) {
                      console.log(response)
                      $scope.user_requests = response.data 
                  }
        ) 
    }

    $scope.show_game_instances = function() {
        $http(
            {
              url: $scope.game_service_url + '/gameinstance',
              method : 'GET',
              params: {
                  user_id: $scope.usrid
              }
            }
        ).then(
                function (response) {
                    console.log(response)
                    $scope.user_completed_games = []
                    $scope.user_running_games = []
                    $scope.user_gi = response.data
                    $scope.game_filter()
                }
        )
    }

    $scope.game_filter = function(){
        for (i = 0; i< $scope.user_gi.length; i++) {
            if ($scope.user_gi[i].status == "COMPLETED"){
                $scope.user_completed_games.push($scope.user_gi[i])
            }
            else {
                $scope.user_running_games.push($scope.user_gi[i])
            }
        }
        $scope.user_gi = []
        
    }

    $scope.get_user_info = function(){
        $http(
            {
                url: $scope.game_service_url + '/user/' + $scope.usrid,
                method: 'GET',
                params: {
                token: $scope.usrtkn //localStorage.getItem("token")
                }
            }
        ).then(
            function (response) {
                console.log(response.data.response)
                $scope.userinfo = response.data.response
            }
        )
    }

    $scope.logout = function(){
        $http(
            {
                url: $scope.game_service_url + '/uservalidation',
                method: 'PUT',
                params: {
                token: $scope.usrtkn //localStorage.getItem("token")
                }
            }
        ).then(
            function (response) {
                console.log(response.data)
                localStorage.removeItem("usrid");
                localStorage.removeItem("token");
                window.open("../game_service.html","_self");
            }
        )
    }

    $scope.move_game = function(game_id){
        localStorage.setItem("game_id",game_id);
        window.open("play_game.html","_self");
    }

    $scope.game_details = function(game_id){
        localStorage.setItem("game_id",game_id);
        window.open("game_details.html","_self");
    }

    $scope.get_users()
    $scope.show_game_instances()
    $scope.get_user_info()
});

var app = angular.module('myApp', ['ui.bootstrap']);
app.controller('myCtrl', function($scope, $http, $timeout, $interval, $q) {

  $scope.game_service_url = "http://127.0.0.1/gameservice" //"http://192.168.43.81/gameservice" 
  localStorage.setItem("serverAddress", $scope.game_service_url )

  $scope.create_user = function() {
         $http(
              {
                  url: $scope.game_service_url + '/user',
                  method: 'POST',
                  headers : {
                    'Content-Type':'application/json' 
                  },
                  data : {
                      name : $scope.name,
                      email : $scope.email,
                      alias : $scope.alias,
                      password : $scope.pwd
                  }
              }
      ).then(
              function (response) {
                  //$scope.token_str = response.data.responseData['X-Authorization-Token']
                  console.log(response)
                  window.open("htmlfiles/user_validation.html","_self");
                 // $scope.get_users()
              } 
      ) 	
  }
  
  $scope.login_link = function () {
    window.open("htmlfiles/user_validation.html","_self");
    }
});

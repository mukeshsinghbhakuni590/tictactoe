

var app = angular.module('myApp', ['ui.bootstrap']);
app.controller('myCtrl', function($scope, $http, $timeout, $interval, $q) {

  $scope.game_service_url =  localStorage.getItem("serverAddress")             // "http://127.0.0.1/gameservice"

  $scope.login = function() {
    $http(
         {
             url: $scope.game_service_url + '/uservalidation',
             method: 'POST',
             headers : {
               'Content-Type':'application/json' 
             },
             data : {
                 email : $scope.email,
                 password : $scope.pwd
             }
         }
    ).then(
        function (response) {
            //$scope.token_str = response.data.responseData['X-Authorization-Token']
            console.log(response['data']['response']['token'])
            localStorage.setItem("usrid", response['data']['response']['userid']);
            localStorage.setItem("token", response['data']['response']['token']); 
            window.open("user_profile.html","_self");
        } 
    ) 	
    }
});
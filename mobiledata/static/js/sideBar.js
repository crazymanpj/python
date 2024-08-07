/**
 * Code by wusong on 2016/5/19.
 */
app.controller('sideBar', function ($scope, $http) {
    $http({
        method: 'get',
        url: '/cm/sidebar/'
    }).success(function (data) {
        $scope.data = data.grouplist;
    });

});

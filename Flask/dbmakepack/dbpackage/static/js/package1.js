/**
 * Created by kingsoft on 2018/1/16.
 */
var app = angular.module('wsAPP', ['ngSanitize', 'ui.select']);
app.controller('conditionController', function ($scope, $http){
    function init() {
        //1、获取产品列表
        //2、获取tryno列表
        //3、获取合作商列表

        //1、 获取产品列表
        $scope.products = ['金山毒霸', '其他'];
        $scope.product = $scope.products[0];
        $scope.panelType = allProducts[$scope.product];
        initDuba();

        /*
        $http({
            method: 'get',
            url: urls.getproductlist
        }).success(function (data) {
            if (data.errorcode == 0) {
                $scope.product = data.productlist;
                $scope.product = '金山毒霸';
                $scope.pantel = 'duba';
                initDuba();
            } else {
                //请求错误
            }
        }).error(function(data){
            //访问超时
        });
        */

    }
    init();
    $scope.product_change = function (x) {
        $scope.panelType = allProducts[x];
    };
    function initDuba() {
        var temp = [
            {id:1, name: "one"},
            {id:2, name: "two"}
        ]
        $scope.itemnames = temp;
        $scope.itemname = {value: $scope.itemnames[0]};
    }
    $scope.item_change = function (x) {
        alert(x);
    }
    
});



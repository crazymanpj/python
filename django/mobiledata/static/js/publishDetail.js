function getDataId() {
    var reg = new RegExp("(^|&)Id=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if(r!=null)return  r[2]; return 0;
}

app.controller('publishDetail', function($scope, $http) {
    function init() {
        var id = getDataId();
        if (id) {
            $http({
                method: 'post',
                url: '/cm/getpublishdetailbyid/',
                data: {
                    id: id
                }
            }).success(function (data) {
                // console.log(data.errorcode);
                if (data.errcode == null) {
                    $scope.publishdetail = data.packagedetails;
                    // console.log($scope.publishdetail);
                    $scope.plugins = $scope.publishdetail.pluginfo;
                    // console.log($scope.plugins);
                } else {
                    //请求错误
                }
            }).error(function(data){
                //访问超时
            });
        }
    }

    //    $scope.changeDetail = function(type) {
    //     /**
    //      * type=0  文件详情
    //      * type=1  修改点
    //      */
    //     var fileListLi = $("#filelistLi");
    //     var changelistLi = $("#changelistLi");
    //     switch (type) {
    //         case 0:
    //             if (!fileListLi.hasClass("active")){
    //                 changelistLi.removeClass("active");
    //                 fileListLi.addClass("active");
    //                 $("#changelist").hide();
    //                 $("#filelist").show();
    //             }
    //             break;
    //         case 1:
    //             // if (!changelistLi.hasClass("active")){
    //             //     fileListLi.removeClass("active");
    //             //     changelistLi.addClass("active");
    //             //     $("#filelist").hide();
    //             //     $("#changelist").show();
    //             // }
    //             break;
    //     }
    // };
    init();

    $scope.ispackage = function(){
        if($scope.ret_filetype == '安装包'){
            return true;
            }
        else{
            return false;
            }
        };

    $scope.isplugin = function(){
        if($scope.ret_filetype == '插件'){
            return true;
        }
        else{
            return false;
        }
    }
});
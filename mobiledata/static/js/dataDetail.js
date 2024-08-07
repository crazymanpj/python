/**
 * Created by kingsoft on 2016/8/29.
 */
function getDataId() {
    var reg = new RegExp("(^|&)Id=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if(r!=null)return  r[2]; return 0;
}
app.controller('dataDetail', function ($scope, $http){
    function init() {
        var id = getDataId();
        if (dataId) {
            $http({
                method: 'post',
                url: '/data/api/data/info/',
                data: {
                    dataid: dataId
                }
            }).success(function (data) {
                if (data.errcode == 0) {
                    $scope.itemlist = data.itemlist;
                    $scope.common = data.common;
                } else {
                    //请求错误
                }
            }).error(function(data){
                //访问超时
            });
        }
    }

    $scope.changeDetail = function(type) {
        /**
         * type=0  文件详情
         * type=1  修改点
         */
        var fileListLi = $("#filelistLi");
        var changelistLi = $("#changelistLi");
        switch (type) {
            case 0:
                if (!fileListLi.hasClass("active")){
                    changelistLi.removeClass("active");
                    fileListLi.addClass("active");
                    $("#changelist").hide();
                    $("#filelist").show();
                }
                break;
            case 1:
                // if (!changelistLi.hasClass("active")){
                //     fileListLi.removeClass("active");
                //     changelistLi.addClass("active");
                //     $("#filelist").hide();
                //     $("#changelist").show();
                // }
                break;
        }
    };
    init();
});
function getDataId() {
    var reg = new RegExp("(^|&)id=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if(r!=null)return  r[2]; return 0;
}

app.controller('EditDetail', function($scope, $http) {
    function init() {
        var id = getDataId();
        if (id) {
            $http({
                method: 'post',
                url: '/cm/editrecordbyid/',
                data: {
                    id: id
                }
            }).success(function (data) {
                console.log(data.errorcode);
                if (data.errcode == null) {
                    $scope.packageinfo = data.packageinfo;
                    $scope.publishtime = data.packageinfo.publishtime;
                    $scope.packagepath = data.packageinfo.packagepath;
                    $scope.apkver = data.packageinfo.apkver;
                    $scope.hostver = data.packageinfo.hostver;
                    $scope.packagemd5 = data.packageinfo.packagemd5;
                    $scope.packagesize = data.packageinfo.packagesize;
                    $scope.channel = data.packageinfo.channel;
                    $scope.iidcode = data.packageinfo.iidcode;
                    $scope.flag = data.packageinfo.flag;
                    $scope.remarks = data.packageinfo.remarks;
                    $scope.issync = data.packageinfo.issync;
                    console.log($scope.packageinfo);
                } else {
                    //请求错误
                }
            }).error(function(data){
                //访问超时
            });
        }
    }
    init();

    $scope.saverecord = function(){
        // alert($scope.packagepath);
        $http({
                method: 'post',
                url: '/cm/saverecordbyid/',
                data: {
                    id: $scope.packageinfo.id,
                    hostver: $scope.hostver,
                    publishtime: $scope.publishtime,
                    packagepath: $scope.packagepath,
                    apkver: $scope.apkver,
                    packagemd5: $scope.packagemd5,
                    packagesize: $scope.packagesize,
                    channel: $scope.channel,
                    iidcode: $scope.iidcode,
                    flag: $scope.flag,
                    remarks: $scope.remarks
                }
            }).success(function (data) {
                console.log(data.errorcode);
                if (data.errorcode == 0) {
                    alert("save success");
                } else {
                    //请求错误
                    alert(data.msg);
                }
            }).error(function(data){
                //访问超时
            });
    }

        $scope.deleterecord = function(pid){
        // alert($scope.packagepath);
        var ret = confirm("确认删除吗？");
        jumpurl = "/";
        if (ret == true)
        {
                $http({
                method: 'post',
                url: '/cm/deleterecordbyid/',
                data: {
                    id: $scope.packageinfo.id
                }
            }).success(function (data) {
                console.log(data.errorcode);
                if (data.errorcode == 0) {
                    alert("delete success");
                    window.location.href=jumpurl;
                } else {
                    //请求错误
                    alert(data.msg);
                }
            }).error(function(data){
                //访问超时
            });
        }
        else{
            return;
        }

    }

});
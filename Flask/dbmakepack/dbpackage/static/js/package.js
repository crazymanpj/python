/**
 * Created by kingsoft on 2018/1/16.
 */
var app = angular.module('package', []);
app.controller('conditionController', function ($scope, $http) {
    function init() {
        //1、获取产品列表
        //2、获取tryno列表
        //3、获取合作商列表

        $http({
            method: 'GET',
            url: urls.getproductlist
        }).success(function (data) {
            if (data.errorcode == 0) {
                $scope.products = data.productlist;
                $scope.product = $scope.products[0];
                $scope.panelType = allProducts[$scope.product];
                initDuba();
            }
        });
    }

    init();
    $scope.product_change = function (x) {
        $scope.panelType = allProducts[x];
        if (x == "duba") {
            initDuba();
        }
    };
    function initDuba() {
        // 初始化其他字段
        $("#js-tid1").val('');
        $("#js-tid2").val('');
        $("#js-tod1").val('');
        $("#js-tod2").val('');
        $("#specialfile").val('');
        $("#localname").val('');
        $scope.packettype = "exe";
        $scope.packetmodel = "非静默";
        $scope.fixuplive = '是';
        $scope.islokmp = '是';

        // item 初始化
        initItemName();


        // tryno初始化
        $http({
            method: 'GET',
            url: urls.gettyrnolist
        }).success(function (data) {
            if (data.errorcode == 0) {
                $scope.trynos = data.trynolist;
                $scope.tryno = $scope.trynos[0] + "";
            } else {
                //请求错误
            }
        }).error(function (data) {
            //访问超时
        });
        refreshHistory();

    }

    function refreshHistory() {
        // 历史记录
        $http({
            method: 'GET',
            url: urls.gethistroypackages
        }).success(function (data) {
            if (data.errorcode == 0) {
                //console.log(data);
                $scope.historypackages = data.data;
            }
        });
    }


    $scope.itemname_change = function (itemname) {
        if (itemname == "add new...") {
            $("#newItemnameModal").modal({
                keyboard: false,
                show: true,
                backdrop: 'static'
            });
        }
    };
    $scope.dismissNewItem = function () {
        $("#newItemnameModal").modal('hide');
        initItemName();

    };

    function initItemName(newItem) {
        $http({
            method: 'GET',
            url: urls.getitemlist
        }).success(function (data) {
            if (data.errorcode == 0) {
                addItemnameOptions(data.partnerlist, newItem);
                $scope.itemnames = data.partnerlist;
            } else {
                //请求错误
            }
        }).error(function (data) {
            //访问超时
        });
    }

    function addItemnameOptions(data, newItem) {
        var content = "";
        if (typeof(newItem) == "undefined") {
            $.each(data, function (idx, val) {
                if (idx == 1) {
                    content += "<option selected='true'>" + val + "</option>"
                } else {
                    content += "<option>" + val + "</option>"
                }
            });
        } else {
            $.each(data, function (idx, val) {
                content += "<option>" + val + "</option>";
            });
            content += "<option selected='true'>" + newItem + "</option>"

        }
        content += "<option>add new ...</option>";
        $("#js-itemname-select").html(content);
    }

    $scope.saveNewItem = function () {
        initItemName($("#newItemName").val());
        $("#newItemnameModal").modal('hide');
    };


    $scope.dopack = function () {
        // 构造参数
        var data = {
            product: $("#js-product-select option:checked").text() + "",
            // product: "duba",
            itemname: $("#js-itemname-select option:checked").text(),
            isnewitem: ($scope.itemnames.indexOf($("#js-itemname-select option:checked").text()) == -1 ? 1 : 0) + "",
            tryno: $("#js-tryno-select option:checked").text(),
            packettype: $("#js-packettype-select option:checked").val() + "",
            packetmodel: ($("#js-packetmodel-select option:checked").val() == "静默" ? 1 : 0) + "",
            tid1: $("#js-tid1").val() + "",
            tid2: $("#js-tid2").val() + "",
            tod2: $("#js-tod2").val() + "",
            tod1: $("#js-tod1").val() + "",
            fixuplive: ($("#js-fixuplive-select option:checked").val() == "是" ? 1 : 0) + "",
            islokmp: ($("#js-islokmp-select option:checked").val() == "是" ? 1 : 0) + "",
            specialfile: $("#specialfile").val(),
            localname: $("#localname").val()
        };
        // 没有做参数为空的校验
        $http({
            method: 'post',
            url: urls.dopack,
            data: data
        }).success(function (data) {
            if (data.errorcode == 0) {
                console.log("打包接口调用成功");
                //alert("开始打包..");
                $scope.message = messages.dopack;
                $("#showMessageModal").modal('show');
                disappear("showMessageModal");
                initDuba();
            } else {
                //请求错误
            }
        }).error(function (data) {
            //访问超时
        });
    };

    $scope.stoppack = function (id) {
        $http({
            method: 'GET',
            url: urls.stoppack,
            data: {
                Taskid: id
            }
        }).success(function (data) {
            if (data.errorcode == 0) {
                alert("停止成功")
            } else {
                //请求错误
            }
            refreshHistory();
        }).error(function (data) {
            //访问超时
        });
    };

    $scope.query = function (id) {
        $http({
            method: 'get',
            url: urls.getiffinish + "?Taskid=" + id
        }).success(function (data) {
            if (data.errorcode == 0) {
                // result 表示打包是否完成 0=未完成 1=完成
                if (data.result == 0) {
                    alert("打包中...");
                }
                if (data.result == 1) {
                    alert("打包完成...");
                    refreshHistory();
                }

            } else {
                //请求错误
            }
        }).error(function (data) {
            //访问超时
        });
    }

});
function showNewItemName() {
    if ($("#js-itemname-select option:checked").text() == "add new ...") {
        $("#newItemnameModal").modal({
            keyboard: false,
            show: true,
            backdrop: 'static'
        });
    }
}

function copyDataPath(a) {
    var dataPath = $(a).attr('data');
    $(a).val(dataPath);
    a.select();
    document.execCommand("Copy");
    $(a).val('点击复制');
    $("#copy-success").show();
    setTimeout(function() {
        $("#copy-success").hide();
    }, 2000);
}

function disappear(id) {
    setTimeout(function () {
        $("#"+id).modal('hide');
    },2000);
}
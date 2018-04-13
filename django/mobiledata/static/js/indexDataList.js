/**
 * Created by Administrator on 2016/5/20.
 */
app.controller('bottomDataList', function ($scope, $http, $rootScope,dataService) {
    // 配置头部，以达到跟jquery post一样的效果
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    data = {}
    data['page'] = '1'

    function initData(current) {
        $http({
            method: 'post',
            url: '/cm/getpublishdata/',
            data: data
        }).success(function (data) {
            $rootScope.bottomdata = data.datalist;
            console.log($rootScope.bottomdata);
            // $rootScope.ispub = data.common.canpub;
            // page.init(data.common.num_pages);
             $rootScope.current = current || 1;
             $rootScope.total = data.pagecount;
        });
    }

    function refresh() {
        var language = $("#js-language-select option:selected").text();
        var channel = $("#js-channel-select option:selected").text();
        // alert(lanuage + "--" + channel)
        var data = {};
        if (language != '全部') {
            data['language'] = language;
        }
        if (language != 'kxe_data' && channel != '全部') {
            data['channel'] = channel;
        }
        data['status'] = $("#js-status-select option:selected").val();
        $http({
            method: 'post',
            url: '/data/api/data/list/',
            data: data
        }).success(function (data) {
            $rootScope.bottomdata = data.itemlist;
            $rootScope.ispub = data.common.canpub;
        });
    }
    $scope.pub = function (id, size, language, channel) {
        if (size >= 5242880) {
            if (language == 'kcomponent') {
                $scope.dataSizeTooBig = 1;
            } else if (language == 'kxe_com' || language == 'kxe_app' || language == 'kav2010' || language == 'kmobile') {
                if (channel == '1335') {
                    $scope.dataSizeTooBig = 1;
                }
            }
        }
        $('#js-pub').modal({
            keyboard: true
        }).on('hidden.bs.modal', function() {
            $scope.dataSizeTooBig = -1;
        });
        $rootScope.pubDataId = id;
    }
    $("#pub-cancel").click(function() {
        $('#js-pub').modal('hide');
        $scope.dataSizeTooBig = -1;
    });
    $("#pub-go").click(function() {
        $rootScope.chicken = getRandomChicken();
        var id = $rootScope.pubDataId;
        $scope.dataSizeTooBig = -1;
        $rootScope.pubDataId = -1;
        $('#js-pub').modal('hide');
        if (user.state() && $rootScope.ispub == 1) {
            //展示动画
            setRandomGif();
            $("#loading").show();
            $("#js-errDetail").hide();
            $("#makedatasuccess").hide();
            $("#js-op").modal({
                keyboard: false,
                backdrop: 'static'
            });
            $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
            $http({
                method: 'post',
                data: {
                    id: id
                },
                url: '/data/api/data/pub/',
                timeout: 1200000
            }).success(function (data) {
                if (data.errcode == 0) {
                    //发布成功

                    $("#loading").hide();
                    $("#makedatasuccess").show();

                    setTimeout(function () {
                        $("#js-op").modal('hide');
                        $("#makedatasuccess").hide();
                        $("#loading").show();
                        refresh();
                    }, 3000);
                } else {
                    //其他原因导致失败
                    $("#loading").hide();
                    $("#js-errDetail").show();
                    $rootScope.errcode = data.errcode;
                    $rootScope.errDetail = data.msg;
                }
            }).error(function (data) {
                //请求超时的判断
                if (status == -1) {
                    $("#loading").hide();
                    $("#js-errDetail").show();
                    $rootScope.errDetail = '接口访问超时';
                }
            });

        } else {
            $("#loading").hide();
            $("#js-errDetail").show();
            $rootScope.errDetail = '用户未登录';
            $("#js-op").modal({
                keyboard: false,
                backdrop: 'static'
            });
        }

    });
    $scope.closeOp = function() {
        $("#js-op").modal('hide');
    };
    $scope.redo = function (id) {
        //先展示动画
        setRandomGif();
        $rootScope.chicken = getRandomChicken();
        $("#loading").show();
        $("#makedatasuccess").hide();
        $("#js-errDetail").hide();
        $("#js-op").modal({
            keyboard: false,
            backdrop: 'static'
        });
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
        var forcereboot = 0;
        var nosigncheck = 0;
        if($('#isSync').is(':checked')) {
            forcereboot = 1;
        }
        if($('#isIgnoreSign').is(':checked')) {
            nosigncheck = 1;
        }
        $http({
            method : 'post',
            data : {
                id : id,
                forcereboot : forcereboot,
                nosigncheck : nosigncheck
            },
            url: '/data/api/data/create/',
            timeout : 12000000
        }).success(function (data) {
            if (data.errcode == 0) {
                //制作成功
                $("#loading").hide();
                $("#makedatasuccess").show();
                setTimeout(function () {
                    $("#js-op").modal('hide');
                    $("#makedatasuccess").hide();
                    $("#loading").show();
                }, 3000);
                $("#isSync").prop("checked", false);
                $("#isIgnoreSign").prop("checked", false);
                refresh();
            } else {
                    //未知的错误
                    $("#loading").hide();
                    $("#js-errDetail").show();
                    $rootScope.errDetail = data.msg;
                    $rootScope.errcode = data.errcode;
                    if (data.errcode == 300) {
                        $rootScope.errDetail = data.msg;
                    }
            }
        }).error(function(data, status) {
            if (status == -1) {
                $("#loading").hide();
                $("#js-errDetail").show();
                $rootScope.errDetail = '接口访问超时';
            }
        });

    }

    $scope.showLogin = function () {
        $("#js-op").modal('hide');
        $("#js-login").modal("show");
        $rootScope.errcode = 0;
    }
    $scope.compare = function (id) {
        console.log("对比开始！")
        // $scope.$emit('handleCompareResultEmit', {id: id});
        $("#js-loading").modal({
            keyboard:false,
            backdrop: 'static'
        });
        $rootScope.chicken = getRandomChicken();
        init(id);
        console.log("对比结束！" + new Date())
    }

    $scope.showModify = function (x) {
        $http({
            method: 'post',
            url: '/data/api/data/modification/',
            data:{
                id: x.id
            },
            timeout : 12000000
        }).success(function(data) {
            //要对返回的数据进行处理
            var changelist = data.common.changelist;
            var content = '';
            if (changelist == '') {
                content = "<h4>无数据</h4>"
            } else {
                var content = "<p style='WORD-WRAP: break-word' width='600px'>" + data.common.changelist + "</p>";
            }
            if (data.errcode == 0 && x.status == 1) {
                $("#path" + x.id).popover({
                    content: content,
                    html: true,
                    trigger: 'hover'
                });
            }
        });
    };

    //对比
    $scope.open = function(parentId, id, type){
        if (type == 1) {
            $("#errModal" + parentId + "" + id).modal();
        }else if (type == 2) {
            $("#addModal" + parentId + "" + id).modal();
        } else if (type == 3) {
            $("#delModal" + parentId + "" + id).modal();
        } else if (type == 4) {
            $("#diffModal" + parentId + "" + id).modal();
        }
    }
    function init(id) {
        console.log('init');
        $http({
            method: 'post',
            url: '/data/api/data/compare/',
            data:{
                id: id
            },
            timeout : 12000000
        }).success(function (data) {
            if (data.errcode == 0) {
                $scope.leftFileCount = data.common.count[0];
                $scope.rightFileCount = data.common.count[1];
                $scope.addFileCount = data.common.addnum;
                $scope.diffFileCount = data.common.diffnum;
                $scope.delFileCount = data.common.delnum;
                $scope.errFileCount = data.common.errnum;
                $scope.errInfo = data.common.err;
                $scope.add = data.common.add;
                $scope.del = data.common.del;
                $scope.diff = data.common.diff;
                $scope.show = $scope.errInfo.concat($scope.diff);
                $scope.showType = 1;
                $("#js-loading").modal('hide');
                setTimeout(function(){
                    $("#js-compare").modal().on('hidden.bs.modal', function() {
                        $("#addLi").removeClass('active');
                        $("#delLi").removeClass('active');
                        $("#errAndDelLi").addClass('active');
                        $scope.show = $scope.errInfo.concat($scope.diff);
                        $scope.showType = 1;
                    });
                },1000);
            } else {
                $("#loading").hide();
                $("#makedatasuccess").hide();
                $("#js-loading").modal('hide');
                $rootScope.errDetail = data.msg;
                $("#js-errDetail").show();
                $("#js-op").modal({
                    keyboard: false,
                    backdrop: 'static'
                });
            }
        }).error(function(data, status) {
            if (status == -1) {
                $("#loading").hide();
                $("#makedatasuccess").hide();
                $("#js-loading").modal('hide');
                $rootScope.errDetail = '接口访问超时';
                $("#js-errDetail").show();
                $("#js-op").modal({
                    keyboard: false,
                    backdrop: 'static'
                });
            }
        });
    };

    $scope.change = function(type) {
        /**
         * 1. errAndDiff
         * 2. Add
         * 3. Del
         * @type {*|jQuery|HTMLElement}
         */
        var errAndDiff = $("#errAndDelLi");
        var add = $("#addLi");
        var del = $("#delLi");
        switch (type) {
            case 1:
                if (!errAndDiff.hasClass('active')) {
                    add.removeClass('active');
                    del.removeClass('active');
                    errAndDiff.addClass('active');
                    $scope.show = $scope.errInfo.concat($scope.diff);
                    $scope.showType = 1;
                }
                break;
            case 2:
                if (!add.hasClass('active')) {
                    errAndDiff.removeClass('active');
                    del.removeClass('active');
                    add.addClass('active');
                    $scope.show = $scope.add;
                    $scope.showType = 2;
                }
                break;
            case 3:
                if (!del.hasClass('active')) {
                    add.removeClass('active');
                    errAndDiff.removeClass('active');
                    del.addClass('active');
                    $scope.show = $scope.del;
                    $scope.showType = 3;
                }
                break;
        }
    };

    $scope.showFileDetail = function(x) {
        var popContent = generateFileDetail($scope.showType, x);
        var ele = document.getElementById("detail" + x.filename);
        $(ele).popover({
            title: x.filename + "详情",
            content: popContent,
            trigger: 'hover',
            html: true
        }).on('shown.bs.popover', function (event) {
            var that = this;
            $(this).parent().find('div.popover').on('mouseenter', function () {
                $(that).attr('in', true);
            }).on('mouseleave', function () {
                $(that).removeAttr('in');
                $(that).popover('hide');
            });
        }).on('hide.bs.popover', function (event) {
            if ($(this).attr('in')) {
                event.preventDefault();
            }
        }).on('mouseleave', function() {
            $(this).popover('hide');
        });
    };
    function generateFileDetail(type, file) {
        var result = '<table class="table table-striped table-hover table-bordered"><thead><th>项目</th><th>外网数据</th><th>本次数据</th></thead><tbody>';
        if(type == 1) {
            $.each(file.values.left, function(key, value) {
                var tmp = "";
                if (file.opname && key == file.opname) {
                    tmp += "<tr>"
                        + "<th>" + key + "</th>"
                        + "<th style='color:red'>" + value + "</th>"
                        + "<th style='color:red'>" + file.values.right[key] + "</th>"
                        + "</tr>";
                }else {
                    tmp += "<tr>"
                        + "<th>" + key + "</th>"
                        + "<th>" + value + "</th>"
                        + "<th>" + file.values.right[key] + "</th>"
                        + "</tr>";
                }
                result += tmp;

            });
        }
        if (type == 2) {
            $.each(file.values, function(key, value) {
                result += "<tr>";
                var tmp = "<th>" + key + "</th>";
                tmp += "<th>无数据</th>" + "<th>" + value + "</th>";
                result += tmp;
                result += "</tr>";
            });
        }
        if (type == 3) {
            $.each(file.values, function(key, value) {
                result += "<tr>";
                var tmp = "<th>" + key + "</th>";
                tmp += "<th>" + value + "</th>" + "<th>无数据</th>";
                result += tmp;
                result += "</tr>";
            });
        }
        result += "</tbody></table>"
        return result;
    }

    $scope.synOtherChannel = function(id, chnum){
        $rootScope.synrecordid = id;
        $("#js-selectsynchannel").modal();
        console.log($rootScope.data);
        $rootScope.data.channel.splice($.inArray(Number(chnum), $rootScope.data.channel), 1);
    };


    initData(1);
});


function copy(copyPath) {
    copyPath.select();
    document.execCommand("Copy");
    $("#copy-success").show();
    setTimeout(function() {
        $("#copy-success").hide();
    }, 2000);
}
app.controller("pageCtrl", function($scope, $http, $rootScope,dataService) {
    $scope.changePage = function(currentPage) {
        refresh(currentPage);
        $rootScope.current = currentPage;
        $('body,html').animate({scrollTop:0},500);
        $("#refresh-success").show();
        setTimeout(function(){
            $("#refresh-success").hide();
        }, 1500);
    }
    function refresh(page) {
        data = {};
        var channel = $("#js-channel-select option:selected").text();
		var hostver = $("#js-hostver-select option:selected").text();
        var apkver = $("#js-apkver-select option:selected").text();
        var status = $("#js-status-select option:selected").text();
        console.log(status);
        if (hostver != '全部') {
            data['hostver'] = hostver;
        }
        if (channel != '全部') {
            data['channel'] = channel;
        }
        if (apkver != '全部') {
            data['apkver'] = apkver;
        }
        if (status == '全部') {
            data['status'] = -1;
        } else if (status == '未发布') {
            data['status'] = 0;
        } else if (status == '已发布') {
            data['status'] = 1;
        } else if (status == '已过期') {
            data['status'] = 2;
        }
        data['page'] = page;
        $http({
            method: 'post',
            url: '/cm/getpublishdata/',
            data: data
        }).success(function (data) {
            $rootScope.bottomdata = data.datalist;
            // $rootScope.ispub = data.common.canpub;
        });
    }
});
app.controller("bodyController", function($scope, $http, $rootScope) {
    $scope.mo = function (event) {

        if (event.keyCode == 116) {
            // event.keyCode = 0;
            if (!event.ctrlKey) {
                event.preventDefault();
                refresh(1);
            }
        }
    }
    function refresh(page) {
        data = {};
        var channel = $("#js-channel-select option:selected").text();
        var hostver = $("#js-hostver-select option:selected").text();
        var apkver = $("#js-apkver-select option:selected").text();

        if (hostver != '全部') {
            data['hostver'] = hostver;
        }
        if (channel != '全部') {
            data['channel'] = channel;
        }
        if (apkver != '全部') {
            data['apkver'] = apkver;
        }
        data['page'] = page;
         $http({
            method: 'post',
            url: '/cm/getpublishdata/',
            data: data
        }).success(function (data) {
            $rootScope.bottomdata = data.datalist;
            console.log($rootScope.bottomdata);
            // $rootScope.ispub = data.common.canpub;
            // page.init(data.common.num_pages);
             $rootScope.current = page || 1;
             $rootScope.total = data.pagecount;
             $('body,html').animate({scrollTop:0},500);
             $("#refresh-success").show();
             setTimeout(function(){
                $("#refresh-success").hide();
            }, 1500);
        });
    }
});




$("#clear_session_btn").click(function() {
    $.post('/tool/api/seropera/', {optype: 'cleansession'},
        function(data) {
            if (data.errcode == 0) {
            }
        }
    );
});
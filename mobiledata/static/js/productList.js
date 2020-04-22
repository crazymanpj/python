
app.controller('selectList', function ($scope, $http, $rootScope, dataService) {
    function refresh() {
        // var data = {};
        // data['language'] = $scope.language;
        // if ($scope.language != 'kxe_data') {
        //     data['channel'] = $scope.channel;
        // }
		data = {}
		data['page'] = '1'
        $http({
            method: 'post',
            url: '/cm/getpublishdata/',
			data: data
        }).success(function (data) {
            $rootScope.bottomdata = data.datalist;
            // console.log($rootScope.data);
            // $rootScope.ispub = data.common.canpub;
            // page.init(data.common.num_pages);
             // $rootScope.current = current || 1;
             $rootScope.total = data.pagecount;
        });
    }
    // 配置头部，以达到跟jquery post一样的效果
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    /*
     * 获取下拉数据方法
     */
    function initSelectData() {
        $http({
            method: 'post',
            url: '/cm/selectlist/'
        }).success(function (res) {
            var data = res.selectlist;
            //data.product.unshift('全部');
            $scope.product = data.product[0];
            data.hostver.unshift('全部');
            $scope.hostver = data.hostver[0];
            data.channel.unshift('全部');
            $scope.channel = data.channel[0];
            for (x in data.channel)
            {
                if (data.channel[x] == "999999")
                    {
                        data.channel[x] = "全网渠道";
                    }
            }
            data.apkver.unshift('全部');
            $scope.apkver = data.channel[0];
            // data.channel.unshift('全部');
            //$scope.channel = data.channel[0];
            //$scope.status = '-1';
            $rootScope.data = data;
        });
    }
    // $scope.product_change = function (x) {
    //     getSelectData({product: x});
    // };

    $scope.hostver_change = function (x) {
      // $("#js-status-select").val("-1");
        var promise = dataService.get({product: $scope.product, hostver: x, channel: $scope.channel, apkver: $scope.apkver}); // 同步调用，获得承诺接口
        promise.then(function (data) {  // 调用承诺API获取数据 .resolve
            $rootScope.bottomdata = data.datalist;
            $rootScope.current = 1;
            $rootScope.total = data.pagecount;
            $("#refresh-success").show();
            setTimeout(function(){
                $("#refresh-success").hide();
            }, 1500);
        });
    };

    $scope.channel_change = function (x) {
        // $scope.status = -1;
        // $("#js-status-select").val("-1");
        var promise = dataService.get({product: $scope.product, hostver: $scope.hostver, apkver: $scope.apkver, channel: x}); // 同步调用，获得承诺接口
        promise.then(function (data) {  // 调用承诺API获取数据 .resolve
            $rootScope.bottomdata = data.datalist;
            $rootScope.current = 1;
            $rootScope.total = data.pagecount;
            $("#refresh-success").show();
            setTimeout(function(){
                $("#refresh-success").hide();
            }, 1500);
        });
    };

    $scope.apkver_change = function (x) {
        // $scope.status = -1;
        $("#js-status-select").val("-1");
        var promise = dataService.get({product: $scope.product, hostver: $scope.hostver, channel: $scope.channel, apkver: x}); // 同步调用，获得承诺接口
        promise.then(function (data) {  // 调用承诺API获取数据 .resolve
            $rootScope.bottomdata = data.datalist;
            $rootScope.current = 1;
            console.log("ttttttt")
            console.log(data)
            $rootScope.total = data.pagecount;
            $("#refresh-success").show();
            setTimeout(function(){
                $("#refresh-success").hide();
            }, 1500);
        });
    };

    $scope.searchinput_change = function (x) {
        var text = x;
        data = {};
        data['page'] = '1';
        if(text == ""){
            return refresh();
        }

        $http({
            method: 'post',
            url: '/cm/searchtext/',
            data: {
                searchtext : text
            }
        }).success(function (data) {
            $rootScope.bottomdata = data.datalist;
            // console.log($rootScope.data);
            // $rootScope.ispub = data.common.canpub;
            // page.init(data.common.num_pages);
             // $rootScope.current = current || 1;
             $rootScope.total = data.pagecount;
        });
    };

    function showMakeError(text) {
        $("#make-error b:first").text(text);
        $("#make-error").show();
        setTimeout(function() {
            $("#make-error").hide();
        }, 2000);
    }

    //制作数据
    $scope.create_data_submit = function () {
        var i = 1;
        var pluginlist = new Array();
        $("#plugincontain input[type='text']").each(function(){
            pluginlist.push($(this).val());
        });
        pluginpath1 = pluginlist[0];
        if ($scope.hostver == '全部') {
            showMakeError('没有选择相应的宿主版本号!');
        } else if ($scope.channel == undefined) {
            showMakeError('没有选择相应的渠道!');
        } else if ($scope.publishtime == undefined){
            showMakeError('没有选择发布日期！')
        } else if (!($scope.apkpath || pluginpath1)) {
            showMakeError('至少需要填写一个安装包地址或插件地址!');
        } else if (!$scope.details) {
            showMakeError('发布内容为空!');
        } else {
            setRandomGif();
            $rootScope.chicken = getRandomChicken();
            $("#loading").show();
            $("#makedatasuccess").hide();
            $("#js-errDetail").hide();
            $("#js-op").modal({
                keyboard: false,
                backdrop: 'static'
            });
            $http({
                method: 'post',
                url: '/cm/submitpublishdata/',
                data:{
                    product: $scope.product,
                    hostver: $scope.hostver,
                    channel: $scope.channel,
                    //status: parseInt($scope.status),
                    publishtime: $scope.publishtime,
                    apkpath: $scope.apkpath,
                    details: $scope.details,
                    pluginlist: pluginlist
                    // forcereboot:forcereboot(),
                    // nosigncheck:nosigncheck()
                }
            }).success(function (data) {
                if (data.errorcode == 0) {
                    //制作成功
                    $("#loading").hide();
                    $("#makedatasuccess").show();
                    setTimeout(function() {
                        $scope.path = '';
                        $scope.details = '';
                        $scope.channel = '';
                        $scope.publishtime = '';
                        $scope.hostver = '全部';
                        $("#data-path").val("");
                        $("#details").val("");
                        $("#makedatasuccess").hide();
                        $("#js-op").modal('hide');
                        window.location.reload();
                    }, 3000);
                    refresh();
                } else {
                    //未知的错误
                    $("#loading").hide();
                    $("#js-errDetail").show();
                    $rootScope.errDetail = data.msg;
                    $rootScope.errorcode = data.errorcode;
                    if (data.errcode == 300) {
                        $rootScope.errDetail = data.msg + "! 可能有人正在做数据！";
                    }
                    // $("#js-op").modal('hide');
                }
            }).error(function(data, status) {
                if (status == -1) {
                    //status = -1 时表示超时
                    $("#loading").hide();
                    $("#js-errDetail").show();
                    $rootScope.errDetail = '接口访问超时';
                }
            });
        }
    };

    //重置数据
    $scope.clear_data = function () {
        $scope.apkpath = '';
        $scope.details = '';
    };


    function getSelectData() {
        var product = arguments[0].product || null,
            language = arguments[0].language || null;
        // alert(product);
        // alert(language);
        var data = {};
        if (product != '全部') {
            data['product'] = product;
        }
        if (language != '全部' && language != null) {
            data['language'] = language;
        }
        $http({
            method: 'post',
            url: '/data/api/product/list/',
            data: data
        }).success(function (res) {
            var data = res.itemlist;
            if (product && !language) {
                data.product.unshift('全部');
                data.language.unshift('全部');
                $scope.language = data.language[0];
                data.channel.unshift('全部');
                $scope.channel = data.channel[0];
            }
            if (language && product) {
                data.product.unshift('全部');
                data.language.unshift('全部');
                data.channel.unshift('全部');
                $scope.channel = data.channel[0];
                console.log(product);
            }
            $scope.data = data;
            reload();
        });
    }

    function reload() {
        var product = $scope.product;
        var language = $scope.language;
        var channel = $scope.channel;
        var data = {};
        // if (product != '全部' && language != null) {
        //     data['product'] = product;
        // }
        if (language != '全部' && language != null) {
            data['language'] = language;
        }
        if (channel != '全部' && channel != null) {
            data['channel'] = channel;
        }
        data['status'] = -1;
        $http({
            method: 'post',
            url: '/data/api/data/list/',
            data:data
        }).success(function (data) {
            $rootScope.data = data.itemlist;
            $rootScope.ispub = data.common.canpub;
            $rootScope.current = 1;
            $rootScope.total = data.common.num_pages;
            $("#js-status-select").val(-1);
            $("#refresh-success").show();
            setTimeout(function(){
                $("#refresh-success").hide();
            }, 1500);
        });
    }

    // $scope.selected = [];
    $scope.selected = [];
    $scope.isChecked = function(id){
        return $scope.selected.indexOf(id) >= 0;
    };

    $scope.synChannel = function($event, channel){
        if ($scope.selected ==''){
            return;
        }
        setRandomGif();
        $rootScope.chicken = getRandomChicken();
        $("#loading").show();
        $("#makedatasuccess").hide();
        $("#js-errDetail").hide();
        $("#js-op").modal({
            keyboard: false,
            backdrop: 'static'
        });

        $http({
            method: 'post',
            url: '/cm/synchannelrecord/',
            data:{
                synrecordid: $rootScope.synrecordid,
                channellist: $scope.selected,
            }
        }).success(function (data) {
            if (data.errorcode == 0) {
            //制作成功
            $("#loading").hide();
            $("#makedatasuccess").show();
            setTimeout(function() {
                $scope.hostver = '全部';
                $scope.details = '';
                $("#data-path").val("");
                $("#makedatasuccess").hide();
                $("#js-op").modal('hide');
            }, 2000);
            refresh();
            initSelectData();
            } else {
            //未知的错误
            $("#loading").hide();
            $("#js-errDetail").show();
            $rootScope.errDetail = data.msg;
            $rootScope.errorcode = data.errorcode;
            }
        }).error(function(data, status) {
            if (status == -1) {
                $("#loading").hide();
                $("#js-errDetail").show();
                $rootScope.errDetail = '接口访问出错';
            }
        });

        //判断没选择的情况
        // alert($rootScope.synrecordid);
        // alert($scope.selected);
        //同步数据
    };
    $scope.updateSelection = function($event, channel){

        var checkbox = $event.target;
        var checked = checkbox.checked;
        if(checked){
            $scope.selected.push(channel);
        }else{
            var idx = $scope.selected.indexOf(channel);
            $scope.selected.splice(idx, 1);
        }
    };
    //添加插件路径
    $scope.pluginnum = 1;
    $scope.add_plugin_path = function(){
        // alert("sfe");
        // document.getElementById("addpluginpath").innerHTML+='<div id="div_'+i+'"><input name="text" name="text_'+i+'" type="text" value="alixixi.com"  /><input type="button" value="删除"  onclick="del('+i+')"/></div>';
        // $("addpluginpath").after('<i>After</i>');
        // var input = document.createElement("input");
        // input.setAttribute("type", "text");
        // input.setAttribute("id", "pluginpath");
        // var div = document.getElementById("plugincontain");
        // div.appendChild(input);

        // var div = document.getElementById("plugincontain");
        $(plugincontain).append('<div id="div_'+$scope.pluginnum+'"><div class="form-group col-md-8"><label>插件：</label><input type="text" class="form-control" placeholder="插件路径地址" ng-model="pluginpath_'+$scope.pluginnum+'" id="plugin_'+$scope.pluginnum+'"></input></div><div class="form-group col-md-1"><button name="add" class="btn btn-danger" style="margin-top:22px" onclick="del_plugin_path('+$scope.pluginnum+')"><span class="glyphicon glyphicon-minus"></span></button></div></div>');
        $scope.pluginnum++;
        //div.innerHTML += '<div id="div_'+i+'"<input type="text" id="pluginpath"/></div>';
        //console.log(div.innerHTML);
    }

//初始化下拉数据
    initSelectData();
});

app.controller('addChannel', function($scope, $http, $rootScope, dataService){
    function initData(){
        // alert($scope.channelDescription);
        // alert($scope.channelId);
    }

    $scope.addchannel = function(){
    var ret = confirm("确认添加该渠道吗？");
    if (ret == true)
    {
        $http({
            method: 'post',
            url: '/cm/addchannel/',
            data: {
                decription : $scope.channelDescription,
                channelnum : $scope.channelId
            }
        }).success(function (data) {
            if(data.errorcode == 0){
                alert("添加成功");
            }
            else{
                alert(data.msg);
            }
        });
    }
    else
    {
    return;
    }
    };
    initData();
});

app.controller('addHostver', function($scope, $http, $rootScope, dataService){
    function initData(){

    }

    $scope.addhostver = function(){
        var ret = confirm("确认添加该宿主版本号吗？");
        if (ret == true)
        {
        $http({
            method: 'post',
            url: '/cm/addhostver/',
            data: {
                hostver : $scope.hostver
            }
        }).success(function (data) {
            if(data.errorcode == null){
                alert("添加成功");
            }
            else{   
                alert(data.msg);
            }
   //          alert('add success!');
   //          $rootScope.data = data;
			// refresh();
        });
        }
        else
        {
        return;
        }
    }
});

app.controller('ChannelManager', function($scope, $http, $rootScope, dataService){
    function initData(){

          $http({
            method: 'get',
            url: '/cm/getchannellist/',
            data: {
            }
        }).success(function (data) {
            if(data.errorcode == null){
                // alert("添加成功");
            }
            else{   
                $scope.data = data.data;
                // alert(data.msg);
            }
   //          alert('add success!');
   //          $rootScope.data = data;
            // refresh();
        });

    }

    $scope.editsinglechannel= function(x){
        $scope.channel = x.channelnum;
        $scope.pid = x.id;
        $scope.description = x.description;
        $('#js-editchannel').modal();
    }

    $scope.savechannel = function(){
        // alert($scope.channel);
        // alert($scope.pid);
        // alert($scope.description);
        jumpurl = '/';
        jumpcuurl = 'ChannelManager.html';

     $http({
            method: 'post',
            url: '/cm/savechannelbyid/',
            data: {
                pid : $scope.pid,
                channelnum : $scope.channel,
                description :  $scope.description
            }
        }).success(function (data) {
            if(data.errorcode == 0){
                window.location.href=jumpcuurl;

            }
            else{   
                 alert(data.msg);
                 window.location.href=jumpurl;
            }
   //          alert('add success!');
   //          $rootScope.data = data;
            // refresh();
        });


    }

initData();
});

$(function () {
	$('#datetimepicker').datetimepicker({ 
// 　　    minView: "month", 
		language: 'zh-CN',
        format: 'yyyy-mm-dd hh:ii',
		autoclose:true 
}).next().on('click', function() {
	$(this).prev().focus();
});});

function del_plugin_path(o){
    document.getElementById('plugincontain').removeChild(document.getElementById("div_"+o));
}
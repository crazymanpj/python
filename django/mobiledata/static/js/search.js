
app.controller('searchchannel', function($scope, $http, $rootScope, dataService){
    function initSearchData(){
        $http({
            method: 'get',
            url: '/cm/getsearchchanneldata/'
        }).success(function(data){
            $scope.data = data;
            data.channellist.unshift('全部');
            $scope.channel = data.channellist[0];
            data.filetypelist.unshift('全部');
            $scope.filetype = data.filetypelist[0];
            //console.log($scope.data)
        });
    }

    $scope.search_channel = function(){
        var channel_select = $scope.channel;
        var filetype_select = $scope.filetype;
        if($scope.channel == '全部'){
            return;
        }else if($scope.filetype == '全部'){
            filetype_select = '';
        }
        $http({
            method: 'post',
            url: '/cm/searchchannel/',
            data: {
                channel : channel_select,
                filetype : filetype_select
            }
        }).success(function(data){
            $rootScope.bottomdata_channel = data;
        });

    };

    initSearchData();
});
$('#searchInput').typeahead({
    source: function(query, process) {
        $.post("/data/api/index/suggest/", {
            filename: query
        }, function(data) {
            process(data.itemlist);
        });
    }
});

// $("#searchBtn").click(function() {
//     var data = {};
//     data['page'] = 1;
//     var product = $("#data-product-select option:selected").text();
//     var language = $("#data-language-select option:selected").text();
//     var channel = $("#data-channel-select option:selected").text();
//     var isvalidStr = $("#data-isIndex-select option:selected").text();
//     // data['filename'] = filename;
//     if(filename == '' && purpose == '') {
//         return;
//     }

//     if(isvalidStr != '全部') {
//         if (isvalidStr == '在') {
//             data['isvalid'] = 1;
//         } else {
//             data['isvalid'] = 0
//         }
//     }
//     if (product != '全部') {
//         data['product'] = product;
//     }
//     if (language != '全部') {
//         data['language'] = language;
//     }
//     if (channel != '全部') {
//         data['channel'] = channel;
//     }
//     var purpose = $("#purpose").val();
//     if (purpose != '') {
//         data['purpose'] = purpose;
//     }
//     $.post(
//         "/data/api/index/search/",
//         data,
//         function(data) {
//             // 展示数据
//             addData(data.itemlist);
//             addPageNo(data.common.num_pages, 1);
//         }
//     );
// });
function jump(id) {
    cookie("id", id);
    window.location.href = "/web/history.html";
}
function addPageNo(pagenum, activepage) {
    $("#js-search-page").show();
    var data = [];
    if (activepage != 1) {
        data.push('<li><a href="javascript:void(0)">' + '首页' + '</a></li>');
        data.push('<li><a href="javascript:void(0)">' + '上一页' + '</a></li>');
    }
    var max = parseInt(activepage) + 2;
    var min = parseInt(activepage) - 2;
    for (var i = min; i <= max; i++) {
        if (i > 0 && i <= pagenum) {
            if (i == activepage) {
                data.push('<li class="active"><a href="javascript:void(0)">' + i + '</a></li>')
            } else {
                data.push('<li><a href="javascript:void(0)">' + i + '</a></li>')
            }
        }
    }
    // if (activepage + 1 )
    data.push('<li disabled><a href="javascript:void(0)">' + '共' + pagenum + '页' + '</a></li>');
    $("#js-search-page").html('').append(data).find('li').on('click', function () {
        pageNo = $(this).find('a').html();
        tmp = "共" + pagenum + "页";
        if (pageNo != tmp) {
            if (pageNo == '首页') {
                pageNo = 1;
            } else if (pageNo == '上一页') {
                pageNo = activepage - 1;
            } else if (pageNo == '下一页') {
                pageNo = activepage + 1;
            } else if (pageNo == '末页') {
                pageNo = pagenum;
            }
            //重新展示数据
            getSearchData(pageNo);
        }
    });
}

function getSearchData(pagenum) {
    var data = {};
    var filename = $("#searchInput").val();
    var product = $("#data-product-select option:selected").text();
    var language = $("#data-language-select option:selected").text();
    var channel = $("#data-channel-select option:selected").text();
    var isvalidStr = $("#data-isIndex-select option:selected").text();
    data['filename'] = filename;
    data['page'] = pagenum;
    if(isvalidStr != '全部') {
        if (isvalidStr == '在') {
            data['isvalid'] = 1;
        } else {
            data['isvalid'] = 0
        }
    }

    if (product != '全部') {
        data['product'] = product;
    }
    if (language != '全部') {
        data['language'] = language;
    }
    if (channel != '全部') {
        data['channel'] = channel;
    }
    var purpose = $("#purpose").val();
    if (purpose != '') {
        data['purpose'] = purpose;
    }
    $.post(
        "/data/api/index/search/",
        data,
        function(data) {
            // 展示数据
            addData(data.itemlist);
            addPageNo(data.common.num_pages, pagenum);
        }
    );
}

function addData(itemlist) {
    var showData = [];
    $.each(itemlist, function(idx, obj) {
        isIndexStr = "";
        if (obj.isvalid == 0) {
            isIndexStr = "否";
        } else {
            isIndexStr = "是";
        }
        isIndex = "<th>" + isIndexStr + "</th>";
        filenameStr = "<th>" + obj.filename + "</th>";
        languageStr = "<th>" + obj.language + "</th>";
        channelStr = "<th>" + obj.channel + "</th>";
        filePathStr = "<th>" + obj.localfilepath + "</th>";
        purposeStr = "<th>" + obj.purpose + "</th>";
        pubStr = "<th><a role='button' class='btn btn-primary' onclick=jump(" + obj.id + ")>查询发布历史</a><th></th>";
        showStr = "<tr>" + isIndex + filenameStr +
            languageStr + channelStr + filePathStr + purposeStr + pubStr +"</tr>";
        showData.push(showStr);
    });

    $("#js-search-lists").html('').append(showData);
}

// $.post(
//     "/data/api/product/list/",
//     {},
//     function(data){
//         var optList = [];
//         $.each(data.itemlist.product, function(idx, obj){
//             optList.push("<option>" + obj + "</option>");
//         });
//         $("#data-product-select").html('').append("<option>全部</option>").append(optList);
//     }
// );
$("#data-product-select").change(function() {
    var productSelected = $("#data-product-select option:selected").text();
    if(productSelected != "全部") {
        $.post(
            "/data/api/product/list/",
            {product:productSelected},
            function(data) {
                var optList = [];
                $.each(data.itemlist.language, function(idx, obj){
                    optList.push("<option>" + obj + "</option>");
                });
                $("#data-language-select").html('').append("<option>全部</option>").append(optList);

            }
        );
    }else {
        var all = "<option>全部</option>";
        $("#data-language-select").empty();
        $("#data-language-select").append(all);
        $("#data-channel-select").empty();
        $("#data-channel-select").append(all);
    }
});

$("#data-language-select").change(function() {
    var productSelected = $("#data-product-select option:selected").text();
    var languageSelected = $("#data-language-select option:selected").text();
    if(languageSelected != "全部") {
        $.post(
            "/data/api/product/list/",
            {
                product:productSelected,
                language:languageSelected
            },
            function(data) {
                var optList = [];
                $.each(data.itemlist.channel, function(idx, obj){
                    optList.push("<option>" + obj + "</option>");
                });
                $("#data-channel-select").html('').append("<option>全部</option>").append(optList);

            }
        );
    }else {
        var all = "<option>全部</option>";
        $("#data-channel-select").empty();
        $("#data-channel-select").append(all);
    }
});

$("#searchInput").bind('keypress', function(event) {
   if (event.keyCode == "13") {
       $("#searchBtn").click();
   }
});
app.controller('pluginsearch', function($scope, $http, $rootScope, dataService){
    function initSearchData(){
        $http({
            method: 'get',
            url: '/cm/getsearchplugindata/',
        }).success(function(data){
            $scope.data = data;
            data.channellist.unshift('全部');
            $scope.channel = data.channellist[0];
            data.plugintypelist.unshift('全部');
            $scope.pluginver = data.plugintypelist[0];
        });
    }

    $scope.search_plugin = function(){
        var channel_select = $scope.channel;
        var plugintype_select = $scope.plugintype;
        if($scope.channel == '全部'){
            return;
        }else if($scope.plugintype == '全部')
        {
            plugintype_select = '';
        }
        $http({
            method: 'post',
            url: '/cm/searchplugin/',
            data: {
                channel : channel_select,
                plugintype : plugintype_select
            }
        }).success(function(data){
            $rootScope.bottomdata_plugin = data;
        });

    };

    $scope.channel_change = function(){
        $http({
            method: 'post',
            url: '/cm/pluginsearch/channelchange/',
            data:{
                channel: $scope.channel
            }
        }).success(function(data){
            $scope.plugintypelist = data.plugintypelist;
            // console.log($scope.pluginverlist);
            data.plugintypelist.unshift('全部');
            $scope.plugintype = $scope.plugintypelist[0];
            // $scope.pluginver = data.pluginverlist[0];
        });
        // alert($scope.pluginver);
    }
    initSearchData();
});
app.controller('packagesearch', function($scope, $http, $rootScope, dataService){
    function initSearchData(){
        $http({
            method: 'get',
            url: '/cm/getsearchpackagedata/'
        }).success(function(data){
            $scope.data = data;
            // console.log($scope.data)
            data.channellist.unshift('全部');
            $scope.channel = data.channellist[0];
            data.packagelist.unshift('全部');
            $scope.apkver = data.packagelist[0];
        });
    }

    $scope.search_package = function(){
        var isallver = 0;
        if($scope.channel == '全部'){
            return;
        }
        if($scope.apkver == "全部")
        {
            isallver = 1;
        }

        $http({
            method: 'post',
            url: '/cm/searchpackage/',
            data: {
                channel : $scope.channel,
                apkver : $scope.apkver,
                isallver : isallver
            }
        }).success(function(data){
            $rootScope.bottomdata_package = data;
        });

    };

    $scope.channel_change = function(){
        $http({
            method: 'post',
            url: '/cm/packagesearch/channelchange/',
            data:{
                channel: $scope.channel
            }
        }).success(function(data){
            $scope.apkverlist = data.apkverlist;
            data.apkverlist.unshift('全部');
            // console.log($scope.apkverlist)
            $scope.apkver = $scope.apkverlist[0];
            // $scope.pluginver = data.pluginverlist[0];
        });
        // alert($scope.pluginver);
    }

    initSearchData();
});
app.controller('hostversearch', function($scope, $http, $rootScope, dataService){
    function initSearchData(){
        $http({
            method: 'get',
            url: '/cm/getsearchhostdata/'
        }).success(function(data){
            $scope.data = data;
            data.channellist.unshift('全部');
            $scope.channel = data.channellist[0];
            data.hostverlist.unshift('全部');
            $scope.hostver = data.hostverlist[0];
            data.filetypelist.unshift('全部');
            $scope.filetype = data.filetypelist[0];
        });
    }

    $scope.channel_change = function(){
        $http({
            method: 'post',
            url: '/cm/hostversearch/channelchange/',
            data:{
                channel: $scope.channel
            }
        }).success(function(data){
            $scope.hostverlist = data.hostverlist;
            data.hostverlist.unshift('全部');
            // console.log($scope.hostverlist)
            $scope.hostver = $scope.hostverlist[0];
            // $scope.pluginver = data.pluginverlist[0];
        });
        // alert($scope.pluginver);
    }

    $scope.search_hostver = function(){
        if($scope.channel == '全部'){
            return;
        }else if($scope.hostver == '全部'){
            return;
        }
        $http({
            method: 'post',
            url: '/cm/searchhostver/',
            data: {
                channel : $scope.channel,
                hostver : $scope.hostver
            }
        }).success(function(data){
            $rootScope.bottomdata_host = data;
        });        
    };

    $scope.ispackagelist = function(){
        // alert($scope.bottomdata_host.packagelist.length);
        if($scope.bottomdata_host.packagelist.length == 0){
            return false;
            }
        else{
            return true;
            }
        };

    $scope.ispluginlist = function(){
        if($scope.bottomdata_host.pluginlist.length == 0){
            return false;
        }
        else{
            return true;
        }
    }

    initSearchData();
});



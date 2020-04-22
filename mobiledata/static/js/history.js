/**
 * Created by kingsoft on 2016/7/16.
 */
function getId() {
    if (cookie("id") != "") {
        d = cookie('id');
        cookie('id', '', -1);
        return d;
    }
    return -1;
}
$("#historyBtn").click(function() {
    if ($("#searchInput").val() == '') {
        return;
    }
    fetchData(1);
});

$("#searchInput").bind('keypress', function(event) {
    if (event.keyCode == "13") {
        $("#historyBtn").click();
    }
});

function fetchData(pageNo) {
    var fileId = getId();
    if ($("#searchInput").val() != '') {
        fileId = -1;
    }
    $.post(
        "/data/api/pub/search/",
        buildParam(fileId, pageNo),
        function(data) {
            // alert(pageNo);
            addQueryPubPage(data.common.num_pages, pageNo);
            showData(data.itemlist);
        }
    );
}

function buildParam(fileId, pageNo) {
    var data = {};
    data['page'] = pageNo;
    if (fileId != -1) {
        //来源于ID参数
        data['filename_id'] = fileId;

    } else {
        //构建其他的参数
        var product = $("#data-product-select option:selected").text();
        var language = $("#data-language-select option:selected").text();
        var channel = $("#data-channel-select option:selected").text();
        var filename = $("#searchInput").val();
        if (product != '全部') {
            data['product'] = product;
        }
        if (language != '全部') {
            data['language'] = language;
        }
        if (channel != '全部') {
            data['channel'] = channel;
        }
        data['filename'] = filename;
    }
    return data;
}

function showData(data) {
    var queryTable = $("#js-query-pub-lists");
    var list = [];
    var keys = ['filename', 'language', 'channel', 'fileversion', 'svnversion',
        'datapath', 'publishtime'];
    if (data.length > 0) {
        $("#searchInput").val(data[0]['filename']);
    }
    $.each(data, function(idx, obj){
        var content = '<tr>';
        $.each(keys, function(idx1, obj1) {
            content += "<th>" + obj[obj1] + "</th>";
        });
        content += "</tr>";
        list.push(content);
    });
    queryTable.html('').append(list);
}
/**
* 1. 如果有Id传进来，直接显示查询结果
* 2. 输入限制条件，点击查询，显示结果，显示页码
* 3. 点击页码，数据改变
**/
function addQueryPubPage(pagenum, activepage) {
    if (typeof(pagenum) == 'undefined') return;
    $("#js-pub-query-page").show();
    var data = [];
    if (activepage != 1) {
        data.push('<li><a href="javascript:void(0)">' + '首页' + '</a></li>');
        data.push('<li><a href="javascript:void(0)">' + '上一页' + '</a></li>');
    }
    var max = parseInt(activepage) + 2;
    var min = parseInt(activepage) - 2;
    // alert(min + "--" + max);
    for (var i = min; i <= max; i++) {
        // var j = i - 2;
        if (i > 0 && i <= pagenum) {
            if (i == activepage) {
                data.push('<li class="active"><a href="javascript:void(0)">' + i + '</a></li>')
            } else {
                data.push('<li><a href="javascript:void(0)">' + i + '</a></li>')
            }
        }
    }

    if (activepage < pagenum) {
        data.push('<li><a href="javascript:void(0)">' + '下一页' + '</a></li>');
        data.push('<li><a href="javascript:void(0)">' + '末页' + '</a></li>');
    }
    data.push('<li><a href="javascript:void(0)">' + '共' + pagenum + '页' + '</a></li>');
    $("#js-pub-query-page").html('').append(data).find('li').on('click', function () {
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
            fetchData(pageNo);
        }
    });
}
fetchData(1);

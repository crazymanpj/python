/**
 * Created by kingsoft on 2018/1/16.
 */

var host1 = "http://10.12.128.129:8080";
var host2 = "http://10.20.220.143";
var host = host1;
var urls = {
    "dopack": host + "/dbpackage/makepackage",
    "getproductlist": host + "/dbpackage/getproductlist",
    "gettyrnolist": host + "/dbpackage/gettrynolist",
    "gethistroypackages" : host + "/dbpackage/getallmakepacketinfo",
    "getiffinish": host + "/dbpackage/getresultbytaskid",
    "stoppack": host + "/dbpackage/stopmakepackages",
    "getitemlist": host + "/dbpackage/getpartnerlist"
};

var allProducts = {
    "duba": '1',
    "other": '2'
};
var messages = {
    "dopack": "开始打包，稍后打包记录中会更新本次打包记录！",
    "packing": "你查询的任务还在打包中！",
    "packed": "你查询的任务已经完成，更新列表中..."
};

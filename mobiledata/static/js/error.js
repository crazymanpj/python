errId = cookie("errId");
msg = cookie("msg");
if (errId != '') {
    cookie("errId", "", -1);
    cookie("msg", "", -1);
    var errContent = "";
    /**
     * 1. 表示重做数据失败
     * 2. 表示对比数据失败
     * 3. 制作数据失败
     * 4. 发布数据失败
     * @type {Array}
     */
    var pageAddress = ["/web/index.html", "/web/index.html", "/web/index.html", "/web/index.html", "/web/index.html"];
    // var pageAddress = ["", "/Platform/index.html", "/Platform/index.html", "/Platform/index.html", "/Platform/index.html"];
    var jumpLink = "";
    var showErr = "";
    if (errId == 0) {
        errContent = "浏览器不支持IE，请使用其他浏览器";
        jumpLink = "<br><br></bt><a style='color:red' href='" + pageAddress[errId] + "'><b>返回前页</b></a>";
        showErr = errContent  + jumpLink;
    } else {
        if (msg == -1) {
            errContent = "请求超时，找管理员要点安慰吧！";
            errId = 0;
        } else if (errId == 1) {
            //做数据失败
            errContent = "重做数据失败！";
        } else if (errId == 2) {
            errContent = "对比数据失败！";
        } else if (errId == 3) {
            errContent = "制作数据失败！";
        } else if (errId == 4) {
            errContent = "发布数据失败！";
        }
        errContent += "错误信息:   " + msg + "!";
        jumpLink = "<br><br></bt><a style='color:red' href='" + pageAddress[errId] + "'><b>返回前页</b></a>";
        showErr = errContent  + jumpLink;
    }
    $("#errContent").html('').html(showErr);
}




/**
 * author：wusong  2016.4.21
 */


/**
 * 时间对象的格式化;
 */
Date.prototype.format = function (format) {
    var o = {
        'M+': this.getMonth() + 1,
        'd+': this.getDate(),
        'h+': this.getHours(),
        'm+': this.getMinutes(),
        's+': this.getSeconds(),
        'q+': Math.floor((this.getMonth() + 3) / 3),
        'S': this.getMilliseconds()
    };
    if (/(y+)/.test(format) || /(Y+)/.test(format)) {
        format = format.replace(RegExp.$1, (this.getFullYear() + '').substr(4 - RegExp.$1.length));
    }
    for (var k in o) {
        if (new RegExp('(' + k + ')').test(format)) {
            format = format.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k] : ('00' + o[k]).substr(('' + o[k]).length));
        }
    }
    return format;
};
/*
 * 时间戳转日期
 */
function timeFormat(timestamp) {
    var timestamp = parseInt(timestamp);
    return (new Date(timestamp).format('yyyy-MM-dd hh:mm:ss'));
}

var changeTheme = {
    init: function () {
        if (cookie('theme')) {
            $('#js-theme-css').attr('href', '/static/css/bootstrap.' + cookie('theme') + '.min.css');
            $('#js-theme-choose a[data-theme="' + cookie('theme') + '"]').parent().addClass('active').find('span').show();
        } else {
            $('#js-theme-css').attr('href', '/static/css/bootstrap.slate.min.css');
            $('#js-theme-choose a:eq(0)').parent().addClass('active').find('span').show();
        }
    },
    bind: function () {
        $('#js-theme-choose a').on('click', function () {
            var theme = $(this).attr('data-theme');
            $('#js-theme-choose li').removeClass('active');
            $('#js-theme-choose span').hide();
            $(this).parent().addClass('active').find('span').show();
            $('#js-theme-css').attr('href', '/static/css/bootstrap.' + theme + '.min.css');
            cookie('theme', theme, {expires: 3600 * 24 * 365, path: "/"});//失效时间 以s为单位

        });
    }
};

var dataManager = {
    bind: function(){
        $('#js-data-manager a').on('click', function(){
            var selectaction = $(this).attr('button-action');
            if (selectaction == 'addchannel'){
                $('#js-addchannel').modal();
            } else if(selectaction == 'addhostver'){
                $('#js-addhostver').modal();
            }

        });
    }
};

var user = {
    //登录状态
    state: function () {
        var nickname = cookie('nickname') || cookie('email');
        if (nickname) {
            $('#js-not-login').hide();
            $('#js-nickname').html('<span class="glyphicon glyphicon-user"></span> ' + nickname + ' <span class="caret"></span>');
            $('#js-is-login').show();
            $('#js-manager-iscanshow').show();
            return true;
        } else {
            return false;
        }
    },
    //表单元素验证
    check: function () {
        var email = arguments[0].email,
            password = arguments[0].password,
            re_password = arguments[0].re_password,
            action = arguments[0].action;
        //对电子邮件的验证
        var email_test = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;

        //注册
        if (action == 'reg') {
            $('#js-reg-form input').removeClass('err-background');
            if (!email) {
                $('#js-reg-form input[name="email"]').val('').addClass('err-background').attr('placeholder', '请输入邮箱').focus();
                return false;
            } else if (!email_test.test(email)) {
                $('#js-reg-form input[name="email"]').val('').addClass('err-background').attr('placeholder', '邮箱格式不正确').focus();
                return false;
            }
            if (!password) {
                $('#js-reg-form input[name="password"]').val('').addClass('err-background').attr('placeholder', '请输入密码').focus();
                return false;
            } else if (password.length < 6) {
                $('#js-reg-form input[name="password"]').val('').addClass('err-background').attr('placeholder', '密码长度应大于等于6').focus();
                return false;
            }

            if (!re_password) {
                $('#js-reg-form input[name="re_password"]').val('').addClass('err-background').attr('placeholder', '请再输入密码').focus();
                return false;
            }
            if (password && re_password && password != re_password) {
                $('#js-reg-form input[name="password"],#js-reg-form input[name="re_password"]').val('').addClass('err-background').attr('placeholder', '两次密码不一致').focus();
                return false;
            }
        }

        //登录
        if (action == 'login') {
            $('#js-login-form input').removeClass('err-background');
            if (!email) {
                $('#js-login-form input[name="email"]').val('').addClass('err-background').attr('placeholder', '请输入邮箱').focus();
                return false;
            } else if (!email_test.test(email)) {
                $('#js-login-form input[name="email"]').val('').addClass('err-background').attr('placeholder', '邮箱格式不正确').focus();
                return false;
            }
            if (!password) {
                $('#js-login-form input[name="password"]').val('').addClass('err-background').attr('placeholder', '请输入密码').focus();
                return false;
            } else if (password.length < 6) {
                $('#js-login-form input[name="password"]').val('').addClass('err-background').attr('placeholder', '密码长度应大于等于6').focus();
                return false;
            }
        }


        return true;

    },
    login: function () {
        var email = $('#js-login-form input[name="email"]').val(),
            password = $('#js-login-form input[name="password"]').val();

        if (user.check({email: email, password: password, action: 'login'})) {
            $.post("/cm/userlogin/", {email: email, password: password},
                function (data) {
                    if (data.errorcode == 0) {
                        $('#js-login-form .modal-body').html('<p class="center-block">登录成功！</p>');
                        user.state();
                        setTimeout(function () {
                            $('#js-login').modal('hide');
                        }, 2000)
                        window.location.reload();
                    } else {
                        $("#passwd-err-tip").show();
                    }
                });
        }
    },
    reg: function () {
        var email = $('#js-reg-form input[name="email"]').val(),
            password = $('#js-reg-form input[name="password"]').val(),
            re_password = $('#js-reg-form input[name="re_password"]').val();
        if (user.check({email: email, password: password, re_password: re_password, action: 'reg'})) {
            $.post("/cm/regist/", {email: email, password: password},
                function (data) {
                    if (data.errorcode == 0) {
                        var nickname = cookie('email') || '请设置昵称';
                        $('#js-reg-form .modal-body').html('<p class="center-block">注册成功！返回后请登录...</p>');
                        $('#js-not-login').hide();
                        $('#js-nickname').html('<span class="glyphicon glyphicon-user"></span> ' + nickname + ' <span class="caret"></span>');
                        $('#js-is-login').show();
                        setTimeout(function () {
                            $('#js-reg').modal('hide');
                        }, 2000)
                        window.location.reload();
                    }
                    else {
                        $("#reg-err").text('').text(data.msg);
                        $("#reg-err").show();
                        setTimeout(function() {
                            $("#reg-err").hide();
                        }, 3000);
                    }
                });
        }
    },
    //事件绑定
    bind: function () {
        //注册
        $('#js-reg-submit').on('click', function () {
            user.reg();
        });
        //登录
        $('#js-login-submit').on('click', function () {
            user.login();
        });
        $(document).keypress(function (e) {
            // 回车键事件
            if (e.which == 13) {
                if ($('#js-login').css('display') == 'block') {
                    user.login();
                }
                if ($('#js-reg').css('display') == 'block') {
                    user.reg();
                }
            }
        });
        //输入状态去掉警告背景
        $('#js-login-form,#js-reg-form').find('input').on('input propertychange', function () {
            $(this).removeClass('err-background');
        });
    },
    init: function () {
        user.state();
        user.bind();
    }
};
user.state();
changeTheme.init();
$(function () {
    changeTheme.bind();
    changeTheme.init();
    dataManager.bind();
    user.init();
    $("#password").focus(function() {
        $("#passwd-err-tip").hide();
    });
    $("#username").focus(function() {
        $("#passwd-err-tip").hide();
    });

});

var app = angular.module('wsAPP', ['nya.bootstrap.select']);

// 创建获取数据服务
app.run(function($rootScope) {
    $rootScope.$on('handleCompareResultEmit', function(event, args) {
        $rootScope.$broadcast('handleCompareResultBroadcast',args);
    });

});
app.service('dataService', function ($http, $q) {
    this.get = function () {
        var product = arguments[0].product || null,
            hostver = arguments[0].hostver || null,
            channel = arguments[0].channel || null,
            apkver = arguments[0].apkver || null,
            page = arguments[0].page || 1,
            data = [];
        var params = {};
        if (product != '全部') {
            params['product'] = product;
        }
        if (hostver != '全部') {
            params['hostver'] = hostver;
        }
        if (channel != '全部') {
            params['channel'] = channel;
        }
        if (apkver != '全部') {
            params['apkver'] = apkver;
        }
        params['status'] = status;
        params['page'] = page;
        var deferred = $q.defer(); // 声明延后执行，表示要去监控后面的执行
        $http({
            method: 'post',
            url: '/cm/getpublishdata/',
            data: params
        }).success(function (data, status, headers, config) {
            deferred.resolve(data);  // 声明执行成功，即http请求数据成功，可以返回数据了
        }).error(function (data, status, headers, config) {
            deferred.reject(data);   // 声明执行失败，即服务器返回错误
        });
        return deferred.promise;   // 返回承诺，这里并不是最终数据，而是访问最终数据的API
    }
});
app.directive('selectPickr', function ($timeout) {
    return {
        link: function (scope, element, attr) {
                $timeout(function () {
                    element.selectpicker('refresh');
                });
        }
    };
});

function getRandom(n) {
    return Math.floor(Math.random() * n)
}

function setRandomGif() {
    var src = "/static/img/" + complexData.gifs[getRandom(complexData.gifs.length)];;
    $("#loading").attr("src", src);
}

function getRandomChicken() {
    return complexData.words[getRandom(complexData.words.length)];
}

// 创建验证码
function createCode() {
    var code = "";
    var codeLength = 4;
    var checkCode = document.getElementById("code");
    var random = new Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z');
    for (var i = 0; i < codeLength; i++) {
        var index = Math.floor(Math.random() * 62);
        code += random[index];
    }
    checkCode.value = code;
}

// 校验验证码
function validateCode() {
    // 获取生成的验证码
    var checkCode = document.getElementById("code").value.toUpperCase();
    // 获取输入的验证码
    var inputCode = document.getElementById("captcha").value.toUpperCase();
    if (inputCode.length <= 0) {
        alert("请输入验证码！");
        return false;
    } else if (inputCode !== checkCode) {
        alert("验证码输入错误！");
        createCode();
        document.getElementById("captcha").value = "";
        return false;
    } else {
        return true;
    }
}
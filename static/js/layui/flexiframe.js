// 使用前先将子页面文档声明改为
//<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
function setIframeHeight(iframe) {
    if (iframe) {
        var iframeWin = iframe.contentWindow || iframe.contentDocument.parentWindow;
        if (iframeWin.document.body) {
            iframe.height = iframeWin.document.body.scrollHeight;
        }
    }
};
$(".flexiframe").each(function (index) {
    var that = $(this);
    (function () {
        setInterval(function () {
            setIframeHeight(that[0])
        }, 200)
    })(that)
});
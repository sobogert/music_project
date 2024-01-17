window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    let scrollHeight = (window.innerHeight / 4);
    let scale = 0.4;

    // Set min size font
    if (document.body.scrollTop > scrollHeight || document.documentElement.scrollTop > scrollHeight) {
        document.getElementById("_marquee").style.fontSize = "34px";
        let duds = document.getElementsByClassName("duddely");
        for (let i = 0; i < duds.length; i++) {
            duds[i].style.height = "34px";
            duds[i].style.width = "27px";
            duds[i].style.marginLeft = "14px";
        }
    }
    else {
        // Resize font as you scroll down
        let currSize = 96 - (document.documentElement.scrollTop * scale);
        if (currSize < 40) {
            currSize = 40;
        }
        let currSizeStr = String(currSize) + "px";
        document.getElementById("_marquee").style.fontSize = currSizeStr;

        // Calc duddely height
        let currHeight = 97 - (document.documentElement.scrollTop * scale);
        if (currHeight < 34) {
            currHeight = 34;
        }
        let currHeightStr = String(currHeight) + "px";

        // Calc duddely width
        let currWidth = 75 - (document.documentElement.scrollTop * scale);
        if (currWidth < 27) {
            currWidth = 27;
        }
        let currWidthStr = String(currWidth) + "px";

        // Calc duddely left margin
        let currMargin = 32 - (document.documentElement.scrollTop * scale);
        if (currMargin < 12) {
            currMargin = 12;
        }
        let currMarginStr = String(currMargin) + "px";

        let duds = document.getElementsByClassName("duddely");
        for (let i = 0; i < duds.length; i++) {
            duds[i].style.height = currHeightStr;
            duds[i].style.width = currWidthStr;
            duds[i].style.marginLeft = currMarginStr;
        }
    }
}
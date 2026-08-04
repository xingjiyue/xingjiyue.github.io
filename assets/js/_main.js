$(document).ready(function () {
  const scssLarge = 925;
  const scssMastheadHeight = 70;

  var bumpIt = function () {
    $("body").css("padding-bottom", "0");
    $("body").css("margin-bottom", $(".page__footer").outerHeight(true));
  };

  var didResize = false;
  $(window).resize(function () {
    didResize = true;
  });
  setInterval(function () {
    if (didResize) {
      didResize = false;
      bumpIt();
    }
  }, 250);
  bumpIt();

  fitvids();

  $(".author__urls-wrapper button").on("click", function () {
    $(".author__urls").fadeToggle("fast", function () {});
    $(".author__urls-wrapper button").toggleClass("open");
  });

  jQuery(window).on("resize", function () {
    if ($(".author__urls.social-icons").css("display") == "none" && $(window).width() >= scssLarge) {
      $(".author__urls").css("display", "block");
    }
  });

  $("a").smoothScroll({
    offset: -scssMastheadHeight,
    preventDefault: false,
  });
});

(function(){
  function fixGrid(){
    var m=window.innerWidth<=768;
    var g=document.querySelector('.dh-body .prof-hero-grid');
    if(g){g.style.gridTemplateColumns=m?'repeat(2,1fr)':'repeat(4,1fr)';g.style.gridTemplateRows=m?'repeat(4,auto)':'repeat(2,1fr)';}
  }
  var _sw=window.switchTab;
  window.switchTab=function(n){if(_sw)_sw.apply(this,arguments);if(window.innerWidth<=768){var nav=document.getElementById('nav-tabs'),ov=document.getElementById('mobile-nav-overlay');if(nav)nav.classList.remove('mobile-open');if(ov)ov.classList.remove('active');}};
  document.addEventListener('DOMContentLoaded',function(){
    fixGrid();var t;window.addEventListener('resize',function(){clearTimeout(t);t=setTimeout(fixGrid,100);});
    var nav=document.getElementById('nav-tabs');
    if(nav){var sx=null;
      nav.addEventListener('touchstart',function(e){sx=e.touches[0].clientX;},{passive:true});
      nav.addEventListener('touchmove',function(e){if(sx!==null&&(sx-e.touches[0].clientX)>55){nav.classList.remove('mobile-open');var ov=document.getElementById('mobile-nav-overlay');if(ov)ov.classList.remove('active');sx=null;}},{passive:true});
      nav.addEventListener('touchend',function(){sx=null;},{passive:true});
    }
  });
})();

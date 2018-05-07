	_.templateSettings = {
      evaluate : /\{\[([\s\S]+?)\]\}/g,
      interpolate : /\{\{([\s\S]+?)\}\}/g
    };

	$.fn.extend({
		animateCss: function(animationName, callback) {
			var animationEnd = (function(el) {
				var animations = {
				animation: 'animationend',
				OAnimation: 'oAnimationEnd',
				MozAnimation: 'mozAnimationEnd',
				WebkitAnimation: 'webkitAnimationEnd',
				};

				for (var t in animations) {
					if (el.style[t] !== undefined) {
						return animations[t];
					}
				}
			})(document.createElement('div'));

			this.addClass('animated ' + animationName).one(animationEnd, function() {
				$(this).removeClass('animated ' + animationName);

				if (typeof callback === 'function') callback();
			});

			return this;
		},
	});

	var contadores = (function() {

		function count(print, max){
			var counter = { var: 0 };
			TweenMax.to(counter, 3, {
				var: max, 
				onUpdate: function () {
					var number = Math.ceil(counter.var);
					print.html(number);
				},    
				ease:Circ.easeOut
			});
		}

		function initWaypoint(elements){
			var waypoint = new Waypoint({
				element: document.getElementById('contadores'),
				handler: function(direction) {
					count(elements[0], 150);
					count(elements[1], 3);
					count(elements[2], 180);

					this.destroy();
				},
				offset: '80%',
	    		triggerOnce: true 
			});
		}

		let instancia = {
			listElements: [],

			getElements: function(elements) {
				this.listElements = elements;
			},

			doCont: function() {
				var elements = this.listElements;
				initWaypoint(elements);
			}
		}
		return instancia;
	});

	var sliderMain = (function() {

		var	isMobile = false;

		var view = {
			$contentMain : $('.content-marcas-main'),
			$requiez : $('#mainRequiez'),
			$labenze : $('#mainLabenze'),
			$okamura : $('#mainOkamura'),
			$infiniti : $('#mainInfiniti'),
			$grupo : $('#mainGrupoRequiez'),
		}

		var tmp = {
			tmpGrupoRequiez : _.template(view.$grupo.html()),
			tmpRequiez : _.template(view.$requiez.html()),
			tmpLabenze : _.template(view.$labenze.html()),
			tmpOkamura : _.template(view.$okamura.html()),
			tmpInfiniti : _.template(view.$infiniti.html()),
		}

		$('.event-marca').click(eventMarca);

		function _init(){

			if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|ipad|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(navigator.userAgent) 
			    || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(navigator.userAgent.substr(0,4))) { 
			    isMobile = true;
			}
			console.log(isMobile);

			view.$contentMain.append(tmp.tmpGrupoRequiez({ mobile : isMobile}));
			initParallax();
		}

		function initParallax(){
			var scene = document.getElementById('scene');
			var parallaxInstance = new Parallax(scene);
		}

		function eventMarca(event){
			var tagMarca = $(this)[0].id;
			$('.event-marca').removeClass('is-selected');
			$('#'+tagMarca).addClass('is-selected');

			var FindScene = view.$contentMain.find('#scene');

			if( FindScene.length > 0 ){
				FindScene.animateCss('bounceOutRight', function(event) {
					$('#scene').remove();
					addScene(tagMarca);
				});
			}else{
				addScene(tagMarca);
			}
       	}

       	function addScene(tagMarca){
       		if( tagMarca == 'grupoRequiez' ){
				$('.content-marcas-main').append(tmp.tmpGrupoRequiez({ mobile : isMobile}));
				var scene = document.getElementById('scene');
				var parallaxInstance = new Parallax(scene);
			}else if( tagMarca == 'requiez' ){
				$('.content-marcas-main').append(tmp.tmpRequiez({ mobile : isMobile}));
				var scene = document.getElementById('scene');
				var parallaxInstance = new Parallax(scene);
			}else if( tagMarca == 'labenze'){
				$('.content-marcas-main').append(tmp.tmpLabenze({ mobile : isMobile}));
				var scene = document.getElementById('scene');
				var parallaxInstance = new Parallax(scene);
			}else if( tagMarca == 'okamura'){
				$('.content-marcas-main').append(tmp.tmpOkamura({ mobile : isMobile}));
				var scene = document.getElementById('scene');
				var parallaxInstance = new Parallax(scene);
			}else if( tagMarca == 'infiniti'){
				$('.content-marcas-main').append(tmp.tmpInfiniti({ mobile : isMobile}));
				var scene = document.getElementById('scene');
				var parallaxInstance = new Parallax(scene);
			}
       	}

        _init();
	});

	$(document).ready(function(){
		
		var flagMenuFix = false;
          $(window).scroll(function(){
            
            if ($(this).scrollTop() > 1 && flagMenuFix == false ) {
              $('.navbar').addClass('header-fix-active');
              flagMenuFix = true;
            }else if($(this).scrollTop() <= 1 && flagMenuFix == true){
              flagMenuFix = false;
              $('.navbar').removeClass('header-fix-active');
            }
          });
  
	});
(function(){

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
					count(elements[0], 100);
					count(elements[1], 200);
					count(elements[2], 300);

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

		var view = {
			$contentMain : $('.content-marcas-main'),
			$requiez : $('#mainRequiez'),
		}

		var tmp = {
			tmpRequiez : _.template(view.$requiez.html()),
		}

		$('.event-marca').click(eventMarca);

		function _init(){
			view.$contentMain.append(tmp.tmpRequiez());
			initParallax();
		}

		function initParallax(){
			var scene = document.getElementById('scene');
			var parallaxInstance = new Parallax(scene);
		}

		function eventMarca(event){
			view.$contentMain.find('#scene').animateCss('bounceOutRight', function(event) {
				
				$('#scene').remove();

				$('.content-marcas-main').append(tmp.tmpRequiez());

				var scene = document.getElementById('scene');
				var parallaxInstance = new Parallax(scene);
			});
       	};

        _init();
	});

	$(document).ready(function(){
		console.log('main.js?ver=0.0.9');

		var cont1 = new contadores();
		cont1.getElements([$('.counter1'), $('.counter2'), $('.counter3')]);
		cont1.doCont();


		var slider = new sliderMain();
	});

})();
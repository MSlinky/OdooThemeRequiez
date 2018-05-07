from odoo import http
from odoo import models, fields, api
from odoo.http import Response

class RequiezController(http.Controller):
	@http.route('/Marcas/<name>', auth='public', website=True)
	def index(self, name):
		data = {}
		if name == 'Requiez':
			data['nombre'] = 'Requiez'
			data['urlLogo'] = '<img src="/theme_requiez/static/img/marcas/req.jpg"/>'
			data['weburl'] = 'https://requiez.com/'
			data['webname'] = '<a href="'+data['weburl']+'" target="_blank">www.requiez.com</a>'
			data['title'] = '<span class="light">OFICINAS </span>DISEÑADAS<br/> <span class="light">PARA UNA </span> RELACIÓN <br/><span class="light">MÁS </span>DIRECTA <span class="light">Y</span> EXITOSA'
			data['content'] = "El espacio laboral es un universo que tiene su propio lenguaje; sus confines están delimitados por la funcionalidad y el máximo aprovechamiento, y su éxito se mide en horas productivas, ideas brillantes y trabajo en equipo. Reqüiez ofrece una amplia gama de productos que responden a las demandas de volumen, ergonomía y diseño funcional en áreas de trabajo que, además, contemplen el diseño como parte integral de sillasu ambiente. <br><br/> La especialización es clave. Por eso, Reqüiez fabrica sillones ejecutivos, sillas operativas y de trabajo, bancos altos, bancas y confortables para salas de espera o espacios de colectividad; una línea completa de visitantes y eventos especiales, pupitres para capacitación, sillas y bancos industriales, y una variedad de accesorios que complementan nuestros diseños, de acuerdo con los requerimientos específicos de uso y aplicación. <br><br/> La identidad es un elemento clave en cualquier oficina. Por ello, cada mobiliario que ofrece Reqüiez puede ser personalizado al gusto del usuario. <br><br/> Nuestros insumos son reciclados y de potencial reutilización, además de introducir la línea ejecutiva Serie Staff, hecha en un 98% de material reciclado. <br><br/>Nuestra garantía está respaldada por la calidad de los elementos empleados en cada silla, y los procesos calificados para su fabricación. Todos los productos de Reqüiez cumplen con estándares internacionales de calidad, así como las pruebas de desempeño, funcionalidad y ergonomía que garantizan una vida útil y duradera."
			data['img'] = [
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/re-1750-sillon-retro-respaldo-alto-tapiz-eco-leather.jpg"/>',
				'<img class="img-marca" src="/theme_requiez/static/img/26869798_1403551743089899_7789104937132097536_n.jpg"/>',
				'<img class="img-marca" src="/theme_requiez/static/img/27581094_149635855746057_1340368450228322304_n.jpg"/>'
				]
		elif name == 'Labenze' :
			data['nombre'] = 'Labenze'
			data['urlLogo'] = '<img src="/theme_requiez/static/img/marcas/labenze.jpg"/>'
			data['weburl'] = 'http://labenze.com/'
			data['webname'] = '<a href="'+data['weburl']+'" target="_blank">www.labenze.com</a>'
			data['title'] = '<span class="light">UNA SOBREDOSIS DE </span><br/>COLOR<span class="light">, </span> ARMONÍA<br/><span class="light"> Y MULTIPREMIADAS</span><br/> COLECCIONES'
			data['content'] = "La búsqueda de la perfección en diseño exige abrir las ventanas de la mente. Concebir el espacio siempre como una posibilidad de creación, como un lienzo que espera ser habitado por brochazos de color y formas que rebasan los confines del marco. En Labenze, entendemos el diseño como una exploración de belleza aplicada en el entorno personal, una expresión de buen gusto y distinción. <br/><br/>Rompemos esquemas de interiorismo al ofrecer mobiliario diseñado por firmas italianas reconocidas a nivel mundial, e integrarlos a ambientes de uso residencial internos y externos, espacios públicos y corporativos. Los muebles incluidos en el catálogo son piezas clave en áreas que priorizan la pasión por el diseño, que encuentran en sus curvas y fibras el punto de partida para inspirar. Cada pieza es cuidadosamente seleccionada de los lanzamientos de nuestras firmas en las principales ferias europeas, con tendencias que reinventan el imaginario de interiorismo mexicano. <br/><br/>Labenze, en su ecléctica opción de sillas, sillones y mesas, despliega formas caprichosas, composiciones visuales que retan los convencionalismos en mobiliario contemporáneo, y abren la puerta la innovación en su faceta más experimental, en la que converge el buen gusto con la imperativa necesidad de comodidad. Su diseño no escatima en ergonomía y resistencia en sus materiales, con tecnología europea para uso rudo, exteriores y cambios abruptos de temperatura. <br/><br/>Al pertenecer a Grupo Reqüiez, cuenta con cobertura a nivel nacional para la comercialización de sus productos. Los socios de negocio que elegimos cuentan con perfiles diversos —profesionales del diseño de interiores, importantes despachos de diseño, mueblerías y tiendas de decoración— que, a su vez, cuentan con proyectos de tipo residencial, comercial y corporativo, y atienden a un selecto grupo de usuarios. <br/><br/>No importa si se trata de un lobby caprichoso en un hotel boutique, del rincón exquisito de algún lounge, o un rincón delicadamente diseñado del hogar; cada pieza de Labenze es un objeto destinado a lo extraordinario, imán de suspiros y miradas."
			data['img'] = [
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/Labenze_web_marca.jpg"/>',
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/labenze1.jpg"/>',
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/labenze2.jpg"/>'
			]
		elif name == 'Okamura' :
			data['nombre'] = 'Okamura'
			data['urlLogo'] = '<img src="/theme_requiez/static/img/marcas/okamrua_logo-min.png"/>'
			data['weburl'] = 'http://okamuramexico.com/'
			data['webname'] = '<a href="'+data['weburl']+'" target="_blank">www.okamuramexico.com</a>'
			data['title'] = '<span class="light">LA MÁS </span>EFICIENTE<br/><span class="light">Y LA</span> MEJOR <br/>PRESENCIA <span class="light">DE OFICINA</span>'
			data['content'] = "Okamura es una marca de origen Japonés con los estándares de calidad y diseño más altos en sillas de oficina. Una marca con más de 60 años en el mercado japonés se incluye en el portafolio de productos de Grupo Reqüiez para satisfacer las necesidades de los más exigentes en cuanto diseño, ergonomía y calidad. Creando la primera silla Okamura en 1961 llamada Type22 comenzó una historia de principios ergonómicos y conocimiento científico para el desarrollo de productos innovadores en el mercado japonés y posteriormente en el mundo.<br/><br/>Siempre en busca de ofrecer al mercando nuevas propuestas, Okamura se apoya en diseñadores como Giorgetto Giugiaro fundador de Giugiaro Design, despacho de diseño reconocido mundialmente, para mezclar el diseño Italiano con la tecnología y calidad Japonesa. Diseños como Contessa, CP y Luce son ejemplos de una sinergia de trabajo entre oriente y occidente que da como resultado un producto que excede necesidades de un mercado global.<br/><br/>Estas colaboraciones con distintos diseñadores no solamente enriquecen las características de los productos sino que le dan al usuario una frescura en propuestas y es lo que Okamura busca continuamente.<br/><br/>Okamura, rankeada entre las primeras 3 empresas de fabricación de muebles de oficina a nivel mundial atiende proyectos de manera global en los 5 continentes por medio de colaboraciones con empresas estratégicamente seleccionadas para dar acceso a mercado global. Productos como Contessa y Leopard han roto paradigmas en los mercados globales por lo que han conseguido posicionarse como unos de los productos icónicos de esta marca tanto por su diseño como por su calidad y tecnología."
			data['img'] = [
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/Okamura_web_marca.jpg"/>',
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/okamura1.jpg"/>',
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/okamura2.jpg"/>'
			]
		elif name == 'Infiniti' :
			data['nombre'] = 'Infiniti'
			data['urlLogo'] = '<img src="/theme_requiez/static/img/marcas/logoInfiniti.png"/>'
			data['weburl'] = 'https://infinitidesignmexico.com/'
			data['webname'] = '<a href="'+data['weburl']+'" target="_blank">www.infinitidesignmexico.com</a>'
			data['title'] = 'CREATIVIDAD<span class="light">, </span><br/>INNOVACIÓN<br/> <span class="light">TECNOLÓGICA</span><br/> CULTURA <span class="light">DEL DISEÑO</span>'
			data['content'] = "Son las palabras clave para comprender la filosofía de Infiniti, una marca joven (nace en 2008), en pleno desarrollo, que propone complementos de decoración concebidos para trabajar, compartir, descansar, acoger.<br/><br/>Como se vislumbra de su nombre, Infiniti no pone límites a las posibilidades expresivas de cada uno: su diseño, interpretado como una experiencia sensorial propiamente dicha, nace de la proximidad con lugares, culturas y estilos de vida diferentes.<br/><br/>Así pues, el espíritu cosmopolita de la marca se manifiesta en una misión única: proponer objetos que pertenezcan a la vida cotidiana de cualquier persona, en cualquier lugar que se encuentre. Sin fronteras, el mundo Infiniti se mueve de Barcelona a Nueva York, de Londres a Tokyo, de Berlín a Venecia y jamás se detiene. <br/><br/>Infiniti se inspira en valores dinámicos, juveniles y vitales: la energía, entendida como conjunto de formas y colores que interpretan un ritmo contemporáneo y otorgan vitalidad y alegría a los lugares donde se vive; el dinamismo, típico de un modo de pensar listo para la sorpresa y el cambio; el estilo, que se identifica en el culto de los detalles y en las combinaciones innovadoras entre materiales y colores; la creatividad, es decir el deseo de atreverse, sorprender y divertirse. Aún más, la innovación, que para Infiniti significa desplazar el horizonte todavía más allá, buscando formas y materiales nuevos; el diseño, resultado de un estudio apasionado; el espíritu cosmopolita, porque Infiniti habita el mundo, gracias a su estilo completamente italiano, hecho de calidad, estética y originalidad. Y, por último, la emoción. Porque Infiniti se propone ser un viaje en el planeta para captar los colores y los sentimientos, plasmando instantes de vida real.<br/><br/>Los productos de Infiniti son respuestas avanzadas a las decisiones del vivir moderno, o sea, no solo objetos útiles, sino concebidos también para respetar los principios de la ergonomía, ofrecer el placer a la vista, garantizar el reciclaje y proponer soluciones inteligentes. <br/><br/>Dando expresión a la vida cotidiana, constantemente sometida a los cambios, también Infiniti se transforma y no se detiene un instante, siempre atenta a la evolución de la moda y las tendencias. <br/><br/>Por este motivo la empresa se dedica a la investigación constante, cuyo valor añadido es el soporte de diseñadores internacionales afirmados y de jóvenes creativos que, gracias a Infiniti, llegan a valorizar su propio talento. <br/><br/>Con el apoyo de quienes ofrecen su propia aportación −empleados, socios y usuarios− la marca evoluciona continuamente. En el mundo Infiniti, sumergido en una comunicación participativa, el cliente es el punto central en torno al cual se desarrollan las ideas. El propósito es el de brindar productos siempre de vanguardia, sin olvidar estilo y técnica, pero ofreciendo una respuesta atenta a las exigencias manifestadas por la clientela."
			data['img'] = [
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/Infiniti_web_marca.jpg"/>',
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/infiniti1.jpg"/>',
				'<img class="img-marca" src="/theme_requiez/static/img/marcas/infiniti2.jpg"/>'
			]
		else:
			data['nombre'] = 'Marca no encontrada'
		return http.request.render('theme_requiez.marcas', {
			'nombreMarca': data
		})

	@http.route('/Marcas', auth='public', website=True)
	def errorMarca(self, **kw):
		data = {}
		data['nombre'] = 'Marca no encontrada'
		data['weburl'] = '-'
		data['webname'] = '-'
		data['title'] = '-'
		data['content'] = "-"
		data['img'] = '-'
		return http.request.render('theme_requiez.marcas', {
			'nombreMarca': data
		})
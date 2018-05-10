from odoo import http

class Requiez(http.Controller):
    @http.route('/inicio', type='http', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('theme_requiez.inicio', {})
# from odoo import http


# class PosProductnameDisplay(http.Controller):
#     @http.route('/pos_productname_display/pos_productname_display', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_productname_display/pos_productname_display/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_productname_display.listing', {
#             'root': '/pos_productname_display/pos_productname_display',
#             'objects': http.request.env['pos_productname_display.pos_productname_display'].search([]),
#         })

#     @http.route('/pos_productname_display/pos_productname_display/objects/<model("pos_productname_display.pos_productname_display"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_productname_display.object', {
#             'object': obj
#         })


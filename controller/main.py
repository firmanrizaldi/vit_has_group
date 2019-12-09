
from odoo import api, fields, models
import time
import datetime
import logging
_logger = logging.getLogger(__name__)
from odoo.http import request
from odoo import http


class BaseWebsite(http.Controller):
    @http.route('/vit/index', type='http', auth='public', website=True)
    def index(self, **kw):
        user_obj = request.env['res.users']
        user = user_obj.browse (request.uid)
        is_admin = user.has_group('base.group_system')

        return request.render('vit_has_group.index', {
            'is_admin' : is_admin
        })




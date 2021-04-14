# Copyright 2021 AKRETION
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel


class PackageUpdateParam(Datamodel):
    _name = "package.update.param"

    ref = fields.String(required=True, allow_none=False)
    weight = fields.Float(required=False)
    tracking_url = fields.String(required=False)
# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Jumana Jabin MP(odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
"""Module containing Stage-based checklist Models"""
from odoo import fields, models


class CrmStage(models.Model):
    """ Inherited model for stage-based checklists. """
    _inherit = "crm.stage"

    stage_check_list_lines_ids = fields.One2many('stage.check.list',
                                                 'stage_id',
                                                 string="CheckList",
                                                 help="One2many field "
                                                      "representing "
                                                      "the checklist lines "
                                                      "associated with the"
                                                      " stage.")
    is_pre_checking = fields.Boolean(default=False,
                                     string="No Need for checklist",
                                     help="If checked, moving to the next "
                                          "stage doesn't require the checklist"
                                          "to be done.")
    is_disable_regress = fields.Boolean(default=False,
                                        string="Prohibit Regress to this stage",
                                        help="If checked, it would not be "
                                             "possible to move a lead back to"
                                             " this stage.")

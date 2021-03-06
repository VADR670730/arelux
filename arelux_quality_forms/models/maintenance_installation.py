# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta
_logger = logging.getLogger(__name__)


class MaintenanceInstallation(models.Model):
    _name = 'maintenance.installation'
    _description = 'Maintenance Installation'
    _order = 'date desc'

    date = fields.Date(
        string='Fecha'
    )
    date_done = fields.Date(
        string='Fecha Hecho'
    )
    maintenance_installation_need_check_id = fields.Many2one(
        comodel_name='maintenance.installation.need.check',
        string='Accion a revisar'
    )
    incidence = fields.Text(
        string='Incidencia'
    )
    solution = fields.Text(
        string='Solucion'
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsable'
    )
    close_measurement = fields.Date(
        string='Cierre incidencia'
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('done', 'Hecho')
        ],
        string='Estado',
        default='draft',
    )

    @api.multi
    def action_done_multi(self):
        for item in self:
            if item.state == 'draft':
                item.action_done()

    @api.multi
    def action_done(self):
        for item in self:
            if item.state == 'draft':
                item.state = 'done'
                item.date_done = fields.datetime.now()

    @api.model
    def maintenance_installation_generate(self, year, month):
        need_check_ids = self.env['maintenance.installation.need.check'].search(
            [
                ('month_' + str(month), '=', True)
            ]
        )
        if need_check_ids:
            date_next_month_item = '%s-%s-01' % (year, month)

            for need_check_id in need_check_ids:
                if need_check_id.quality_team_id.user_id:
                    installation_ids = self.env['maintenance.installation'].search(
                        [
                            ('date', '=', date_next_month_item),
                            (
                                'maintenance_installation_need_check_id',
                                '=',
                                need_check_id.id
                            )
                        ]
                    )
                    if len(installation_ids) == 0:
                        vals = {
                            'date': date_next_month_item,
                            'maintenance_installation_need_check_id': need_check_id.id,
                            'user_id': need_check_id.quality_team_id.user_id.id,
                            'state': 'draft'
                        }
                        self.env['maintenance.installation'].sudo().create(vals)

    @api.model
    def cron_autongenerate_maintenance_installation_next_month(self):
        current_date = datetime.today()
        date_next_month = current_date + relativedelta(months=+1, day=1)
        date_next_month_split = date_next_month.strftime("%Y-%m-%d").split('-')
        year_next_month = str(date_next_month_split[0])
        month_next_month = str(date_next_month_split[1])
        # maintenance_installation_generate
        self.maintenance_installation_generate(year_next_month, month_next_month)

    @api.model
    def cron_autongenerate_maintenance_installation_all_this_year(self):
        current_date = datetime.today()
        current_date_year = current_date.strftime("%Y")
        # operations
        for month_item in range(1, 13):
            # fix
            if len(str(month_item)) == 1:
                month_item = '0' + str(month_item)
            # maintenance_installation_generate
            self.maintenance_installation_generate(current_date_year, month_item)

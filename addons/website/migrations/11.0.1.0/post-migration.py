# -*- coding: utf-8 -*-
# Copyright 2017 Bloopark <http://bloopark.de>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env.cr.execute("""
      INSERT INTO website_page(url,view_id,create_uid,create_date,write_uid,write_date)
      SELECT wm.url,iuv.id,iuv.create_uid,iuv.create_date,iuv.write_uid,iuv.write_date
      FROM ir_ui_view iuv,website_menu wm where page=true and iuv.name=wm.name
      """)
    openupgrade.load_data(env.cr, 'website', 'migrations/11.0.1.0/noupdate_changes.xml', )

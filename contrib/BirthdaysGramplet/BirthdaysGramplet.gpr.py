# File: Birthdays.gpr.py
register(GRAMPLET,
         id='Birthdays', 
         name=_("Birthdays Gramplet"),
         description = _("a gramplet that displays the birthdays of the n following days"),
         status = STABLE,
         version="0.0.1",
         fname="BirthdaysGramplet.py",
         height = 200, 
         gramplet = 'BirthdaysGramplet',
         gramps_target_version="3.2",
         gramplet_title=_("Birthdays Gramplet") 
         )

from ._anvil_designer import AnmeldenTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Anmelden(AnmeldenTemplate):
  def __init__(self, item, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel_1.items = anvil.server.call("get_mitglieder")#+{"KID":item["KID"]}]
    

    # Any code you write here will run before the form opens.

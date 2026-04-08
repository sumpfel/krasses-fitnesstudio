from ._anvil_designer import KursuebersichtTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Kursuebersicht(KursuebersichtTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    print(anvil.server.call('get_uebersicht_data'))

    # Any code you write here will run before the form opens.

    self.repeating_panel_1.items = anvil.server.call('get_uebersicht_data')
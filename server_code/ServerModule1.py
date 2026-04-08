import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_uebersicht_data():
  conn = sqlite3.connect(data_files["fitnessstudio.db"])
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute('select Bezeichnung, Wochentag, Uhrzeit, "/" || TeilnehmerMax AS Teilnehmer, KID from Kurs')
  rows = cur.fetchall()
  return [dict(row) for row in rows]

@anvil.server.callable
def get_mitglieder():
  conn = sqlite3.connect(data_files["fitnessstudio.db"])
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute('select Vorname || " " || Nachname as Name, MID from Mitglied')
  rows = cur.fetchall()
  return [dict(row) for row in rows]

@anvil.server.callable
def mitglied_anmelden(KID,MID):
  conn = sqlite3.connect(data_files["fitnessstudio.db"])
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()

  cur.execute(
    "INSERT INTO Anmeldungen (KID, MID, anmeldedatum) VALUES (?, ?, ?)", (KID, MID)
  )
  rows = cur.fetchall()
  return
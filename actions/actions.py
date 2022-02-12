from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset

#action_call_XXX -> Settano le slot slots plumber, electrician, painter 
class ActionCallPlumber(Action):
  def name(self) -> Text:
      return "action_call_plumber" 
  def run(self, 
          dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      selected_intent = Tracker.get_intent_of_latest_message(tracker)[-3:]
      if selected_intent == "ENG":
        SlotSet("slot_plumber", "plumber")
      elif selected_intent == "ITA":
        SlotSet("slot_plumber", "idraulico") 
      return []   

class ActionCallElectrician(Action):
  def name(self) -> Text:
      return "action_call_electrician"  
  def run(self, 
          dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      selected_intent = Tracker.get_intent_of_latest_message(tracker)[-3:]
      if selected_intent == "ENG":
        SlotSet("slot_plumber", "electrician")
      elif selected_intent == "ITA":
        SlotSet("slot_plumber", "elettricista") 
      return []   
    

class ActionCallPainter(Action):
  def name(self) -> Text:
      return "action_call_painter"  
  def run(self, 
          dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      selected_intent = Tracker.get_intent_of_latest_message(tracker)[-3:]
      if selected_intent == "ENG":
        SlotSet("slot_plumber", "painter")
      elif selected_intent == "ITA":
        SlotSet("slot_plumber", "imbianchino") 
      return []   

#Resetta tutte le slots
class ResetSlots(Action):
  def name(self) -> Text:
      return "action_reset_slots"  
  def run(self, 
          dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      return[AllSlotsReset()]
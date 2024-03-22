from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  
  def button_1_click(self, **event_args):
    nums = self.text_area_1.text.split()
    arr = [int(num)for num in nums]
    n = len(arr)
    if self.radio_button_1.selected:
        anvil.server.call(insertion_sort(arr))
    elif choice == "selection":
        selection_sort(arr)
    elif choice == "bubble":
        bubble_sort(arr)
    elif choice == "merge":
        merge_sort(arr)
    
    
    


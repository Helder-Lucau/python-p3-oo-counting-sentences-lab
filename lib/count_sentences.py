#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self._value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    pass

  def is_question(self):
    if self._value.endswith("?"):
      return True
    else:
      return False

  def is_exclamation(self):
    pass

  def count_sentences(self):
    pass

  value = property(get_value, set_value)
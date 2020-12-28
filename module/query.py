import requests
import json
import os
import csv
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


class QueryBuilder:

  def __init__(self):
    """constructor of query builder to create dinamically a query
    query variable it's the final string of the query
    """
    self.query = ""
    self.filters = []
    self.words = []
    self.logic_operators = []

  def addFieldRestriction(self, field):
    """ add field restriction to the query
        check documentation for more information https://dev.elsevier.com/sc_search_tips.html
    Args:
        filter ([string]): [field restriction like "KEY","TITLE","ABS"]
    """
    self.query += f"{field}%28"
    self.filters.append(field)

  def addWord(self, word):
    """
      Insert values , words that it'll be searched on Scopus API
    Args:
        word ([string]): [values to be search as key of the query]
    """
    self.query += f"{word}"
    self.words.append(word)

  def addBooleanOperator(self, operator):
    """
      Boolean Operator to use between query or between words.
      For more information visit documentation https://dev.elsevier.com/sc_search_tips.html
    Args:
        operator ([string]): [boolean operator in string format]
    """
    self.query += f"+{operator}+"
    self.logic_operators.append(operator)

  def to_str(self):
    """
      Combine fields,boolean operator and words to create the query
    Returns:
        [string]: [query composed]
    """
    if(self.query[len(self.query)-3:] != "%29"):
      self.query += "%29"
    return self.query

  def concatenate_query(self, _query, boolean_operator=""):
    """
      Concatenate two instance of query builder. 
      The boolean operator it's used between the queries.
    Args:
        _query ([QueryBuilder]): [instance of QueryBuilder class]
        boolean_operator (str, optional): [Boolean operator used for concatenate, default to "".]. Defaults to "".

    Returns:
        [type]: [description]
    """
    self.to_str()
    if(boolean_operator != ""):
      self.query += "+"+boolean_operator
    self.query += "+"+_query.to_str()

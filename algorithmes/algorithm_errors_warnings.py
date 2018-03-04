import json
import importlib

algorithmes_test = __import__('algorithmes_test')

warnings_file = open('../errors/warnings.json', 'w')
errors_file = open('../errors/errors.json', 'w')

def detect_warnings:

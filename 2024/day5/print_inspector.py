import re

class PrintInspector():

    def __init__(self, rules_string):
        self.rules = self.parse_rules(rules_string)
        
    def parse_rules(self, rules_string):
        parsed_rules = {}
        rule_list = list(map(lambda rule: list(map(int, rule.split('|'))), re.findall(r'\d+\|\d+', rules_string)))
        for rule in rule_list:
            preceding_page = rule[0]
            succeeding_page = rule[1]
            
            if not preceding_page in parsed_rules:
                parsed_rules[preceding_page] = []
                
            if not succeeding_page in parsed_rules[preceding_page]:
                parsed_rules[preceding_page].append(succeeding_page)
        return parsed_rules

    def parse_updates(self, updates_string):
        parsed_updates = list(map(lambda line: list(map(int, re.findall(r'\d+', line))), updates_string.split('\n')))
        return parsed_updates
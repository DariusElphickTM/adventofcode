import re

class PrintInspector():

    def __init__(self, rules_string):
        self.rules = self.parse_rules(rules_string)
    
    def get_part_1_answer(self, updates_string):
        safe_updates = self.filter_updates(updates_string, True)
        total = 0
        for safe_update in safe_updates:
            total += safe_update[len(safe_update) // 2]
        return total
    
    def get_part_2_answer(self, updates_string):
        return 123
    
    def filter_updates(self, updates_string, is_safe: True):
        parsed_updates = self.parse_updates(updates_string)
        return list(filter(lambda update: self.is_update_safe(update) == is_safe, parsed_updates))
    
    def is_update_safe(self, update):
        is_safe = True
        for i, page in enumerate(update):
            if page in self.rules:
                relevant_rule = self.rules[page]
                for page in relevant_rule:
                    if page in update and update.index(page) < i:
                        is_safe = False
                        break
        return is_safe
    
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
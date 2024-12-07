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
        unsafe_updates = self.filter_updates(updates_string, False)
        corrected_updates = list(map(self.correct_unsafe_update, unsafe_updates))
        total = 0
        for corrected_update in corrected_updates:
            total += corrected_update[len(corrected_update) // 2]
        return total
    
    def correct_unsafe_update(self, update):
        corrected_update = []
        for i, page in enumerate(update):
            insertion_index = i
            if page in self.rules:
                relevant_rule = self.rules[page]
                for rule in relevant_rule:
                    if rule in corrected_update and corrected_update.index(rule) < i:
                        new_insertion_index = corrected_update.index(rule)
                        insertion_index = new_insertion_index if new_insertion_index < insertion_index else insertion_index
            corrected_update.insert(insertion_index, page)
        return corrected_update
    
    def filter_updates(self, updates_string, is_safe: True):
        parsed_updates = self.parse_updates(updates_string)
        return list(filter(lambda update: self.is_update_safe(update) == is_safe, parsed_updates))
    
    def is_update_safe(self, update):
        is_safe = True
        for i, page in enumerate(update):
            if page in self.rules:
                relevant_rule = self.rules[page]
                for rule in relevant_rule:
                    if rule in update and update.index(rule) < i:
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
import re

def main():
    print("Hello World")
    
def parse_rules(input):
    parsed_rules = {}
    rule_list = list(map(lambda rule: list(map(int, rule.split('|'))), re.findall(r'\d+\|\d+', input)))
    for rule in rule_list:
        preceding_page = rule[0]
        succeeding_page = rule[1]
        
        if not preceding_page in parsed_rules:
            parsed_rules[preceding_page] = []
            
        if not succeeding_page in parsed_rules[preceding_page]:
            parsed_rules[preceding_page].append(succeeding_page)
    return parsed_rules

def parse_updates(input):
    parsed_updates = list(map(lambda line: list(map(int, re.findall(r'\d+', line))), input.split('\n')))
    return parsed_updates

if __name__ == "__main__":
    main()
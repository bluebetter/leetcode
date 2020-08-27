# coding=utf-8
TCS = {
    'func': 'findItinerary',
    #'func': 'findItinerary2',
    'tcs': [
        {
            'input': [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]],
            'hope': ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"],
        },
        {
            'input': [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            'hope': ["JFK", "MUC", "LHR", "SFO", "SJC"]
        },
        {
            'input': [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
            'hope': ["JFK","ATL","JFK","SFO","ATL","SFO"]
        }
        
    ]
}

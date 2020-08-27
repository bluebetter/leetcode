class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        map_next = {}
        for tc in tickets:
            f, t = tc[0], tc[1]
            if f in map_next:
                if t < map_next[f]:
                    map_next[f].insert(0, t)
                else:
                    map_next[f].append(t)
            else:
                map_next[f] = [t]
        res = []
        f = 'JFK'
        print(map_next)
        while f:
            res.append(f)
            next_list = []
            new_f = ''
            for n in map_next.get(f):
                if n not in res:
                    if not f:
                        new_f = n
                    else:
                        next_list.append(n)
            map_next[f] = next_list
            if not new_f:
                f = res[-1]
            else:
                f = new_f
        return res

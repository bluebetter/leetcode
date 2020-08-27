class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(curr):
            while curr in map_next and map_next[curr]:
                tmp = map_next[curr].pop(0)
                dfs(tmp)
            stack.append(curr)
        
        map_next = {}
        for f, t in tickets:
            if f in map_next:
                for i in range(len(map_next[f])):
                    if t < map_next[f][i]:
                        map_next[f].insert(i, t)
                        t = ''
                        break
                if t:
                    map_next[f].append(t)
            else:
                map_next[f] = [t]
        stack = []
        dfs('JFK')
        return stack[::-1]

    def findItinerary2(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import collections, heapq
        def dfs(curr):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])
        
        stack = list()
        dfs("JFK")
        return stack[::-1]

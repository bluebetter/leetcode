class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        transfer = {
            'init': {
                'space': 'init',
                'number': 'int',
                'point': 'point_no',
                'sign': 'int_sign'
            },
            'int_sign': {
                'number': 'int',
                'point': 'point_no',
            },
            'int': {
                'number': 'int',
                'exp': 'exp',
                'point': 'point_yes',
                'space': 'end'
            },
            'point_yes': {
                'number': 'fraction',
                'exp': 'exp',
                'space': 'end',
            },
            'point_no': {
                'number': 'fraction',
            },
            'fraction': {
                'number': 'fraction',
                'exp': 'exp',
                'space': 'end',
            },
            'exp': {
                'number': 'exp_int',
                'sign': 'exp_sign',
            },
            'exp_sign': {
                'number': 'exp_int',
            },
            'exp_int': {
                'number': 'exp_int',
                'space': 'end',
            },
            'end': {
                'space': 'end'
            }
        }

        def getCharType(c):
            if ' ' == c:
                return 'space'
            elif '.' == c:
                return 'point'
            elif c in ['-', '+']:
                return 'sign'
            elif c.isdigit():
                return 'number'
            elif 'e' == c.lower():
                return 'exp'
            else:
                return 'illegal'
        
        st = 'init'
        for c in s:
            c_type = getCharType(c)
            if c_type not in transfer[st]:
                return False
            st = transfer[st][c_type]
        return st in ['int', 'point', 'fraction', 'exp_int', 'end']

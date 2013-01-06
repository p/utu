import re

def forward(cls, old_method, new_method):
    def fn(self):
        # call e.g. setUp on all parents of the adjusted base
        getattr(super(cls, self), old_method)()
        
        # call setup on all children of the adjusted base
        new_fn = getattr(self, new_method, None)
        
        if new_fn:
            new_fn()
    
    setattr(cls, old_method, fn)

class adjusted_base(object):
    def setup(self):
        pass
    
    def teardown(self):
        pass

all_cap_re = re.compile('([a-z0-9])([A-Z])')

def adjust_test_base(cls):
    class adjusted_cls(adjusted_base, cls):
        pass
    
    methods = {'setup': 'setUp', 'teardown': 'tearDown'}
    for new_method in methods:
        old_method = methods[new_method]
        forward(adjusted_cls, old_method, new_method)
    
    for method in dir(adjusted_cls):
        if method.startswith('assert'):
            converted_name = all_cap_re.sub(r'\1_\2', method).lower()
            if converted_name != method:
                setattr(adjusted_cls, converted_name, getattr(adjusted_cls, method))
    
    return adjusted_cls

_adjusted_test_bases = {}

def adjusted_test_base(cls):
    adjusted = _adjusted_test_bases.get(cls)
    if adjusted is None:
        adjusted = adjust_test_base(cls)
        _adjusted_test_bases[cls] = adjusted
    return adjusted

def adjusted_unittest_base():
    import unittest
    return adjusted_test_base(unittest.TestCase)

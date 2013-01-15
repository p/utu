import utu
import unittest

def invoke(test):
    runner = unittest.runner.TextTestRunner()
    loader = unittest.loader.defaultTestLoader
    test = loader.loadTestsFromTestCase(test)
    runner.run(test)

class UtuTest(unittest.TestCase):
    def test_sanity(self):
        # XXX should work out why I cannot use an ordinary variable here
        state = {}
        
        class Testee(unittest.TestCase):
            def test_method(self):
                state['test_ran'] = True
        
        invoke(Testee)
        
        self.assertTrue('test_ran' in state)
    
    def test_assertion(self):
        state = {}
        
        class Testee(utu.adjusted_unittest_base()):
            def test_foo(self):
                self.assert_true(True)
                state['asserted'] = True
        
        invoke(Testee)
        
        self.assertTrue('asserted' in state)
    
    def test_setup(self):
        state = {}
        
        class Testee(utu.adjusted_unittest_base()):
            @classmethod
            def setup_class(cls):
                state['setup_class_ran'] = True
            
            @classmethod
            def teardown_class(cls):
                state['teardown_class_ran'] = True
            
            def setup(self):
                state['setup_ran'] = True
            
            def teardown(self):
                state['teardown_ran'] = True
            
            def test_foo(self):
                self.assert_true(True)
                state['asserted'] = True
        
        invoke(Testee)
        
        self.assertTrue('setup_class_ran' in state)
        self.assertTrue('teardown_class_ran' in state)
        self.assertTrue('setup_ran' in state)
        self.assertTrue('teardown_ran' in state)
        self.assertTrue('asserted' in state)
    
    def test_setup_with_super(self):
        state = {}
        
        class Testee(utu.adjusted_unittest_base()):
            @classmethod
            def setup_class(cls):
                super(Testee, cls).setup_class()
                
                state['setup_class_ran'] = True
            
            @classmethod
            def teardown_class(cls):
                super(Testee, cls).teardown_class()
                
                state['teardown_class_ran'] = True
            
            def setup(self):
                super(Testee, self).setup()
                
                state['setup_ran'] = True
            
            def teardown(self):
                super(Testee, self).teardown()
                
                state['teardown_ran'] = True
            
            def test_foo(self):
                self.assert_true(True)
                state['asserted'] = True
        
        invoke(Testee)
        
        self.assertTrue('setup_class_ran' in state)
        self.assertTrue('teardown_class_ran' in state)
        self.assertTrue('setup_ran' in state)
        self.assertTrue('teardown_ran' in state)
        self.assertTrue('asserted' in state)

if __name__ == '__main__':
    unittest.main()

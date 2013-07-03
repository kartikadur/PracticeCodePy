'''
Created on Apr 5, 2013

@author: zeroshiiro
'''
from median import MedianFinder
import unittest

class TestMedianFinder(unittest.TestCase):
    
    def testTest(self):
        self.assertTrue(True, "To check if the tests are running")
        
    def testAddedItemsAreSorted1(self):
        a = [3, 2, 4, 1, 5]
        s = MedianFinder()
        for i in range(1, len(a) + 1):
            s.addItem(a[i - 1])
            m = a[0:i]
            self.assertEquals(sorted(m), s.items)
        
    def testItemsSortedAfterRemoval1(self):
        a = [3, 2, 4, 1, 5]
        s = MedianFinder()
        for i in a:
            s.addItem(i)
        
        for i in range(1, len(a) + 1):
            s.remItem(a[i - 1])
            m = a[i: len(a)]
            self.assertEquals(sorted(m),s.items)
            
    def testRemoveFromEmptyMedianFinder(self):
        s = MedianFinder()
        self.assertEquals(s.remItem(4), "Wrong!")
        
    def testRemoveItemNotInMedianFinder(self):
        a = [3, 2, 4, 1, 5]
        s = MedianFinder()
        for i in a:
            s.addItem(i)
        self.assertEquals(s.remItem(10), "Wrong!")
    
    def testMedianOnAdd(self):
        a = [3, 2, 4, 1, 5]
        aMedian = [3, 2.5, 3, 2.5, 3]
        s = MedianFinder()
        for i in range(1, len(a) + 1):
            self.assertEquals(aMedian[i - 1], s.addItem(a[i - 1]))                              
    
    def testMedianOnRemoval(self):
        a = [-3, -2, -4, -1, -5]
        aMedian = [-3, -4, -3, -5, "Wrong!"]
        s = MedianFinder()
        
        self.assertEquals("Wrong!", s.remItem(a[0]))

        for i in a:
            s.addItem(i)
        
        for i in range(1, len(a) + 1):
            self.assertEquals(aMedian[i - 1], s.remItem(a[i - 1]))
    
    def testInput01(self):
        x = "C:/xampp/htdocs/PracticeCodePy/testInputs/medianInputs/Input01.txt"
        data = open(x)
        N = data.readline();
        s = MedianFinder()
        for i in range(int(N)):
            Q = data.readline().split(" ")
            num = int(Q[1])
            if(Q[0] == "a"):
                print(s.addItem(num))
            elif(Q[0] == "r"):
                print(s.remItem(num))
            




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
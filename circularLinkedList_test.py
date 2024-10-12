import unittest
import cirularLinkedList as cll

class TestCircularLinkedList(unittest.TestCase): 
    
    def test_circularLinkedListComparison_pos(self):
        cll1 = cll.CircularLinkedList()
        cll1.append("1")
        cll1.append("2")
        cll1.append("3")
        cll1.append("4")
        cll2 = cll.CircularLinkedList()
        cll2.append("3")
        cll2.append("4")
        cll2.append("1")
        cll2.append("2")
        self.assertTrue(cll1 == cll2)

    def test_circularLinkedListComparison_neg(self):
        cll3 = cll.CircularLinkedList()
        cll3.append("1")
        cll3.append("2")
        cll3.append("3")
        cll3.append("4")
        cll4 = cll.CircularLinkedList()
        cll4.append("3")
        cll4.append("4")
        cll4.append("2")
        cll4.append("1")
        self.assertFalse(cll3 == cll4)

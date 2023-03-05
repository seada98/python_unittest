import unittest
import test_cases
class TestSpeed (unittest.TestCase):
    def test_car_speed_low(self):
        self.assertEqual('Low', test_cases.car_speed(30))
    def test_car_speed_normal(self):
        self.assertEqual('Normal', test_cases.car_speed(100))
    def test_car_speed_high(self):
        self.assertEqual('High', test_cases.car_speed(150))
    def test_car_speed_vhigh(self):
        self.assertEqual('V.High', test_cases.car_speed(210))
    def test_car_speed_invalid(self):
        self.assertEqual('Invalid', test_cases.car_speed(230))
    def test_car_speed_invalid1(self):
        self.assertEqual('Invalid', test_cases.car_speed(-1))
mysuit = unittest.TestSuite()
mysuit.addTest(TestSpeed())
#student score
class TestScore (unittest.TestCase):
    def test_invalid(self):
        self.assertEqual('Invalid', test_cases.student_score(-1))
    def test_failed(self):
        self.assertEqual('Failed', test_cases.student_score(30))
    def test_Passed(self):
        self.assertEqual('Passed', test_cases.student_score(60))
    def test_good(self):
        self.assertEqual('Good', test_cases.student_score(73))
    def test_vgood(self):
        self.assertEqual('V.Good', test_cases.student_score(76))
    def test_excellent(self):
        self.assertEqual('Excellent', test_cases.student_score(90))

mysuitscore = unittest.TestSuite()
mysuitscore.addTest(TestScore())

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(mysuit)
    runner.run(mysuitscore)


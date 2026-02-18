from Point import Point
import unittest

class TestPoint(unittest.TestCase):
    def test_Point_Default(self) -> None:
        p = Point()
        self.assertEqual(str(p), "(0, 0)")
        self.assertAlmostEqual(p.x, 0)
        self.assertEqual(p.y, 0)
    def test_Point_Provided(self) -> None:
        p = Point(3.0, 4.0)
        self.assertEqual(str(p), "(3.0, 4.0)")
    def test_Point_Update(self) -> None:
        # test_Point_Move
        p = Point()
        p.move(3.0, 4.0)
        self.assertEqual(str(p), "(3.0, 4.0)")
    def test_Point_Reset(self) -> None:
        p = Point(3.0, 4.0)
        p.reset()
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)
    def test_Point_CalDistance(self) -> None:
        p1 = Point()
        p2 = Point(3.0, 4.0)
        d = p1.calculate_distance(p2)
        self.assertEqual(d, 5)
        p1.move(3.2, 5.9)
        p2.move(2.4, 8.7)
        d = p2.calculate_distance(p1)
        self.assertAlmostEqual(d, 2.91, 2)


if __name__ == "__main__":
    unittest.main()
import unittest

from codingexercises.jumpingKangaroos import (
    kangaroo
)

class KangarooTest(unittest.TestCase):
    def test_kangaroo_in_the_back_but_faster(self) -> None:
        self.assertEqual(
            kangaroo(kanga1=0, speed1=3, kanga2=4, speed2=2), True)

    def test_kangaroo_in_the_back_and_slower(self) -> None:
        self.assertEqual(
            kangaroo(kanga1=0, speed1=2, kanga2=5, speed2=3), False)

    def test_kangaroo_in_the_front_and_faster(self) -> None:
        self.assertEqual(
            kangaroo(kanga1=5, speed1=3, kanga2=0, speed2=2), False)

    def test_kangaroo_in_the_front_and_slower(self) -> None:
        self.assertEqual(
            kangaroo(kanga1=5, speed1=2, kanga2=0, speed2=3), True)

    def test_kangaroo_starts_in_negative_position(self) -> None:
        self.assertEqual(
            kangaroo(kanga1=-1, speed1=3, kanga2=0, speed2=2), True)

    def test_kangaroos_meet_with_float_speed(self) -> None:
        self.assertEqual(
            kangaroo(kanga1=0, speed1=1.5, kanga2=3, speed2=1), True)

    def test_kangaroos_does_not_meet_with_float_speed(self) -> None:
        self.assertEqual(
            kangaroo(kanga1=0, speed1=1.5, kanga2=3, speed2=1.2), False)

import unittest
from komby.komby import Komby


class KombyTest(unittest.TestCase):

    def test_total_partitions_0(self):
        data = []
        self.assertEqual(Komby.total_partitions(data), 0)

    def test_total_partitions_1(self):
        data = [1]
        self.assertEqual(Komby.total_partitions(data), 1)

    def test_total_partitions_n(self):
        data = [1, 2, 5]
        self.assertEqual(Komby.total_partitions(data), 4)

    def test_partitions_0(self):
        data = []
        self.assertEqual(Komby.partitions(data), [])

    def test_partitions_1(self):
        data = [1]
        self.assertEqual(Komby.partitions(data), [[[1]]])

    def test_partitions_2(self):
        data = [1, 2]
        self.assertEqual(Komby.partitions(data), [[[1, 2]], [[1], [2]]])

    def test_partitions_3(self):
        data = [1, 2, 3]
        self.assertEqual(Komby.partitions(data), [[[1, 2, 3]], [[1, 2], [3]], [[1], [2, 3]], [[1], [2], [3]]])

    def test_partitions_sorted(self):
        """
        Verify if the sort operation worked
        :return:
        """
        data = [1, 2, 3, 4, 5]
        partitions = Komby.partitions(data, True)

        error = False
        ant = 1
        for p in partitions:
            if len(p) < ant:
                error = True
            ant = len(p)

        self.assertFalse(error)

    def test_partitions_show(self):
        data = [1, 2, 3]

        print("Number of possible partitions: {}.\n".format(Komby.total_partitions(data)))

        partitions = Komby.partitions(data, True)

        print("Partitions:")
        for p in partitions:
            print("\t - {}".format(p))


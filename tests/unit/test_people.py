from unittest import TestCase
import people


class PeopleTest(TestCase):
    def test_read_all(self):

        timestamp = people.get_timestamp()

        expected = [
            {
                "fname": "Tooth",
                "lname": "Fairy",
                "timestamp": timestamp
            },
            {
                "fname": "Knecht",
                "lname": "Ruprecht",
                "timestamp": timestamp
            },
            {
                "fname": "Easter",
                "lname": "Bunny",
                "timestamp": timestamp
            }
        ]

        self.assertEqual(people.read_all(), expected)

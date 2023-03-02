from unittest import TestCase
import people


class PeopleCrudTest(TestCase):
    def test_create_people(self):
        # Swearengen
        person = {
            'lname': 'Swearengen',
            'fname': 'Al'
        }
        p = people.create(person)

        expected = {
            "lname": p[0].get('lname'),
            "fname": p[0].get('fname'),
            "timestamp": people.get_timestamp(),
        }

        self.assertEqual(p[0], expected)
        self.assertEqual(p[1], 201)

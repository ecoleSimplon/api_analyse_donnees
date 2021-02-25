import unittest
import fonctions as f
import values as v


class TestCreateJson(unittest.TestCase):

    def test_filename(self):
        self.assertEqual(f.create_json(""), 1)
        self.assertEqual(f.create_json("",""), 1)
        self.assertEqual(f.create_json("foo"), 1)
        self.assertEqual(f.create_json("/"), 1)
        self.assertEqual(f.create_json(123), 1)
        self.assertEqual(f.create_json(123.1), 1)
        self.assertEqual(f.create_json('estimates.json'),1)
        self.assertEqual(f.create_json('estimates.csv', '/'), 1)
        self.assertEqual(f.create_json('estimates.csv','estimates'), 1)
        self.assertEqual(f.create_json('estimates.csv','estimates.csv'), 1)
        self.assertEqual(f.create_json('estimates.csv','estimates.txt'), 1)
        self.assertEqual(f.create_json('estimates.csv','estimates.json'), 0)
        self.assertEqual(f.create_json('estimates.csv'), 0)
        self.assertEqual(f.create_json(), 0)
        

class TestGetLatestByCountry(unittest.TestCase):

    def test_filename(self):
        self.assertIsNone(f.get_latest_by_country('foo'))
        self.assertIsNone(f.get_latest_by_country('123'))
        self.assertIsNone(f.get_latest_by_country(456))
        self.assertIsNone(f.get_latest_by_country(456.1))
        self.assertIsNone(f.get_latest_by_country(''))
        self.assertIsNone(f.get_latest_by_country('.'))
        self.assertIsNone(f.get_latest_by_country('/'))
        self.assertIsNone(f.get_latest_by_country('Albania', 'estimates.csv'))
        self.assertIsNone(f.get_latest_by_country('estimates.csv', 'Albania'))
        self.assertIsNotNone(f.get_latest_by_country('Albania', 'estimates.json'))
    
    def test_return(self):
        countries = v.countries
        values = v.values_latest
        for i in range(len(countries)):
            self.assertEqual(f.get_latest_by_country(countries[i]), values[i])


class TestAverageForYear(unittest.TestCase):
    
    def test_filename(self):
        self.assertIsInstance(f.average_for_year(''),1)
        self.assertIsInstance(f.average_for_year('_'),1)
        self.assertIsInstance(f.average_for_year(2017), 1)
        self.assertIsInstance(f.average_for_year('2017'), float)
        self.assertIsInstance(f.average_for_year('2024'), 1)

    def test_return(self):
        years = v.years
        values = v.values_years
        for i in range(len(years)):
            self.assertEqual(f.average_for_year(years[i]), values[i])

class TestPerCapita(unittest.TestCase):

    def test_filename(self):
        self.assertEqual(f.get_per_capita('', 'France'), 1)
        self.assertEqual(f.get_per_capita('/', 'France'), 1)
        self.assertEqual(f.get_per_capita('.', 'France'), 1)
        self.assertEqual(f.get_per_capita('_', 'France'), 1)
        self.assertEqual(f.get_per_capita('2015', 'France'), 1)
        self.assertEqual(f.get_per_capita(2015, 'France'), 1)
        self.assertEqual(f.get_per_capita('2017', 'foo'), 1)
        self.assertEqual(f.get_per_capita('2017', 2015), 1)
        self.assertEqual(f.get_per_capita('2017', '2015'), 1)
        self.assertIsInstance(f.get_per_capita('estimates.json', 'France'), dict)

    def test_return(self):
        countries = v.countries
        values = v.values_capita
        for i in range(len(countries)):
            self.assertEqual(f.get_per_capita("estimates.json", countries[i]), values[i])
        

if __name__ == '__main__':
    unittest.main()
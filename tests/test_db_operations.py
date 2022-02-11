import unittest
from moto import mock_dynamodb
from src import db_operations


class DynamoDBTestCase(unittest.TestCase):
    
    @mock_dynamodb
    def test_create_table(self):
        result = db_operations.create_visitor_table()
        self.assertEqual(result.table_name, 'Visitors')

        
    @mock_dynamodb
    def test_delete_table(self):
        result = db_operations.delete_table()
        self.assertEqual(result["message"], "deleted table")

if __name__== '__main__':
    unittest.main()
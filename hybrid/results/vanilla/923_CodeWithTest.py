import pandas as pd
import random

def task_func(person_names, email_domains, num_records=5):
    # Check if the number of names provided is less than the number of records requested
    if len(person_names) < num_records:
        raise ValueError("The number of names provided is less than the number of records requested.")
    
    # Check if no email domains are provided
    if not email_domains:
        raise ValueError("No email domains are provided.")
    
    # Randomly select names and email domains to create the specified number of records
    selected_names = random.sample(person_names, num_records)
    selected_domains = random.choices(email_domains, k=num_records)
    
    # Create emails by combining selected names and domains
    emails = [f"{name.lower().replace(' ', '.')}@{domain}" for name, domain in zip(selected_names, selected_domains)]
    
    # Clean emails by replacing "@" with "[at]"
    cleaned_emails = [re.sub(r'@', '[at]', email) for email in emails]
    
    # Create a DataFrame with the selected names and cleaned emails
    df = pd.DataFrame({
        'Name': selected_names,
        'Email': cleaned_emails
    })
    
    return df

# Example usage:
# person_names = ["Alice Johnson", "Bob Smith", "Charlie Brown", "David Wilson", "Eve Davis"]
# email_domains = ["example.com", "test.org", "sample.net"]
# df = task_func(person_names, email_domains, num_records=5)
# print(df)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        random.seed(0)  # Initialize random seed
        result_df = task_func(['John Doe', 'Jane Smith'], ['gmail.com', 'yahoo.com'], 2)
        self.assertTrue(isinstance(result_df, pd.DataFrame))
        self.assertEqual(len(result_df), 2)
        self.assertTrue(set(result_df.columns) == {'Name', 'Email'})
        self.assertTrue(all(result_df['Email'].str.contains('[at]')))
        
    def test_case_2(self):
        random.seed(0)  # Initialize random seed
        result_df = task_func(['Alice'], ['outlook.com'], 1)
        self.assertTrue(isinstance(result_df, pd.DataFrame))
        self.assertEqual(len(result_df), 1)
        self.assertTrue(set(result_df.columns) == {'Name', 'Email'})
        self.assertTrue(all(result_df['Email'].str.contains('[at]')))
        
    def test_case_3(self):
        random.seed(0)  # Initialize random seed
        with self.assertRaises(ValueError):
            task_func(['John Doe'], ['gmail.com'], 2)
            
    def test_case_4(self):
        random.seed(0)  # Initialize random seed
        with self.assertRaises(ValueError):
            task_func(['John Doe', 'Jane Smith'], [], 2)
            
    def test_case_5(self):
        random.seed(0)  # Initialize random seed
        result_df = task_func(['John Doe', 'Jane Smith', 'Bob'], ['gmail.com', 'yahoo.com'], 3)
        self.assertTrue(isinstance(result_df, pd.DataFrame))
        self.assertEqual(len(result_df), 3)
        self.assertTrue(set(result_df.columns) == {'Name', 'Email'})
        self.assertTrue(all(result_df['Email'].str.contains('[at]')))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
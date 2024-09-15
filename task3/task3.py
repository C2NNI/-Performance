import json

with open("C:/Users/Артём/Desktop/НТ Performance/values.json" , "r") as file:
    value_file = json.load(file)['values']
print(value_file)
with open("C:/Users/Артём/Desktop/НТ Performance/tests.json", "r") as file:
    test_file = json.load(file)['tests']
print(test_file)

values_dict = {value['id']: value['value'] for value in value_file}

for test in test_file:
    if isinstance(test, dict):
        test_id = test.get('id')
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        for subtest in test.get('values', []):
            if isinstance(subtest, dict):
                subtest_id = subtest.get('id')
                if subtest_id in values_dict:
                    subtest['value'] = values_dict[subtest_id]

with open("C:/Users/Артём/Desktop/НТ Performance/report.json", 'w') as report_file:
    json.dump({'tests': test_file}, report_file, ensure_ascii=False, indent=4)
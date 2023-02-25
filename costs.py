import os
import tiktoken

def list_subdirectories(directory_path):
    subdirectories = {}
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            subdirectories[str(item)] = item_path
    return subdirectories

def scrape_text(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    text = f.read()
                    return str(text)

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    cost = round(num_tokens * 0.0004 / 1000, 4)
    print('The number of tokens in the above corpus is: ' + str(num_tokens) + ' tokens')
    print('The cost to run the model on the above corpus is: $' + str(cost) + ' dollars')
    return num_tokens, cost

if __name__ == '__main__':
    directory_path = input("Enter the directory path: ")
    paths = list_subdirectories(directory_path)
    total_tokens = 0
    total_cost = 0
    for path in paths:
        print('')
        print('Company: ' + str(path))
        print('')
        company_text = scrape_text(paths[path])
        if company_text:
            company_tokens, company_cost = num_tokens_from_string(company_text, "text-embedding-ada-002")
            total_tokens += company_tokens
            total_cost += company_cost
    print('')
    print('Total number of tokens in directory: ' + str(total_tokens) + ' tokens')
    print('Total cost to run the model on the directory: $' + str(total_cost) + ' dollars')

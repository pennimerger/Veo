import json, time, random, pandas as pd

def write_csv(jsonfile):
    num = random.randint(100,8000)
    csvfile = f"results/write_csv{num}.csv"
    suffix = (".json")
    if jsonfile.endswith(suffix):
        with open(jsonfile, 'r+') as file:
            file_data = json.load(file) 
        df = pd.json_normalize(file_data)
        df.to_csv(csvfile, index=False)

    else:
        print("Only Json and csv file formats!")

def scroll(browser):
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def write_json(new_data, filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file) # loads data into a dict
        file_data.append(new_data)
        file.seek(0) # sets file current position at offset
        json.dump(file_data, file, indent = 4) # converts back to json.

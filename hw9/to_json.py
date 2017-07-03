import json
import requests
from work_with_file import write_to_file, read_file_data



def get_info(url):
	print("Get to {}".format(url))
	result = requests.get(url)
	print("result code {}".format(result.status_code))
	if result.status_code == 200:
		return result.json()
	else:
		raise RuntimeError("Get from url = '{}' return code {}".format(url, result.status_code))

if __name__ == '__main__':
    out_json_file = "save_info.json"
    url = "https://jsonplaceholder.typicode.com/posts/1/comments"
    data_json = get_info(url)
    print(json.dumps(data_json, sort_keys=True, indent=4))
    write_to_file(json.dumps(data_json), filename =out_json_file)
    print(read_file_data(out_json_file))
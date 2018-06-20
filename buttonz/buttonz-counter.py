import urllib.request
import re
from bs4 import BeautifulSoup
import pandas
from operator import itemgetter
import sys

def buttonz_counter(file, output):
    http_prefix = 'http://'
    btn_regexp = re.compile('(class="((?i)[A-Z 0-9]{0,}(?i)(btn|button).*?)")|(<input type="(submit|reset|button)")|(<button>)')
    dataframe = pandas.read_csv(file, header=None)
    dataset = dataframe.values
    pages = dataset[:, :].astype(str)
    content_array = []
    num_pages = len(pages)
    for site in range(0,num_pages):
        page = str(pages[site][0])
        if not page.startswith(http_prefix):
            page = http_prefix+page
        html = urllib.request.urlopen(page)
        soup = str(BeautifulSoup(html, "html.parser"))
        button_number = re.findall(btn_regexp, soup)
        content_array.append([page,len(button_number)])
    content_sorted = sorted(content_array, key=itemgetter(1), reverse=True)
    write_to_file(output,content_sorted)

def write_to_file(file_name, dataset):
    csv_headers = 'address,number_of_buttons\n'
    separator = ','
    f = open(output, 'w')
    f.write(csv_headers)
    for i in dataset:
        f.write(i[0] + separator + str(i[1]) + '\n')
    f.close()

if __name__ == '__main__':
    file = str(sys.argv[1])+'.csv'
    output = str(sys.argv[2])
    buttonz_counter(file, output)
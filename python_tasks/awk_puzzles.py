"""
* What is the most frequent browser (user agent)?
* Show number of requests per month for ip 95.108.129.196 (for example:
Sep 2016 - 100500 reqs, Oct 2016 - 0 reqs, Nov 2016 - 2 reqs...)
* Show total amount of data which server has provided for each unique ip
(i.e. 100500 bytes for 1.2.3.4; 9001 bytes for 5.4.3.2 and so on)
"""


import argparse
import os
import re
from datetime import datetime


parse_line_pattern = re.compile(r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) .+ (?P<date>\[.+\]) \"[^\"]+\" \d+ ("
                                r"?P<bytes>[\d|-]+)( \"[^\"]\")* (?P<agent>\".+\") \".+\"")


def parse_line(record):
    try:
        match_line = parse_line_pattern.match(record)

        ip = match_line.groupdict()['ip']

        req_date = match_line.groupdict()['date']

        bytes_amount = match_line.groupdict()['bytes']
        try:
            bytes_amount = int(bytes_amount)
        except:
            bytes_amount = 0

        user_agent = match_line.groupdict()['agent']

        req_date = req_date.strip("[]").split()[0].split(':')[0]
        req_date = datetime.strptime(req_date, "%d/%b/%Y").strftime("%b/%Y")
        return ip, req_date, bytes_amount, user_agent
    except:
        print(record, "doesn't match")


def read_log_file(file_path):
    with open(file_path, 'r') as lf:
        for line in lf:
            if not line:
                continue
            record_line = parse_line(line)
            if record_line:
                yield record_line


def create_report(log_file):
    records = read_log_file(log_file)
    report_dict = {'user_agents': {}, 'bytes': {}}

    for i in records:
        if i[3] in report_dict['user_agents']:
            report_dict['user_agents'][i[3]] += 1
        else:
            report_dict['user_agents'][i[3]] = 1

        if i[0] in report_dict and i[1] in report_dict[i[0]]:
            report_dict[i[0]][i[1]] += 1
        elif i[0] in report_dict and i[1] not in report_dict[i[0]]:
            report_dict[i[0]][i[1]] = 1
        else:
            report_dict[i[0]] = {i[1]: 1}

        if i[0] in report_dict['bytes']:
            report_dict['bytes'][i[0]] += i[2]
        else:
            report_dict['bytes'][i[0]] = i[2]

    return report_dict


def get_most_frequent_agent(report):
    agent = sorted([[i[1], i[0]] for i in report['user_agents'].items()], reverse=True)[0]
    return agent


def main(log_file, ip):
    report_name = f"{log_file}-{datetime.now()}-report.txt"

    new_report = create_report(log_file)
    freq_agent = get_most_frequent_agent(new_report)

    with open(report_name, 'a') as rp:
        rp.write(f"most frequent user agent: {freq_agent[1]} - used {freq_agent[0]} times ")
        rp.write('\n')
        rp.write('\n')
        rp.write(f"number of requests for {ip}:")
        rp.write('\n')
        for i in new_report[ip].items():
            rp.write(f"{i[0]}  -  {i[1]} requests")
            rp.write('\n')
        rp.write('\n')
        rp.write("total amount of data:")
        rp.write('\n')
        for i in new_report['bytes'].items():
            rp.write(f"{i[1]} bytes for {i[0]}")
            rp.write('\n')

    return report_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--log_file', default='access.log')
    parser.add_argument('--ip', default='193.106.31.130')
    args = parser.parse_args()

    log_file_path = os.getcwd()

    log_file = os.path.join(log_file_path, args.log_file)
    ip = args.ip

    report = main(log_file, ip)
    print(f"your report in {report} file")

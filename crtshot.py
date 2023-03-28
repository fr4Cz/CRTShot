#!/usr/bin/env python3
from selenium import webdriver
from time import sleep,time
import requests as req
import argparse as ap
import json


def main():
    parser = ap.ArgumentParser()
    parser.add_argument('-d','--domain', type=str, help='TLD to request certificates from')
    parser.add_argument('--subdomains-only', action='store_true', help='Only list subdomains')
    args = parser.parse_args()

    if args.domain:
        get_banner()
        print('[+] Fetching certificates from CRT.sh')
        print('[+] IMPORTANT! Wildcard certificates will be dropped from final results!')
        crt = get_certificates(args.domain)
        if args.subdomains_only:
            for subdomain in subdomains:
                print("     {}".format(subdomain))
            exit(0)

        print('[+] Fetching screenshots')
        get_screenshots()
            
    else:
        print('No TLD to fetch information from')
        exit(0)

def get_certificates(tld):
    try:
        res = req.get('https://crt.sh/?q={}&output=json'.format(tld))
        res.raise_for_status()

        if res.status_code != 204:
            content = res.content.decode('utf-8')
            jsondata = json.loads(content)
            for i in range(len(jsondata)):  
                # Extracting Subdomains
                name_value = jsondata[i]['name_value']
                get_subdomains(name_value)

            if len(subdomains) < 1:
                print('[+] Found no subdomains for domain: {}'.format(tld))
            else:
                print('[+] Found {} subdomains'.format(len(subdomains)))
            return

        else:
            print('[x] No content (HTTP/204)')
    except:
            print('[x] Failed to parse subdomains ...')
    exit(1)

def get_subdomains(dirty_subs):
    if dirty_subs.find("\n"):
        subdomain_list = dirty_subs.split("\n")
        for subdomain in subdomain_list:
            if subdomain.find('*'):
                if subdomain not in subdomains:
                    subdomains.add(subdomain)
            else:
                pass

def get_screenshots():
    active = 0
    for p in ['http', 'https']:
        for sub in subdomains:
            url = '{}://{}'.format(p, sub)
            try:
                res = req.get(url, timeout=25)
                if res.ok:
                    active += 1

                    # Take screenshot
                    driver = webdriver.Firefox()
                    driver.get(url)
                    sleep(1)
                    
                    screenshot_file = '{}-{}-{}-screenshot.png'.format(time(), p, sub)
                    driver.get_screenshot_as_file(screenshot_file)
                    driver.quit()

                    print(' [*] Screenshot {} generated'.format(screenshot_file))
            except:
                pass

    print('[+] {}/{} Active subdomains found'.format(active, len(subdomains)))

def get_banner():
    print('   _____ _____ _______ _____ _           _   ')
    print('  / ____|  __ \__   __/ ____| |         | |  ')
    print(' | |    | |__) | | | | (___ | |__   ___ | |_ ')
    print(' | |    |  _  /  | |  \___ \| \'_ \ / _ \| __|')
    print(' | |____| | \ \  | |  ____) | | | | (_) | |_ ')
    print('  \_____|_|  \_\ |_| |_____/|_| |_|\___/ \__|')
    print('                                             ')
    print('                     https://github.com/fr4Cz', end="\n\n")

if __name__ == '__main__':
    subdomains = set()
    main()


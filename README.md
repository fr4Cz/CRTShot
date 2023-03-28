# CRTShot
CRTShot was written to create screenshots from subdomains found by requesting crt.sh


## Screenshots from domains
```
$ python3 crtshot.py -d github.com
   _____ _____ _______ _____ _           _   
  / ____|  __ \__   __/ ____| |         | |  
 | |    | |__) | | | | (___ | |__   ___ | |_ 
 | |    |  _  /  | |  \___ \| '_ \ / _ \| __|
 | |____| | \ \  | |  ____) | | | | (_) | |_ 
  \_____|_|  \_\ |_| |_____/|_| |_|\___/ \__|
                                             
                     https://github.com/fr4Cz

[+] Fetching certificates from CRT.sh
[+] IMPORTANT! Wildcard certificates will be dropped from final results!
[+] Found 84 subdomains
[+] Fetching screenshots
 [*] Screenshot 1680040726.17947-http-slack.github.com-screenshot.png generated
 [*] Screenshot 1680040733.3897915-http-education.github.com-screenshot.png generated
 [*] Screenshot 1680040738.3055406-http-support@github.com-screenshot.png generated
...............
...............
 [*] Screenshot 1680041470.8320022-https-examregistration.github.com-screenshot.png generated
 [*] Screenshot 1680041475.9319198-https-docs.github.com-screenshot.png generated
 [*] Screenshot 1680041634.9886158-https-community.github.com-screenshot.png generated
 [*] Screenshot 1680041642.798309-https-help.github.com-screenshot.png generated
[+] 51/84 Active subdomains found

```

## Listing subdomains without screenshots
NOTE! Listing subdomains will not test for validity
```
$ python3 crtshot.py -d github.com --subdomains-only
   _____ _____ _______ _____ _           _   
  / ____|  __ \__   __/ ____| |         | |  
 | |    | |__) | | | | (___ | |__   ___ | |_ 
 | |    |  _  /  | |  \___ \| '_ \ / _ \| __|
 | |____| | \ \  | |  ____) | | | | (_) | |_ 
  \_____|_|  \_\ |_| |_____/|_| |_|\___/ \__|
                                             
                     https://github.com/fr4Cz

[+] Fetching certificates from CRT.sh
[+] IMPORTANT! Wildcard certificates will be dropped from final results!
[+] Found 84 subdomains
     vpn-ca.iad.github.com
     codespaces-ppe.github.com
     skyline.github.com
     offer.github.com
     raw.github.com
     docs-front-door.github.com
     graphql.github.com
     jobs.github.com
     id.github.com
     ......
     ......
```


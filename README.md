kyl191.letsencrypt
=========

Ansible role for installing Let's Encrypt & creating certs

Requirements
------------

The sites var expects the list of sites to create keys for to be stored as a dict.
By default this playbook expects:
- all sites are stored in a common directory (like /var/www/site.doma.in)
  - if this is not case, add root: /path/to/webroot as a key under the site name
- each key in the dict is a domain
  - no other options
- each site can only have 1 alternate name
  - specify an alternate domain with alt: www.doma.in
- by default, you're creating a new legit cert.
  - For testing, override the default with letsencrypt_server: https://acme-staging.api.letsencrypt.org/directory

You *MUST* specify an email address to use in the playbook, like `letsencrypt_email_address: "letsencrypt@demo.net"`

Role Variables
--------------
Defaults:
letsencrypt_install_path: /root/letsencrypt
letsencrypt_webroot_prefix: /var/www
letsencrypt_webserver_sslroot: /etc/nginx/ssl
letsencrypt_sites_var: letsencrypt_sites
letsencrypt_server: https://acme-v01.api.letsencrypt.org/directory

Dependencies
------------

None. This playbook assumes the existence of nginx, but doesn't fail if nginx isn't available.

Example Playbook
----------------

Standalone Let's Encrypt example:
```
  roles:
    - kyl191.letsencrypt
  vars:
    letsencrypt_sites:
      test.net: ~
      demo.test.io:
        alt: www.demo.test.io
        root: /home/test/demo/
    letsencrypt_email_address: "letsencrypt@demo.net"
    letsencrypt_server: https://acme-staging.api.letsencrypt.org/directory
```
Integration with other roles - let's encrypt can use a dict of sites defined in another var
Pass letsencrypt_sites_var the name of the var:
```
  roles:
    - nginx-proxy
    - kyl191.letsencrypt
  vars:
    nginx_sites:
       test.net: ~
      demo.test.io:
        root: /home/test/demo/
        alt: www.demo.test.io
    letsencrypt_sites_var: nginx_sites
```
License
-------

MIT

Author Information
------------------

Complaints/comments to https://github.com/kyl191/kyl191.letsencrypt

# Sherl0ck

Hunt down social media accounts by username across social networks, which based on maigret and sherlock project.

## About

**Sherl0ck** collect a dossier on a person **by username only**, checking for accounts on a huge number of sites and gathering all the available information from web pages. No API keys required. Sherl0ck is an easy-to-use and powerful fork of [Maigret](https://github.com/soxoj/maigret).

Currently supported more than 2500 sites ([full list](https://github.com/antx-code/sherl0ck/blob/main/sites.md)), search is launched against 500 popular sites in descending order of popularity by default. Also supported checking of Tor sites, I2P sites, and domains (via DNS resolving).

## Main features

* Profile pages parsing, [extraction](https://github.com/soxoj/socid_extractor) of personal info, links to other profiles, etc.
* Recursive search by new usernames and other ids found
* Search by tags (site categories, countries)
* Censorship and captcha detection
* Requests retries

See full description of Maigret features [in the Maigret project documentation](https://maigret.readthedocs.io/en/latest/features.html).

## Installation

### Package installing

**NOTE**: Python 3.8 or higher and poetry is required, **Python 3.8 is recommended.**

```bash

# clone the repo
git clone https://github.com/antx-code/sherl0ck.git && cd sherl0ck

# install the dependencies
poetry install

# usage sherl0ck mode
python3 sherl0ck.py dia sherlock

# use maigret mode
python3 sherl0ck.py run sherlock

```

## Usage examples

```bash
# make json reports on all available sites
python3 sherl0ck.py dia sherlock

# make HTML and PDF reports
python3 sherl0ck.py run user --html --pdf

# search on sites marked with tags photo & dating
python3 sherl0ck.py run user --tags photo,dating

# search for three usernames on all available sites
python3 sherl0ck.py run user1 user2 user3 -a
```

Use `python3 sherl0ck.py --help` to get full options description. Also options [are documented](https://maigret.readthedocs.io/en/latest/command-line-options.html).

## License

MIT © [Sherl0ck](https://github.com/antx-code/sherl0ck.git)<br/>
MIT © [Maigret](https://github.com/soxoj/maigret)<br/>
MIT © [Sherlock Project](https://github.com/sherlock-project/)<br/>
Original Creator of Sherlock Project - [Siddharth Dushantha](https://github.com/sdushantha)

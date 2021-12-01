# adventofcode2021

## One-time Setup

Update the `config.sample` filename to `config`. Update the contents to your configuration.

```text
session=<session_id_from_adventofcode_browser_cookie>
year=YYYY
```

### How to get the session ID

1. When on the [adventofcode.com](adventofcode.com) page, click the `Login` link at the top
1. Login with Github
1. Use a browser extension or the browser's built-in dev tools to view the header information when navigating to the input URL
1. Copy the session ID (e.g. 6e6c95f2ed878507aa5d555e6a46e3c677a904fd0499bd0626abe5635bf4f888feb82118795481e00448fa5e39c3c3fe
)

## Run the setup script

```bash
./new.sh <day_number>
```

The setup script (`new.sh`) will do the following.

1. Create a new subdirectory called `day<day_number>` (e.g. `day1`)
1. Copy the `__template.py` file into the new subdirectory and rename it `a.py`
1. Change the permissions on `a.py` to allow execution
1. Fetch the input for the day's problem and save it to a file named `in` within the subdirectory

## Run your solution

It is recommended that you `cd` into the new day's subdirectory.

```bash
cd day<day_number>
```

To run your solution against the input (`in`) use the following.

```bash
./a.py in
```

## Working on part 2

You can either add onto `a.py` for part 2 of the problem or copy to a new file.

```bash
cp a.py b.py
```


# Overview

This project contains automated tests for the Yandex login page using Selenium and pytest with POM pattern.

## Setup

1. Ensure you have Python 3.x installed.
2. Navigate to the project directory:

```bash
cd yandex_auth_test
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

To run tests, simply use pytest. For example:

```bash
pytest -k test_mail_auth
```

or

```bash
pytest -k "Safari"
```

## Browsers

Currently, the tests support Chrome and Safari. You can specify the browser using the @pytest.mark.browser marker in the test functions.

## Project Structure

pages/: Contains the Page Object Models of the website.

test/: Contains test scripts

logs: Logs and reports

data: Receiving and storing data from jsonplaceholder

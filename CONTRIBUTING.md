# Contributing to the `netscaler.adc` ansible collection

We're glad you want to contribute to this project! This document will help answer common questions you may have during your first contribution.

## Submitting Issues

Contribution need not come in the form of code only. Submitting, confirming, and triaging issues are also important tasks for any project. This project uses GitHub to track all project issues. You can use [Issues](https://github.com/netscaler/ansible-collection-netscaleradc/issues) to submit issues, if any, and feature requests.

We ask you not to submit security concerns via GitHub. For details on submitting potential security issues please see <https://www.citrix.com/about/trust-center/vulnerability-process.html>

## Contributor License Agreement (CLA)

We would love to accept your pull requests! Before we can take them, we have to clear a couple of legal hurdles.

- Please sign the [Contributor License Agreement](https://cla-assistant.io/netscaler/ansible-collection-netscaleradc).
- If you have not signed the above agreement, you will be prompted, via a comment, to sign the CLA when you open a PR.
- You only need to do this once and you are good to go.
- That's it! Thanks for your contribution.

> Note: Submitting issues does not require signing the CLA.

## Pull Requests Process

Before creating a pull request, please ensure the following:

- You have signed the [Contributor License Agreement](https://cla-assistant.io/netscaler/ansible-collection-netscaleradc).
- You have followed the [Coding Style](#coding-style).
- You have run the [tests](#testing).
- You have added a description of your changes to the PR description.
- You have added a link to the issue you are addressing in the PR description.
- You have validated your changes.
- You have added or updated the relevant documentation.
- You have added tests for your changes.
- You have updated the [CHANGELOG.md](./CHANGELOG.md) file with your changes.

## Coding Style

1. This project uses the `ansible-lint` tool to enforce a consistent coding style. There are also some additional checks that are run as part of the CI process. You can run the checks locally using the following command:

    ```bash
    make lint
    ```

2. Format your code using the make target

    ```bash
    make fmt
    ```

## Testing

1. Run sanity tests using the make target

    ```bash
    make test_sanity
    ```

2. Run the integration tests using the make target

    a. Update your ADC credentials in the [tests/integration/integration_config.yml](./tests/integration/integration_config.yml) file

    b. Run the below make target

    ```bash
    make test_int
    ```

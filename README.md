A common repository for all l10n of payments.

Assumes that:
* (payments-config)[https://github.com/mozilla/payments-config/] is cloned at ../payments-config.
* (payments-ui)[https://github.com/mozilla/payments-ui/] is cloned at ../payments-ui.

Commands:

`python generate.py --repo=[repo] --action=[action]``

* Supported repos: `payments-config`, `payments-ui`

* Supported actions:
    * `generate_pot`: generates the .pot files from the source.
    * `generate_po`: generates the .po files from the .pot file for that repo.
    * `generate_mo`: generates the .mo files from the .po file for that repo.

Because xgettext doesn't support JavaScript files, `generate_pot` cannot
be run against `payments-ui`. Instead go to the `payments-ui` repo and use the
extraction commands there.

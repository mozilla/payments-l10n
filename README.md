A common repository for all l10n of payments.

Assumes that:
* [payments-config](https://github.com/mozilla/payments-config/) is cloned at ../payments-config.
* [payments-ui](https://github.com/mozilla/payments-ui/) is cloned at ../payments-ui.

Commands:

`python generate.py --repo=[repo] --action=[action] [--debug]``

* `repo`: one of `payments-config`, `payments-ui`

* `action`:
    * `pot`: generates the .pot files from the source.
    * `po`: generates the .po files from the .pot file for that repo.
    * `mo`: generates the .mo files from the .po file for that repo.

* `debug`: defaults to false. If true, it will process the dbg language.

Because xgettext doesn't support JavaScript files, `pot` cannot
be run against `payments-ui`. Instead go to the `payments-ui` repo and use the
extraction commands there.

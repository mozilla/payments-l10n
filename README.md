A common repository for all l10n of payments.

Assumes that payments-config lives at ../payments-config.

`python generate.py --repo=payments-config --action=generate_po``

Generates the .po files from payments-config into the appropriate locales using
the `possible_locales` defined in `generate.py`.

`python generate.py --repo=payments-config --action=generate_mo`

Generates the .mo files from `payments-config.po` files in this repository.

import argparse
import os
import sys

# All the locales we'll generate gettext files for.
possible_locales = [
    'ca', 'cs', 'cy', 'da', 'de', 'dsb', 'en', 'es', 'es_AR', 'es_CL',
    'et', 'eu', 'ff', 'fr', 'fy', 'he', 'hsb', 'hu', 'id', 'it', 'ja', 'ko',
    'lt', 'nb_NO', 'nl', 'pa', 'pl', 'pt', 'pt_BR', 'rm', 'ru', 'sk', 'sl',
    'sq', 'sr', 'sr_Latn', 'sv', 'sv_SE', 'tr', 'uk', 'zh_CN', 'zh_TW'
]

# For the moment, no locales are actually ready, as they become translated,
# add them to here.
ready_locales = [
    'en', 'fr'
]

root = os.path.abspath(os.path.join(os.path.dirname(__file__)))


def pot(prefix):
    print 'Generating .pot from {}.'.format(prefix)
    if prefix == 'payments-ui':
        raise ValueError('Use i18n abide to generate the .pot file.')

    # Hardcoded for payments_config at the moment.
    filename = os.path.join(root, '..', prefix, 'payments_config/products.py')
    cmd = ('xgettext {} -o locale/templates/LC_MESSAGES/{}.pot'
           .format(filename, prefix))
    os.system(cmd)


def po(prefix, debug):
    print 'Generating .po from {}.'.format(prefix)

    if debug:
        print 'Generating dbg locale.'
        cmd = ('podebug --rewrite=unicode locale/templates/LC_MESSAGES/{0}.pot '
               'locale/dbg/LC_MESSAGES/{0}.po'
               .format(prefix))
        os.system(cmd)
        return

    for locale in possible_locales:
        if locale == 'templates':
            continue
        filename = os.path.join(
            root, 'locale', locale, 'LC_MESSAGES/{}.po'.format(prefix))
        directory = 'locale/{}/LC_MESSAGES'.format(locale)

        if not os.path.exists(directory):
            os.makedirs(directory)

        cmd = ('msginit --input=locale/templates/LC_MESSAGES/{}.pot '
               '--locale={} --no-translator --output={}'
               .format(prefix, locale, filename))
        os.system(cmd)


def mo(prefix, debug):
    print 'Generating .mo for each .po file.'
    for locale in ['dbg' if debug else possible_locales]:
        cmd = ('msgfmt locale/{}/LC_MESSAGES/{}.po '
               '--output-file=locale/{}/LC_MESSAGES/{}.mo'
               .format(locale, prefix, locale, prefix))
        print '... for {}/LC_MESSAGES/{}.po'.format(locale, prefix)
        os.system(cmd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--repo',
        action='store',
        choices=['payments-config', 'payments-ui'],
        dest='repo',
        help='Repository to process',
    )
    parser.add_argument(
        '--action',
        action='store',
        choices=['mo', 'po', 'pot'],
        dest='action',
        help='Action to do'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        dest='debug',
        help='Run the debug locale, ignoring others, defaults to false.'
    )
    parsed = parser.parse_args()
    if parsed.debug:
        print 'Only processing the debug language.'
    locals()[parsed.action](parsed.repo, parsed.debug)

#!/usr/bin/env python

import argparse
import pandas as pd

from pathlib import Path


def format_attribute(content, attribute):
    '''
    Format attribute answer
    '''
    print(content)
    if content:
        if attribute:
            return "**%s**: %s\n" % (attribute, content)
        else:
            return "%s\n" % content
    else:
        return ""


def format_application(df, out_fp):
    '''
    Format pending applications

    :param df: data frame with applications
    :param out_fp: Path to file with nice looking applications
    '''
    colname_text = {
        'First Name': 'First Name',
        'Last Name': 'Last Name',
        'Areas of expertise (You can include the ones not listed in the others section)': 'Areas of expertise',
        'Biography (Who are you? What do you want people to know about you?)': "Biography",
        'What style of mentoring do you prefer?': "What style of mentoring do you prefer?",
        'What goal(s) would you like to work on with your mentor? For example:- Help with creating a tool, tutorial, or running data analysis': "What goal(s) would you like to work on with your mentor?",
        'Why do you want to be a mentee? What do you hope to achieve from it?':"Why do you want to be a mentee? What do you hope to achieve from it?",
        'What do you expect from your mentor?':"What do you expect from your mentor?",
        'Do you have previous mentoring experience?':"Do you have previous mentoring experience?",
        "If yes, explain": "",
        'What spoken language do you prefer for your mentoring calls?': 'What spoken language do you prefer for your mentoring calls?',
        'How often would you be prepared to have contact with your mentor?': 'How often would you be prepared to have contact with your mentor?',
        'When do you join Galaxy?': 'When do you join Galaxy?'
    }
    df = df.fillna("")

    with out_fp.open('w') as out_f:
        for index, row in df.iterrows():
            if row['Status'] == 'Pending':
                for colname in colname_text:
                    out_f.write(format_attribute(row[colname], colname_text[colname]))
                out_f.write("\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get applications')
    subparser = parser.add_subparsers(dest='command')
    # Format application
    formatapplication = subparser.add_parser('formatapplication', help="Format pending applications")
    application = formatapplication.add_mutually_exclusive_group()
    application.add_argument('-af', '--application_fp', help="Path to application sheet file")
    application.add_argument('-au', '--application_url', help="URL to application sheet file")
    formatapplication.add_argument('-o', '--out_fp', help="Path to application output file")

    args = parser.parse_args()
    if args.command == 'formatapplication':
        if args.application_fp:
            application_df = pd.read_csv(Path(args.application_fp), )
        else:
            application_df = pd.read_csv(args.application_url)
        format_application(application_df, Path(args.out_fp))
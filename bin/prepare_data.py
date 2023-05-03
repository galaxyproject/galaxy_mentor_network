#!/usr/bin/env python

import argparse
import pandas as pd

from pathlib import Path


colname_text = {
    'Timestamp': 'Application date',
    #'First Name': 'First Name',
    #'Last Name': 'Last Name',
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

def format_attribute(content, attribute):
    '''
    Format attribute answer
    '''
    if content:
        if attribute:
            return "**%s**: %s\n" % (attribute, content)
        else:
            return "%s\n" % content
    else:
        return ""


def format_application(row, type, out_f):
    '''

    '''
    out_f.write("---\n")
    out_f.write("### New application\n")
    out_f.write("\n")
    out_f.write("---\n")
    out_f.write("\n")
    for colname in colname_text:
        out_f.write(format_attribute(row[colname], colname_text[colname]))
    out_f.write("\n")
    out_f.write("---\n")
    out_f.write("\n")
    #if type == 'nm':
    #    out_f.write("### Actions for Network Managers\n\n")
    #    out_f.write("Please vote:\n")
    #    out_f.write("- **Light Bulb (:bulb:)** for direct submission to the mentor channel (good application)\n")
    #    out_f.write("- **Thumbs up (:+1:)** for submission to the mentor channel, asking if any mentor has a possible project for them (a bit vague application)\n")
    #    out_f.write("- **Gear (:gear:)** for asking them to rework their application (vague application)\n")
    #elif type == "mentors":
    #    out_f.write("### Actions for Mentors\n\n")
    #    out_f.write("Interested in mentoring this person? Let us know using the reactions\n")
    #    out_f.write("- **Thumbs up (:+1:)** to mentor the project in its actual format\n")
    #    out_f.write("- **OK hand (:ok_hand:)** if this application is a big vague but you may have an actual project that fits this person\n")
    #out_f.write("\n")
    #out_f.write("---\n")
    #out_f.write("\n\n\n")


def format_applications(df, out_dp):
    '''
    Format pending applications

    :param df: data frame with applications
    :param out_dp: Path to folder with nice looking applications
    '''
    pending_fp = out_dp / Path("pending_mentee_applications")
    waiting_fp = out_dp / Path("waiting_gmentor_mentee_applications")
    df = df.fillna("")
    with pending_fp.open('w') as pending_f:
        with waiting_fp.open('w') as waiting_f:
            for index, row in df.iterrows():
                if row['Status'] == 'Pending':
                    format_application(row, "nm", pending_f)
                elif row['Status'] == 'Waiting for Gmentor':
                    format_application(row, "mentors", waiting_f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get applications')
    subparser = parser.add_subparsers(dest='command')
    # Format application
    formatapplication = subparser.add_parser('formatapplication', help="Format pending applications")
    application = formatapplication.add_mutually_exclusive_group()
    application.add_argument('-af', '--application_fp', help="Path to application sheet file")
    application.add_argument('-au', '--application_url', help="URL to application sheet file")
    formatapplication.add_argument('-o', '--out_dp', help="Path to application output folder")

    args = parser.parse_args()
    if args.command == 'formatapplication':
        if args.application_fp:
            application_df = pd.read_csv(Path(args.application_fp), )
        else:
            application_df = pd.read_csv(args.application_url)
        format_applications(application_df, Path(args.out_dp))
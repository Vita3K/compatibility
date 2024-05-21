"""
Retrieves log files from given ("REPO_NAMES") repositories
for offline/batch processing/searching.
Iterates thought all issues, finds the last posted comment
that contains at least one file and downloads all files to
appropriately named directories, with the filename being
the Issue title (game name/titleID).
Replaces invalid characters in that file name with '-' and
if there are multiple files in an issue, appends the
filenames with "_N" where "N" is a number starting from 0.
Author: VelocityRa
Date: 18/8/2018
https://gist.github.com/VelocityRa/c01699914c0179eb05d78bee2aeaf9c1
"""

from github import *
import re
import os
import os.path
import urllib.request

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO_NAMES = ["Vita3K/compatibility", "Vita3K/homebrew-compatibility"]
LOGS_BASE_PATH = "logs"

# Regular expression to find log file paths
log_files_re = re.compile(r"/files/\d+/\w+\.\w+")

# Ensure logs base path exists
logs_path = os.path.normpath(os.path.join(os.getcwd(), LOGS_BASE_PATH))
if not os.path.exists(logs_path):
    os.mkdir(logs_path)

# Function to find log files in a comment or issue body
def find_log_files(text):
    return log_files_re.findall(text)

# Function to fix up log file paths (modify this function as needed)
def fixup_log_file_paths(log_files, repo_name):
    return [r"https://github.com/" + repo_name + "/" + log_file for log_file in log_files]

# Function to normalize the file name
def normalize_file_name(title):
    # Remove invalid characters and replace them with underscores
    return re.sub(r'[^\w]+', '_', title)

# Initialize GitHub API client
g = Github(login_or_token=GITHUB_TOKEN)

for repo_full_name in REPO_NAMES:
    print("Getting logs for repo: {}".format(repo_full_name))

    # Extract the repository name from the full repository path
    (_, repo_name) = os.path.split(repo_full_name)
    log_base_path = os.path.join(logs_path, repo_name)
    if not os.path.exists(log_base_path):
        os.mkdir(log_base_path)

    # Get the repository object
    repo = g.get_repo(repo_full_name, lazy=False)
    issues = repo.get_issues()

    log_count = 0
    error_log_count = 0
    for issue in issues:
        # Combine issue body and comments to search for log files
        comments = issue.get_comments()
        first_comment = issue.body

        if comments:
            for comment in comments:
                first_comment += "\n" + comment.body
        logs_posted = find_log_files(first_comment)

        if len(logs_posted) == 0:
            logs_posted = find_log_files(issue.body)

        logs_posted = fixup_log_file_paths(logs_posted, repo_full_name)

        print("Issue #{} for game {}".format(issue.id, issue.title))
        for log_id, log in enumerate(logs_posted):
            # Normalize the file name to avoid invalid characters
            normalized_file_name = normalize_file_name(issue.title)
            if len(logs_posted) > 1:
                normalized_file_name += "_" + str(log_id)
            normalized_file_name += ".log"

            log_full_path_cur = os.path.join(log_base_path, normalized_file_name)

            try:
                print("Retrieving: {} as {}".format(log, normalized_file_name))
                log_content = urllib.request.urlopen(log).read().decode('utf-8')

                # Write to individual log file
                with open(log_full_path_cur, 'w') as individual_log_file:
                    individual_log_file.write(log_content)
                log_count += 1
            
            except Exception as e:
                print(f"Error at Retrieving: {log} - {str(e)}")
                error_log_count += 1

    print("Total logs retrieved: {}".format(log_count))
    print("Error logs count: {}".format(error_log_count))

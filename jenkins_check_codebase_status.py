import csv
import hashlib
import os


sha1_data = {}

# codebase must be a directory
codebase = '/home/rakesh/Desktop'
sha1_file = '/home/rakesh/Documents/doc/jenkins_project/sha1_data.csv'


def get_all_files_in_directory(directory):
    if os.path.exists(directory):
        all_files = []
        for path, subdirs, files in os.walk(directory):
            for sub_url in files:
                all_files.append(os.path.join(path, sub_url))
        return all_files
    else:
        print 'folder not found'


def get_sha1sum(location):
    s = hashlib.sha1(open(location, 'rb').read())
    return s.hexdigest()


def save_codebase(codebase, tmp_sha_loc):
    if not os.path.exists(sha1_file):
        print "Scanning codebase for the first time... Bear with me it'll take a lot of time"
        with open(sha1_file, 'wb') as csv_file:
            csv_file.write('Empty for now')
        save_codebase(codebase, sha1_file)
    all_files = get_all_files_in_directory(codebase)
    for location in all_files:
        sha1_data[location] = get_sha1sum(location)
    with open(tmp_sha_loc, 'wb') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ',')
        csv_writer.writerow(['LOCATION','SHA1SUM'])
        for key, value in sha1_data.iteritems():
            csv_writer.writerow([key, value])


def check_codebase_sha(tmp_sha_loc):
    save_codebase(codebase, tmp_sha_loc)
    if get_sha1sum(sha1_file) != get_sha1sum(tmp_sha_loc):
        print 'You have changed something'
        save_codebase(codebase, sha1_file)
    else:
        print 'Same codebase'

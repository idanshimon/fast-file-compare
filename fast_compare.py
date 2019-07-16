#!/usr/bin/env python
"""Foobar.py: Description of what foobar does."""

__author__      = "Idan Shimon"
__copyright__   = "Copyright 2019"
__license__		= "GPL	"

import sys
import os
import hashlib
import multiprocessing
import time
import logging
import logging

LOGLEVEL = logging.DEBUG
logging.basicConfig(level=LOGLEVEL, format='%(message)s')

HASH_TYPE = 'md4'
MB = 1024*1024
GB = 1024*1024*1024
SMALL_FILE_MAX_SIZE = 1024*1024

TOTAL_PARTS = multiprocessing.cpu_count()
TOTAL_PARTS_SIZE = 5*GB
PART_SIZE = TOTAL_PARTS_SIZE//TOTAL_PARTS

def usage():
	print('%s [original_file] [compare_file]' % sys.argv[0])

def compute_hash(fpath, index=0, chunk_size=None):
	'''Compute hash for file path
		@the file path to compute the data from
		@starting index - pointer in the file
		@chunk_size - how many bytes to read
	'''

	logging.debug('compute hash for file %s (starting index:%s, size:%s)' % (fpath, index, chunk_size))
	with open(fpath, 'rb') as f:
		f.seek(index)
		data = f.read(chunk_size)
		return (index, hashlib.new('md4', data).hexdigest())

def get_hash_small_file(fpath):
	return [compute_hash(fpath)]

def multi_hash(fpath):
	start_time = time.time()

	fsize = os.path.getsize(fpath)

	# If file is smaller than 1MB compute the hash, no point for multiprocessing
	if fsize <= MB:
		return get_hash_small_file(fpath)

	#If file is a "large file" greater than 1MB than activate multiprocessing and get results
	with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
		params = []
		for i in range(0, fsize, PART_SIZE):
			params.append((fpath, i, PART_SIZE, ))
		results = p.starmap(compute_hash, params)
		results.sort(key=lambda x:x[0]) # each item looks like this [(index, hash) ... ] i.e. [(0, 'f6a7fc41c88634c4232d9d76301bf429'), (1, 'dksjalkdjsalkdjlksjd...') ..]
		sorted_results = [i[1] for i in results]
		end_time = time.time()
		logging.debug('Compute hash for %s Took %.6f seconds (Size:%d)' % (fpath, end_time-start_time, fsize))

		return sorted_results
	
def is_identicle(src_file, dest_file):
	'''Compare between two files in an effcient way'''
	if os.path.getsize(src_file) == os.path.getsize(dest_file):
		s1 = multi_hash(src_file)
		s2 = multi_hash(dest_file)
		if (len(s1) == len(s2) and s1 == s2):
			return True
		else:
			logging.error('Error: Files content is not the same')
	else:
		logging.error('Error: Files are different sizes')
		return False
		
def main():
	if len(sys.argv) < 3:
		usage()
		exit(1)

	src_file = sys.argv[1]
	dest_file = sys.argv[2]

	if not os.path.isfile(src_file):
		logging.error('Error: source file not found')
	if not os.path.isfile(dest_file):
		logging.error('Error: destination file not found')


	logging.debug('CPU COUNT: %d' % multiprocessing.cpu_count())
	start_time = time.time()
	
	files_equal = is_identicle(src_file, dest_file)

	end_time = time.time()
	logging.info('Compare Took %.6f seconds' % (end_time-start_time))
	if files_equal:
		logging.info('All Good!')
	else:
		logging.error('Error: Files are not equal')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
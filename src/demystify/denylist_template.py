# -*- coding: utf-8 -*-


denylist_template = """########################################################################
# Denylist and Rogues output configuration for demystify.
#
# Denylist: describes files or filenames to highlight in a Demystify
#           report. Denylist items might be files that are not on your
#           accepted formats policy. For example, system files. Denylist
#           entries might also be filenames that are well known that are
#           known not to fit your accepted formats policy, e.g.
#           .DS_Store, or Thumbs.db.
#
# Rogues:   Describes 'sets' of Demystify analysis reports that tend to
#           highlight issues that require further investigation and so
#           will be exported as a file path listing to be used with
#           tools like rsync. The opposite of a Rogues report is a
#           heroes report. The heroes report should contain a file path
#           listing that should not require further triage.
#
#           Rogues and heroes can be used during triage of collections.
#           Organizations capable of processing split ingests may also
#           benefit.
#
#           What makes Rogues/Heroes special is that as a file listing
#           a tool like Rsync in combination with the mechanism can be
#           used to create two separate on-disk views of a file
#           classification scheme (or file tree), where one tree
#           contains all objects that might require further appraisal.
#           And another that, with greater confidence, can be accepted
#           by the organization, or appraised less rigorously, assuming
#           there has already been one round of appraisal by the donor
#           and your org.
#
# MIMEtype and PUID listing for file formats that may require further
# analysis, e.g. ZIP files for their contents, or OLE2 because it
# requires a more accurate identification.
#
# 	fmt/682 - Thumbs.db
#	fmt/468 - ISO Image
#	fmt/394 - .DS_Store
#	fmt/111 - OLE2
#	fmt/473 - MS Office Container
#	fmt/474 - MS Office Help
#	fmt/503 - Macintosh Resource Fork
#	fmt/523 - Macro Enabled OOXML
#	fmt/819 - CDROM/XA
#	x-fmt/157 - interchange file
#	x-fmt/418 - icon file
#	x-fmt/419 - DVD data file
#	x-fmt/428 - windows shortcut
#	x-fmt/429 - web archive
#	x-fmt/453 - truetype font
#	application/x-sh - shell file
#	application/vnd.ms-tnef - MS transport neutral encapsulation format
#	application/x-stuffit - stuffit archive
#	application/x-pak - PAK archive
#	application/x-mswinurl - internet shortcut
#	application/x-executable - executable file
#	x-fmt/263 - zip
#	x-fmt/266 - gzip
#
########################################################################

[denylist]

# PUIDs and IDs that are to be filtered using the denylist.
#
# 	e.g. False or list of PUIDS, fmt/682,fmt/111
#
ids=fmt/111,fmt/682,fmt/394,x-fmt/409,x-fmt/410,x-fmt/411,fmt/688,fmt/689,fmt/690,fmt/691,fmt/468,fmt/473,fmt/474,fmt/503,fmt/523,fmt/819,x-fmt/157,x-fmt/418,x-fmt/419,x-fmt/428,x-fmt/429,x-fmt/453,application/x-sh,application/vnd.ms-tnef,application/x-stuffit,application/x-pak,application/x-mswinurl,application/x-executable,x-fmt/263,x-fmt/266,fmt/583,fmt/524

# File names can be used to filter specific filenames from across an
# extract.
#
# 	e.g. .DS_Store
#
filenames='.DS_Store','Untitled Document','desktop.ini','(copy','ZbThumbnail.info','lorem','New Microsoft Word Document','Bin.dat','Thumbs.db', 'vitae', 'Appointments', 'CV', 'Application', 'Resume', 'Appointment', 'Test', 'list', 'member', 'people', 'address', 'phone'

# Directory names can also be filtered from the extract.
#
directorynames='Untitled Folder','New Folder','(copy','.git','lorem'

# File extensions can be filtered where a tool is not able to identify
# by file format signature.
#
# 	e.g. .tmp
#
fileextensions='.ini','.exe','.cfg','.dll','.lnk','.tmp'

[rogues]

# Sets of analyses that are run by Demystify for which you want file
# listings for.
#
#	e.g. To separately investigate duplicate files
#		 set: `duplicatechecksums=True`
#

; Output unidentified files.
unidentified=False

; Output duplicate files.
duplicatechecksums=False

; Output PRONOM only identification.
pronomonly=True

; Output denylist.
denylist=True

; Output non-ascii filenames.
nonasciifilenames=True

; Output non-ascii directories.
nonasciidirs=True

; Output zero-byte files.
zerobytefiles=True

; Output multiple IDs.
multipleids=False

; Output extension mismatches.
extensionmismatches=True
"""

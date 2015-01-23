#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sg3_utils
Version  : 1.41
Release  : 7
URL      : http://sg.danny.cz/sg/p/sg3_utils-1.41.tgz
Source0  : http://sg.danny.cz/sg/p/sg3_utils-1.41.tgz
Summary  : Utilities for devices that use SCSI command sets
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+
Requires: sg3_utils-bin
Requires: sg3_utils-lib
Requires: sg3_utils-doc

%description
Collection of Linux utilities for devices that use the SCSI command set.
Includes utilities to copy data based on "dd" syntax and semantics (called
sg_dd, sgp_dd and sgm_dd); check INQUIRY data and VPD pages (sg_inq); check
mode and log pages (sginfo, sg_modes and sg_logs); spin up and down
disks (sg_start); do self tests (sg_senddiag); and various other functions.
See the README, ChangeLog and COVERAGE files. Requires the linux kernel 2.4
series or later. In the 2.4 series SCSI generic device names (e.g. /dev/sg0)
must be used. In the 2.6 series and later other device names may be used as
well (e.g. /dev/sda).

Warning: Some of these tools access the internals of your system
and the incorrect usage of them may render your system inoperable.

%package bin
Summary: bin components for the sg3_utils package.
Group: Binaries

%description bin
bin components for the sg3_utils package.


%package dev
Summary: dev components for the sg3_utils package.
Group: Development
Requires: sg3_utils-lib
Requires: sg3_utils-bin

%description dev
dev components for the sg3_utils package.


%package doc
Summary: doc components for the sg3_utils package.
Group: Documentation

%description doc
doc components for the sg3_utils package.


%package lib
Summary: lib components for the sg3_utils package.
Group: Libraries

%description lib
lib components for the sg3_utils package.


%prep
%setup -q -n sg3_utils-1.41

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/scsi_logging_level
/usr/bin/scsi_mandat
/usr/bin/scsi_readcap
/usr/bin/scsi_ready
/usr/bin/scsi_satl
/usr/bin/scsi_start
/usr/bin/scsi_stop
/usr/bin/scsi_temperature
/usr/bin/sg_compare_and_write
/usr/bin/sg_copy_results
/usr/bin/sg_dd
/usr/bin/sg_decode_sense
/usr/bin/sg_emc_trespass
/usr/bin/sg_format
/usr/bin/sg_get_config
/usr/bin/sg_get_lba_status
/usr/bin/sg_ident
/usr/bin/sg_inq
/usr/bin/sg_logs
/usr/bin/sg_luns
/usr/bin/sg_map
/usr/bin/sg_map26
/usr/bin/sg_modes
/usr/bin/sg_opcodes
/usr/bin/sg_persist
/usr/bin/sg_prevent
/usr/bin/sg_raw
/usr/bin/sg_rbuf
/usr/bin/sg_rdac
/usr/bin/sg_read
/usr/bin/sg_read_block_limits
/usr/bin/sg_read_buffer
/usr/bin/sg_read_long
/usr/bin/sg_readcap
/usr/bin/sg_reassign
/usr/bin/sg_referrals
/usr/bin/sg_rep_zones
/usr/bin/sg_requests
/usr/bin/sg_reset
/usr/bin/sg_reset_wp
/usr/bin/sg_rmsn
/usr/bin/sg_rtpg
/usr/bin/sg_safte
/usr/bin/sg_sanitize
/usr/bin/sg_sat_identify
/usr/bin/sg_sat_phy_event
/usr/bin/sg_sat_read_gplog
/usr/bin/sg_sat_set_features
/usr/bin/sg_scan
/usr/bin/sg_senddiag
/usr/bin/sg_ses
/usr/bin/sg_ses_microcode
/usr/bin/sg_start
/usr/bin/sg_stpg
/usr/bin/sg_sync
/usr/bin/sg_test_rwbuf
/usr/bin/sg_turs
/usr/bin/sg_unmap
/usr/bin/sg_verify
/usr/bin/sg_vpd
/usr/bin/sg_wr_mode
/usr/bin/sg_write_buffer
/usr/bin/sg_write_long
/usr/bin/sg_write_same
/usr/bin/sg_write_verify
/usr/bin/sg_xcopy
/usr/bin/sg_zone
/usr/bin/sginfo
/usr/bin/sgm_dd
/usr/bin/sgp_dd

%files dev
%defattr(-,root,root,-)
/usr/include/scsi/sg_cmds.h
/usr/include/scsi/sg_cmds_basic.h
/usr/include/scsi/sg_cmds_extra.h
/usr/include/scsi/sg_cmds_mmc.h
/usr/include/scsi/sg_io_linux.h
/usr/include/scsi/sg_lib.h
/usr/include/scsi/sg_lib_data.h
/usr/include/scsi/sg_linux_inc.h
/usr/include/scsi/sg_pt.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sg3_utils
Version  : 1.43r785
Release  : 13
URL      : http://sg.danny.cz/sg/p/sg3_utils-1.43r785.tar.xz
Source0  : http://sg.danny.cz/sg/p/sg3_utils-1.43r785.tar.xz
Summary  : Utilities for devices that use SCSI command sets
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+
Requires: sg3_utils-bin
Requires: sg3_utils-lib
Requires: sg3_utils-license
Requires: sg3_utils-man

%description
Collection of Linux utilities for devices that use the SCSI command set.
Includes utilities to copy data based on "dd" syntax and semantics (called
sg_dd, sgp_dd and sgm_dd); check INQUIRY data and VPD pages (sg_inq); check
mode and log pages (sginfo, sg_modes and sg_logs); spin up and down
disks (sg_start); do self tests (sg_senddiag); and various other functions.
See the README, ChangeLog and COVERAGE files. Requires the linux kernel 2.4
series or later. In the 2.4 series SCSI generic device names (e.g. /dev/sg0)
must be used. In the 2.6 series and later other device names may be used as
well (e.g. /dev/sda). Also some support for NVMe devices, esspecially with
sg_ses to NVMe enclosures.

Warning: Some of these tools access the internals of your system
and the incorrect usage of them may render your system inoperable.

%package bin
Summary: bin components for the sg3_utils package.
Group: Binaries
Requires: sg3_utils-license
Requires: sg3_utils-man

%description bin
bin components for the sg3_utils package.


%package dev
Summary: dev components for the sg3_utils package.
Group: Development
Requires: sg3_utils-lib
Requires: sg3_utils-bin
Provides: sg3_utils-devel

%description dev
dev components for the sg3_utils package.


%package lib
Summary: lib components for the sg3_utils package.
Group: Libraries
Requires: sg3_utils-license

%description lib
lib components for the sg3_utils package.


%package license
Summary: license components for the sg3_utils package.
Group: Default

%description license
license components for the sg3_utils package.


%package man
Summary: man components for the sg3_utils package.
Group: Default

%description man
man components for the sg3_utils package.


%prep
%setup -q -n sg3_utils-1.43r785

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534991250
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534991250
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/sg3_utils
cp COPYING %{buildroot}/usr/share/doc/sg3_utils/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/sg_write_buffer
/usr/bin/rescan-scsi-bus.sh
/usr/bin/scsi_logging_level
/usr/bin/scsi_mandat
/usr/bin/scsi_readcap
/usr/bin/scsi_ready
/usr/bin/scsi_satl
/usr/bin/scsi_start
/usr/bin/scsi_stop
/usr/bin/scsi_temperature
/usr/bin/sg_bg_ctl
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
/usr/bin/sg_read_attr
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
/usr/bin/sg_seek
/usr/bin/sg_senddiag
/usr/bin/sg_ses
/usr/bin/sg_ses_microcode
/usr/bin/sg_start
/usr/bin/sg_stpg
/usr/bin/sg_stream_ctl
/usr/bin/sg_sync
/usr/bin/sg_test_rwbuf
/usr/bin/sg_timestamp
/usr/bin/sg_turs
/usr/bin/sg_unmap
/usr/bin/sg_verify
/usr/bin/sg_vpd
/usr/bin/sg_wr_mode
/usr/bin/sg_write_long
/usr/bin/sg_write_same
/usr/bin/sg_write_verify
/usr/bin/sg_write_x
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
/usr/include/scsi/sg_pr2serr.h
/usr/include/scsi/sg_pt.h
/usr/include/scsi/sg_pt_linux.h
/usr/include/scsi/sg_pt_nvme.h
/usr/include/scsi/sg_unaligned.h
/usr/lib64/libsgutils2.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsgutils2.so.2
/usr/lib64/libsgutils2.so.2.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/sg3_utils/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man8/rescan-scsi-bus.sh.8
/usr/share/man/man8/scsi_logging_level.8
/usr/share/man/man8/scsi_mandat.8
/usr/share/man/man8/scsi_readcap.8
/usr/share/man/man8/scsi_ready.8
/usr/share/man/man8/scsi_satl.8
/usr/share/man/man8/scsi_start.8
/usr/share/man/man8/scsi_stop.8
/usr/share/man/man8/scsi_temperature.8
/usr/share/man/man8/sg3_utils.8
/usr/share/man/man8/sg_bg_ctl.8
/usr/share/man/man8/sg_compare_and_write.8
/usr/share/man/man8/sg_copy_results.8
/usr/share/man/man8/sg_dd.8
/usr/share/man/man8/sg_decode_sense.8
/usr/share/man/man8/sg_emc_trespass.8
/usr/share/man/man8/sg_format.8
/usr/share/man/man8/sg_get_config.8
/usr/share/man/man8/sg_get_lba_status.8
/usr/share/man/man8/sg_ident.8
/usr/share/man/man8/sg_inq.8
/usr/share/man/man8/sg_logs.8
/usr/share/man/man8/sg_luns.8
/usr/share/man/man8/sg_map.8
/usr/share/man/man8/sg_map26.8
/usr/share/man/man8/sg_modes.8
/usr/share/man/man8/sg_opcodes.8
/usr/share/man/man8/sg_persist.8
/usr/share/man/man8/sg_prevent.8
/usr/share/man/man8/sg_raw.8
/usr/share/man/man8/sg_rbuf.8
/usr/share/man/man8/sg_rdac.8
/usr/share/man/man8/sg_read.8
/usr/share/man/man8/sg_read_attr.8
/usr/share/man/man8/sg_read_block_limits.8
/usr/share/man/man8/sg_read_buffer.8
/usr/share/man/man8/sg_read_long.8
/usr/share/man/man8/sg_readcap.8
/usr/share/man/man8/sg_reassign.8
/usr/share/man/man8/sg_referrals.8
/usr/share/man/man8/sg_rep_zones.8
/usr/share/man/man8/sg_requests.8
/usr/share/man/man8/sg_reset.8
/usr/share/man/man8/sg_reset_wp.8
/usr/share/man/man8/sg_rmsn.8
/usr/share/man/man8/sg_rtpg.8
/usr/share/man/man8/sg_safte.8
/usr/share/man/man8/sg_sanitize.8
/usr/share/man/man8/sg_sat_identify.8
/usr/share/man/man8/sg_sat_phy_event.8
/usr/share/man/man8/sg_sat_read_gplog.8
/usr/share/man/man8/sg_sat_set_features.8
/usr/share/man/man8/sg_scan.8
/usr/share/man/man8/sg_seek.8
/usr/share/man/man8/sg_senddiag.8
/usr/share/man/man8/sg_ses.8
/usr/share/man/man8/sg_ses_microcode.8
/usr/share/man/man8/sg_start.8
/usr/share/man/man8/sg_stpg.8
/usr/share/man/man8/sg_stream_ctl.8
/usr/share/man/man8/sg_sync.8
/usr/share/man/man8/sg_test_rwbuf.8
/usr/share/man/man8/sg_timestamp.8
/usr/share/man/man8/sg_turs.8
/usr/share/man/man8/sg_unmap.8
/usr/share/man/man8/sg_verify.8
/usr/share/man/man8/sg_vpd.8
/usr/share/man/man8/sg_wr_mode.8
/usr/share/man/man8/sg_write_buffer.8
/usr/share/man/man8/sg_write_long.8
/usr/share/man/man8/sg_write_same.8
/usr/share/man/man8/sg_write_verify.8
/usr/share/man/man8/sg_write_x.8
/usr/share/man/man8/sg_xcopy.8
/usr/share/man/man8/sg_zone.8
/usr/share/man/man8/sginfo.8
/usr/share/man/man8/sgm_dd.8
/usr/share/man/man8/sgp_dd.8

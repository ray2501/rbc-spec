#!/usr/bin/tclsh

set arch "x86_64"
set base "rbctoolkit-release-0.1.1"
set fileurl "https://github.com/apnadkarni/rbctoolkit/archive/release-0.1.1.tar.gz"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

set var2 [list tar xzvf $base.tar.gz]
exec >@stdout 2>@stderr {*}$var2

cd $base

set var2 [list tar czvf rbc-0.1.1.tar.gz rbc]
exec >@stdout 2>@stderr {*}$var2

file copy rbc-0.1.1.tar.gz ..

cd ..
file delete -force $base
file delete -force $base.tar.gz

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force rbc-0.1.1.tar.gz build/SOURCES
file copy -force configure.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb rbc.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete rbc-0.1.1.tar.gz

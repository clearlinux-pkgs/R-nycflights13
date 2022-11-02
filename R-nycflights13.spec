#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-nycflights13
Version  : 1.0.2
Release  : 48
URL      : https://cran.r-project.org/src/contrib/nycflights13_1.0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/nycflights13_1.0.2.tar.gz
Summary  : Flights that Departed NYC in 2013
Group    : Development/Tools
License  : CC0-1.0
Requires: R-tibble
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
Also includes useful 'metadata' on airlines, airports, weather, and
    planes.

%prep
%setup -q -c -n nycflights13
cd %{_builddir}/nycflights13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641067513

%install
export SOURCE_DATE_EPOCH=1641067513
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nycflights13
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nycflights13
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nycflights13
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc nycflights13 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/nycflights13/DESCRIPTION
/usr/lib64/R/library/nycflights13/INDEX
/usr/lib64/R/library/nycflights13/Meta/Rd.rds
/usr/lib64/R/library/nycflights13/Meta/data.rds
/usr/lib64/R/library/nycflights13/Meta/features.rds
/usr/lib64/R/library/nycflights13/Meta/hsearch.rds
/usr/lib64/R/library/nycflights13/Meta/links.rds
/usr/lib64/R/library/nycflights13/Meta/nsInfo.rds
/usr/lib64/R/library/nycflights13/Meta/package.rds
/usr/lib64/R/library/nycflights13/NAMESPACE
/usr/lib64/R/library/nycflights13/NEWS.md
/usr/lib64/R/library/nycflights13/R/nycflights13
/usr/lib64/R/library/nycflights13/R/nycflights13.rdb
/usr/lib64/R/library/nycflights13/R/nycflights13.rdx
/usr/lib64/R/library/nycflights13/data/Rdata.rdb
/usr/lib64/R/library/nycflights13/data/Rdata.rds
/usr/lib64/R/library/nycflights13/data/Rdata.rdx
/usr/lib64/R/library/nycflights13/help/AnIndex
/usr/lib64/R/library/nycflights13/help/aliases.rds
/usr/lib64/R/library/nycflights13/help/nycflights13.rdb
/usr/lib64/R/library/nycflights13/help/nycflights13.rdx
/usr/lib64/R/library/nycflights13/help/paths.rds
/usr/lib64/R/library/nycflights13/html/00Index.html
/usr/lib64/R/library/nycflights13/html/R.css

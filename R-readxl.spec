#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-readxl
Version  : 1.3.1
Release  : 22
URL      : https://cran.r-project.org/src/contrib/readxl_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/readxl_1.3.1.tar.gz
Summary  : Read Excel Files
Group    : Development/Tools
License  : BSD-2-Clause GPL-3.0
Requires: R-readxl-lib = %{version}-%{release}
BuildRequires : R-Rcpp
BuildRequires : R-cellranger
BuildRequires : R-cli
BuildRequires : R-mime
BuildRequires : R-progress
BuildRequires : R-tibble
BuildRequires : R-utf8
BuildRequires : buildreq-R

%description
# readxl <img src='man/figures/logo.png' align="right" height="139" />
[![Travis-CI Build
Status](https://travis-ci.org/tidyverse/readxl.svg?branch=master)](https://travis-ci.org/tidyverse/readxl)
[![AppVeyor Build
Status](https://ci.appveyor.com/api/projects/status/github/tidyverse/readxl?branch=master&svg=true)](https://ci.appveyor.com/project/tidyverse/readxl)
[![Coverage
Status](https://img.shields.io/codecov/c/github/tidyverse/readxl/master.svg)](https://codecov.io/github/tidyverse/readxl?branch=master)
[![CRAN\_Status\_Badge](https://www.r-pkg.org/badges/version/readxl)](https://cran.r-project.org/package=readxl)
[![lifecycle](https://img.shields.io/badge/lifecycle-stable-brightgreen.svg)](https://www.tidyverse.org/lifecycle/#stable)

%package lib
Summary: lib components for the R-readxl package.
Group: Libraries

%description lib
lib components for the R-readxl package.


%prep
%setup -q -c -n readxl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552869384

%install
export SOURCE_DATE_EPOCH=1552869384
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readxl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readxl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readxl
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  readxl || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/readxl/DESCRIPTION
/usr/lib64/R/library/readxl/INDEX
/usr/lib64/R/library/readxl/Meta/Rd.rds
/usr/lib64/R/library/readxl/Meta/features.rds
/usr/lib64/R/library/readxl/Meta/hsearch.rds
/usr/lib64/R/library/readxl/Meta/links.rds
/usr/lib64/R/library/readxl/Meta/nsInfo.rds
/usr/lib64/R/library/readxl/Meta/package.rds
/usr/lib64/R/library/readxl/Meta/vignette.rds
/usr/lib64/R/library/readxl/NAMESPACE
/usr/lib64/R/library/readxl/NEWS.md
/usr/lib64/R/library/readxl/R/readxl
/usr/lib64/R/library/readxl/R/readxl.rdb
/usr/lib64/R/library/readxl/R/readxl.rdx
/usr/lib64/R/library/readxl/doc/cell-and-column-types.R
/usr/lib64/R/library/readxl/doc/cell-and-column-types.Rmd
/usr/lib64/R/library/readxl/doc/cell-and-column-types.html
/usr/lib64/R/library/readxl/doc/index.html
/usr/lib64/R/library/readxl/doc/sheet-geometry.R
/usr/lib64/R/library/readxl/doc/sheet-geometry.Rmd
/usr/lib64/R/library/readxl/doc/sheet-geometry.html
/usr/lib64/R/library/readxl/extdata/clippy.xls
/usr/lib64/R/library/readxl/extdata/clippy.xlsx
/usr/lib64/R/library/readxl/extdata/datasets.xls
/usr/lib64/R/library/readxl/extdata/datasets.xlsx
/usr/lib64/R/library/readxl/extdata/deaths.xls
/usr/lib64/R/library/readxl/extdata/deaths.xlsx
/usr/lib64/R/library/readxl/extdata/geometry.xls
/usr/lib64/R/library/readxl/extdata/geometry.xlsx
/usr/lib64/R/library/readxl/extdata/type-me.xls
/usr/lib64/R/library/readxl/extdata/type-me.xlsx
/usr/lib64/R/library/readxl/help/AnIndex
/usr/lib64/R/library/readxl/help/aliases.rds
/usr/lib64/R/library/readxl/help/figures/logo.png
/usr/lib64/R/library/readxl/help/paths.rds
/usr/lib64/R/library/readxl/help/readxl.rdb
/usr/lib64/R/library/readxl/help/readxl.rdx
/usr/lib64/R/library/readxl/html/00Index.html
/usr/lib64/R/library/readxl/html/R.css
/usr/lib64/R/library/readxl/tests/BIFF5-LABEL-record-string-read-mac-10-11.supp
/usr/lib64/R/library/readxl/tests/testthat.R
/usr/lib64/R/library/readxl/tests/testthat/helper.R
/usr/lib64/R/library/readxl/tests/testthat/sheets/65536-rows-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/Ekaterinburg_IP_9.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/biff5-label-records.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/big-texty-numbers-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/big-texty-numbers-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/blanks.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/blanks.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/dates-1900-LibreOffice.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/dates-1900.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/dates-1904.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/dates-leap-year-1900-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/dates-leap-year-1900-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/datetime-rounding.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/datetime-rounding.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/embedded-chartsheet.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/empty-named-column.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/empty-named-column.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/empty-sheets.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/empty-sheets.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/geometry.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/geometry.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/inlineStr.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/inlineStr2.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/iris-excel-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/iris-excel-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/iris-google-doc.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/list_type.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/list_type.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/los-angeles-arrests-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/missing-first-column.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/missing-first-column.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/missing-v-node-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/missing-values-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/missing-values-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/more-than-256-unique-strings-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/mtcars.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/names-need-repair-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/names-need-repair-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/new_line_errors.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/no-styles-or-sharedStrings-parts.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/no-yes-col-names.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/no-yes-col-names.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/nonstandard-xml-ns-prefix.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/numbers-as-na-and-shared-strings-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/numbers-as-na-and-shared-strings-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/richtext-coloured.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/sheet-xml-lookup.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/skipping.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/skipping.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/style-only-cells.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/style-only-cells.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/texty-dates-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/texty-dates-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/types.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/types.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/unnamed-duplicated-columns.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/unnamed-duplicated-columns.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/utf8-sheet-names.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/utf8-sheet-names.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/vietnamese-utf8.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/vietnamese-utf8.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/whitespace-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/whitespace-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/test-coercion.R
/usr/lib64/R/library/readxl/tests/testthat/test-col-names.R
/usr/lib64/R/library/readxl/tests/testthat/test-col-types.R
/usr/lib64/R/library/readxl/tests/testthat/test-compatibility.R
/usr/lib64/R/library/readxl/tests/testthat/test-dates.R
/usr/lib64/R/library/readxl/tests/testthat/test-empty.R
/usr/lib64/R/library/readxl/tests/testthat/test-encoding.R
/usr/lib64/R/library/readxl/tests/testthat/test-example.R
/usr/lib64/R/library/readxl/tests/testthat/test-formats.R
/usr/lib64/R/library/readxl/tests/testthat/test-geometry.R
/usr/lib64/R/library/readxl/tests/testthat/test-missing-values.R
/usr/lib64/R/library/readxl/tests/testthat/test-n-max.R
/usr/lib64/R/library/readxl/tests/testthat/test-problems.R
/usr/lib64/R/library/readxl/tests/testthat/test-read-excel.R
/usr/lib64/R/library/readxl/tests/testthat/test-return.R
/usr/lib64/R/library/readxl/tests/testthat/test-richtext.R
/usr/lib64/R/library/readxl/tests/testthat/test-shared-string-table.R
/usr/lib64/R/library/readxl/tests/testthat/test-sheets.R
/usr/lib64/R/library/readxl/tests/testthat/test-skipping.R
/usr/lib64/R/library/readxl/tests/testthat/test-trim-ws.R
/usr/lib64/R/library/readxl/tests/testthat/test-xml-namespaces.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/readxl/libs/readxl.so
/usr/lib64/R/library/readxl/libs/readxl.so.avx2
/usr/lib64/R/library/readxl/libs/readxl.so.avx512

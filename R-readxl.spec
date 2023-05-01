#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-readxl
Version  : 1.4.2
Release  : 56
URL      : https://cran.r-project.org/src/contrib/readxl_1.4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/readxl_1.4.2.tar.gz
Summary  : Read Excel Files
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: R-readxl-lib = %{version}-%{release}
Requires: R-readxl-license = %{version}-%{release}
Requires: R-cellranger
Requires: R-cpp11
Requires: R-progress
Requires: R-tibble
BuildRequires : R-cellranger
BuildRequires : R-cpp11
BuildRequires : R-progress
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
# readxl <img src='man/figures/logo.png' align="right" height="139" />
<!-- badges: start -->

%package lib
Summary: lib components for the R-readxl package.
Group: Libraries
Requires: R-readxl-license = %{version}-%{release}

%description lib
lib components for the R-readxl package.


%package license
Summary: license components for the R-readxl package.
Group: Default

%description license
license components for the R-readxl package.


%prep
%setup -q -n readxl
cd %{_builddir}/readxl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678837654

%install
export SOURCE_DATE_EPOCH=1678837654
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-readxl
cp %{_builddir}/readxl/LICENSE.note %{buildroot}/usr/share/package-licenses/R-readxl/bf07378c279323df68098ac0edfd7a53bf54842a || :
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
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/readxl/DESCRIPTION
/usr/lib64/R/library/readxl/INDEX
/usr/lib64/R/library/readxl/LICENSE
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
/usr/lib64/R/library/readxl/WORDLIST
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
/usr/lib64/R/library/readxl/tests/testthat/_snaps/coercion.md
/usr/lib64/R/library/readxl/tests/testthat/_snaps/col-types.md
/usr/lib64/R/library/readxl/tests/testthat/helper.R
/usr/lib64/R/library/readxl/tests/testthat/sheets/65536-rows-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/Ekaterinburg_IP_9.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/biff5-label-records.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/biff5-rich-text-string.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/big-texty-numbers-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/big-texty-numbers-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/blanks.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/blanks.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/color-date-lowercase-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/color-date-xls.xls
/usr/lib64/R/library/readxl/tests/testthat/sheets/color-date-xlsx.xlsx
/usr/lib64/R/library/readxl/tests/testthat/sheets/currency-formats-xlsx.xlsx
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
/usr/lib64/R/library/readxl/tests/testthat/test-excel-format.R
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-readxl/bf07378c279323df68098ac0edfd7a53bf54842a

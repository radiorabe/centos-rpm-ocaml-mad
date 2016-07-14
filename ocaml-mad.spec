Name:     ocaml-mad

Version:  0.4.5
Release:  1
Summary:  OCaml bindings for the libmad
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-mad
Source0:  https://github.com/savonet/ocaml-mad/releases/download/0.4.5/ocaml-mad-0.4.5.tar.gz

BuildRequires: ocaml
BuildRequires: libmad-devel
Requires:      libmad

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export OCAMLFIND_LDCONF=ignore
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
make install

%files
/usr/lib64/ocaml/mad/META
/usr/lib64/ocaml/mad/dllmad_stubs.so
/usr/lib64/ocaml/mad/libmad_stubs.a
/usr/lib64/ocaml/mad/mad.a
/usr/lib64/ocaml/mad/mad.cma
/usr/lib64/ocaml/mad/mad.cmi
/usr/lib64/ocaml/mad/mad.cmx
/usr/lib64/ocaml/mad/mad.cmxa
/usr/lib64/ocaml/mad/mad.mli

%description
OCAML bindings for the libmad based on based on Madlld example.


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-mad.spec

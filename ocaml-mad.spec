Name:     ocaml-mad

Version:  0.4.5
Release:  2
Summary:  OCaml bindings for the libmad
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-mad
Source0:  https://github.com/savonet/ocaml-mad/releases/download/0.4.5/ocaml-mad-0.4.5.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
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
%{_libdir}/ocaml/mad/META
%{_libdir}/ocaml/mad/dllmad_stubs.so
%{_libdir}/ocaml/mad/libmad_stubs.a
%{_libdir}/ocaml/mad/mad.a
%{_libdir}/ocaml/mad/mad.cma
%{_libdir}/ocaml/mad/mad.cmi
%{_libdir}/ocaml/mad/mad.cmx
%{_libdir}/ocaml/mad/mad.cmxa
%{_libdir}/ocaml/mad/mad.mli

%description
OCAML bindings for the libmad based on based on Madlld example.


%changelog
* Fri Nov 23 2018 Lucas Bickel <hairmare@rabe.ch> - 0.4.5-2
- Require missing ocaml-findlibs
- Start cleaning up files section

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-mad.spec

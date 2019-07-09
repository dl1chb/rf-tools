# rf-tools
SPEC-Files for the COPR rf-tools repository.

This Repo is for everyone who wants to build this packages on their own and for bugs and disucussions regarding
the copr repo https://copr.fedorainfracloud.org/coprs/beckus/rf-tools/

Please consider the use of it at your own risk! Some packages might not be build with the caution they are supposed
to, but I will keep an eye on it.

The RPMs are build using rpmbuild and mock, like:
$ rpmbuild -bs foo.spec
$ mock -r <"whatever architecture you want" foo.srpm
Later they are just uploaded to copr by using "copr-cli build rf-tools foo.srpm"

Maybe you need to use "spectool -g -R file.spec" to download ne necessary sources
